########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann, TU Munich
#   Date: January 18, 2017
#
########################################################################################################################

## IMPORT LIB

import os 
import snappy
from snappy import ProductIO
from snappy import HashMap
import json
import geojson
from shapely.geometry import shape    
from snappy import GPF
import zipfile
from snappy_01_mosaic import mosaicOp

## GET SNAP TOOLS ##___________________________________________________________

GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()
HashMap = snappy.jpy.get_type('java.util.HashMap')
SubsetOp = snappy.jpy.get_type('org.esa.snap.core.gpf.common.SubsetOp')
WKTReader = snappy.jpy.get_type('com.vividsolutions.jts.io.WKTReader')
snappy.GPF.getDefaultInstance().getOperatorSpiRegistry().loadOperatorSpis()

def start(image_path, aoi, preprocessing_options, preprocessing_status=None):
    if 'subset' in preprocessing_options:
        subset(image_path, aoi)
        if preprocessing_status is not None:
            preprocessing_status.set('Create Subset.')
    if 'mosaic' in preprocessing_options:
        mosaic(image_path, aoi)
        if preprocessing_status is not None:
            preprocessing_status.set('Create Mosaic.')
    else:
        if preprocessing_status is not None:
            preprocessing_status.set('Please select a preproccessing option.')
        else:
            pass  

        
def ziparchive(image_path, aoi):
    for folder in os.listdir(image_path):
        if folder.endswith('.zip'):
            zip_ref = zipfile.ZipFile(image_path + folder, 'r')
            zip_ref.extractall(image_path)
            zip_ref.close()
                
    
def subset(image_path, aoi): 
    for folder in os.listdir(image_path):
        # Zipped Folder________________________________________________________
        if folder.endswith('.zip'): 
            ziparchive(image_path, aoi)
            # Use current path for subset
            path = image_path + folder + '/'
            # Check if Sentine-1 or Sentinel-2
            if folder.startswith('S1'):
                for file in os.listdir(path):
                    if file.endswith('manifest.safe') and "_GRD" in folder: subset_s1(path, file, aoi)
            if folder.startswith('S2') and folder.endswith('.SAFE'):
                for file in os.listdir(path):
                    if file.endswith('.xml') and file!='INSPIRE.xml': subset_s2(path, file, aoi)
                    
        # Unzipped Folder______________________________________________________
        # Use current path for subset
        path = image_path + folder + '/'
        # Check if Sentine-1 or Sentinel-2
        if folder.startswith('S1'):
            for file in os.listdir(path):
                if file.endswith('manifest.safe') and "_GRD" in folder: subset_s1(path, file, aoi)
        if folder.startswith('S2') and folder.endswith('.SAFE'):
            for file in os.listdir(path):
                if file.endswith('.xml') and file!='INSPIRE.xml': subset_s2(path, file, aoi)
            
                
def subset_s2(path, file, aoi):
    # Read Data________________________________________________________________
    print("SUBSET: Read Product...")
    sentinel = ProductIO.readProduct(path+file)
    print("SUBSET: Done reading!")
    # Get Band Names and print info
    name = sentinel.getName()
    print("SUBSET: Image ID:        %s" % name)
    band_names = sentinel.getBandNames()
    print("SUBSET: Bands:       %s" % (list(band_names)))
    # Preprocessing ___________________________________________________________
    # Resampling
    parameters = HashMap()
    parameters.put('targetResolution', 10)
    print("SUBSET: resample target resolution: 10m")
    product_resample = snappy.GPF.createProduct('Resample', parameters, sentinel)
    # Geojson to wkt
    with open(aoi) as f:
            gjson = json.load(f)       
    for feature in gjson['features']:
        polygon = (feature['geometry'])
    str_poly = json.dumps(polygon)
    gjson_poly = geojson.loads(str_poly)
    poly_shp = shape(gjson_poly)
    wkt = poly_shp.wkt
    # Subset
    geom = WKTReader().read(wkt)
    op = SubsetOp()
    op.setSourceProduct(product_resample)
    op.setGeoRegion(geom)
    product_sub = op.getTargetProduct()            
    # Write Data_______________________________________________________            
    print("SUBSET: Writing subset.")
    subset = path + name + '_subset_'
    ProductIO.writeProduct(product_sub, subset, "BEAM-DIMAP")    
    print("SUBSET: Done and saved in %s" % path)

def subset_s1(path, file, aoi):
    # Read Data________________________________________________________________
    print("SUBSET: Read Product...")
    sentinel = ProductIO.readProduct(path+file)
    print("SUBSET: Done reading!")
    name = sentinel.getName()
    print(name)
    # Get Polarisation and Name
    pols = ['VV'] # WISHLIST only VV works right now, should be changed to HH and VH
    for p in pols:
        print("SUBSET: calibration:   %s" % p)
        polarization = p
        # Preprocessing________________________________________________________
        # Calibration
        parameters = HashMap() 
        parameters.put('outputSigmaBand', True) 
        parameters.put('sourceBands', 'Intensity_' + polarization) 
        parameters.put('selectedPolarisations', polarization) 
        parameters.put('outputImageScaleInDb', False)      
        calib = path + file + "_calibrate_" + polarization 
        target_0 = GPF.createProduct("Calibration", parameters, sentinel) 
        ProductIO.writeProduct(target_0, calib, 'BEAM-DIMAP')
        calibration = ProductIO.readProduct(calib + ".dim")
        # Geojson to wkt
        with open(aoi) as f:
                gjson = json.load(f)       
        for feature in gjson['features']:
            polygon = (feature['geometry'])
        str_poly = json.dumps(polygon)
        gjson_poly = geojson.loads(str_poly)
        poly_shp = shape(gjson_poly)
        wkt = poly_shp.wkt
        # Subset
        geom = WKTReader().read(wkt)
        subsettings = HashMap()
        subsettings.put('geoRegion', geom)
        subsettings.put('outputImageScaleInDb', False)
        # Write Data_______________________________________________________            
        print("SUBSET: Writing subset.")  
        subset = path + file + "_subset_" + polarization
        target_1 = GPF.createProduct("Subset", subsettings, calibration)
        ProductIO.writeProduct(target_1, subset, 'BEAM-DIMAP')
        print("SUBSET: Done and saved in %s" % path)
        
        
def mosaic(image_path, aoi):   
    path = image_path
    # Unzip Downloaded Data
    for folder in os.listdir(path):
        if folder.endswith('.zip'):
            zip_ref = zipfile.ZipFile(path + folder, 'r')
            zip_ref.extractall(path)
            zip_ref.close()
    # Select Folder
    src_path = []
    for folder in os.listdir(path):
        if folder.endswith('.SAFE'):
            src_path.append(path + folder + '/')                
    src_path_1 = src_path[0]
    src_path_2 = src_path[1]            
    trg_path = image_path       
    # Read Data________________________________________________________________
    products   = []
    products.append(ProductIO.readProduct(src_path_1))
    products.append(ProductIO.readProduct(src_path_2))
    # Preprocessing____________________________________________________________
    # Bounding Box
    with open(aoi) as f:
        geojson = json.load(f)
    for feature in geojson['features']:
        polygon = (feature['geometry'])
    coordinates = polygon['coordinates']
    print(coordinates)
    NE = coordinates[0][2]
    SW = coordinates[0][0]
    # Resampling
    parameters = HashMap()
    parameters.put('targetResolution', 10)
    product_resample_0 = snappy.GPF.createProduct('Resample', parameters, products[0])
    product_resample_1 = snappy.GPF.createProduct('Resample', parameters, products[1])
    products = [product_resample_0, product_resample_1]
    # Get Band Names
    band_names = products[0].getBandNames()
    print("Bands:       %s" % (list(band_names)))  
    # Mosaic for every Band              
    bands      = {'B2': 'B2'}
    para       = {'northBound': NE[1], 'eastBound': NE[0], 'southBound': SW[1], 'westBound': SW[0], \
                  'pixelSizeX': 0.0001, 'pixelSizeY': 0.0001}    
    # Write Data_______________________________________________________________
    mosaicOp().mosaic(products, trg_path, bands, para)




