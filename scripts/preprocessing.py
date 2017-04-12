########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
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
    
def subset(image_path, aoi):
    path = image_path
    for folder in os.listdir(path):
        if folder.endswith('.zip'):
            zip_ref = zipfile.ZipFile(path + folder, 'r')
            zip_ref.extractall(path)
            zip_ref.close()
    for folder in os.listdir(path):
        output = path + folder + '/'
        # Read Data____________________________________________________________
        if folder.endswith('.SAFE'):
            for file in os.listdir(output):
                if file.endswith('.xml') and file!='INSPIRE.xml': sentinel = ProductIO.readProduct(output+file)  
            # Get Band Names
            band_names = sentinel.getBandNames()
            print("Bands:       %s" % (list(band_names)))
            # Preprocessing ___________________________________________________
            # Resampling
            parameters = HashMap()
            parameters.put('targetResolution', 10)
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
            print("SUBSET: Writing.")
            subset = output+'_subset_'
            ProductIO.writeProduct(product_sub, subset, "GeoTIFF")
            
            print("SUBSET: Done.")


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
    para       = {'northBound': NE[1], 'eastBound': NE[0], 'southBound': SW[1], 'westBound': SW[0]-0.05, \
                  'pixelSizeX': 0.0001, 'pixelSizeY': 0.0001}    
    # Write Data_______________________________________________________________
    mosaicOp().mosaic(products, trg_path, bands, para)




