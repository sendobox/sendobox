########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Adaption of Adreas Baumann http://forum.step.esa.int/users/abgbaumann/activity
#   Date: March 29, 2017
#
########################################################################################################################

## IMPORT LIB

import os
import re

class basicOp(object):   
    
    def __init__(self):
        # Constants
        global length_1deg_equ
        global length_1deg_mer
        global km2m
        
        length_1deg_equ = 40075.0 / 360.0 # WGS84
        length_1deg_mer = 20004.0 / 180.0 # WGS84
        km2m = 1000        
        
        
        
    # Get a list of all folders in a certain directory
    @staticmethod
    def searchForFolders(PATH='.'):
        '''
        -----------------------------------------------------------------------------------------------        
        This function gives back a list of directories in a defined folder.
        -----------------------------------------------------------------------------------------------
        Parameter(s):   - PATH [optional]:       Path to a directory.
                                                 DEFAULT: Takes the directory of the script.
        -----------------------------------------------------------------------------------------------
        '''
        DIR_NAMES =  [NAME for NAME in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, NAME))]
        return DIR_NAMES
    
    @staticmethod
    def searchForFiles(PATH='.',EXT='ALL'):
        '''
        -----------------------------------------------------------------------------------------------        
        This function gives back a list of files in a defined folder.
        -----------------------------------------------------------------------------------------------
        Parameter(s):   - PATH [optional]:       Path to a directory.
                                                 DEFAULT: Takes the directory of the script.
                        - EXT [optional]:        Ending of the file name (e.g. 'doc','.xml','ome.txt')
                                                 DEFAULT: Searches for all Files
        -----------------------------------------------------------------------------------------------
        '''
        FILE_NAME_LIST = []
        if EXT != 'ALL':
            for file in os.listdir(PATH):
                if file.endswith(EXT):  
                    FILE_NAME_LIST.append(file)
        else:
            for file in os.listdir(PATH):
                if file.endswith('*.*'):  
                    FILE_NAME_LIST.append(file)
        return FILE_NAME_LIST
    
    @staticmethod
    def checkForExpression(name, reg='S2.{1}_.{4}_.{3}_.{6}_.{4}_.{15}_.{4}_V.{15}_.{15}.xml'):
        r = re.compile(reg)
        if r.match(name) is not None:
            return True
        else:
            return False
    
    def s2folder(self, PATH='.'):
        '''
        -----------------------------------------------------------------------------------------------        
        This function checks if the input directory has the S2 structure (first layer)
        -----------------------------------------------------------------------------------------------
        Parameter(s):   - PATH [optional]:       Path to a possible S2 directory
                                                 DEFAULT: Takes the directory of the script.
        -----------------------------------------------------------------------------------------------
        '''        
        DIR_LIST  = self.searchForFolders(PATH)
        dir_exist = 0
        
        for DIR in DIR_LIST:
            if DIR == 'AUX_DATA' or \
               DIR == 'DATASTRIP' or \
               DIR == 'GRANULE' or \
               DIR == 'HTML' or \
               DIR == 'rep_info':
                dir_exist = dir_exist + 1
                
        if dir_exist == 5:
            return True
        else:
            return False
        
    def PointlistToPolygon(self, POINT_PATH):
        f = open(POINT_PATH, 'r')
        lat = []
        lon = []
        
        for (j, line) in enumerate(f):
            line = line.replace('\n','')
            line = line.split(',')
            
            for (i, coord) in enumerate(line):
                if coord[-1] == 'N':
                    lat_c = float(coord[:-1])
                    lat.append(lat_c)
                    if j == 0:
                        lat_end = lat_c
                elif coord[-1] == 'S':
                    lat_c = -float(coord[:-1])
                    lat.append(x_c)     
                    if j == 0:
                        lat_end = lat_c                    
                elif coord[-1] == 'E':
                    lon_c = float(coord[:-1])
                    lon.append(lon_c)
                    if j == 0:
                        lon_end = lon_c                     
                elif coord[-1] == 'W':
                    lon_c = -float(coord[:-1])
                    lon.append(lon_c)
                    if j == 0:
                        lon_end = lon_c
        lat.append(lat_end)
        lon.append(lon_end)
        
        str_poly = "POLYGON(("
        
        for (i,lat_i) in enumerate(lat):
            if i == 0:
                str_poly = str_poly + str(lon[i]) + ' ' + str(lat[i])
            else:
                str_poly = str_poly + ', ' + str(lon[i]) + ' ' + str(lat[i])
        
        str_poly = str_poly + "))"
        return str_poly
    
    def BoundingBox(self, data):
        
        # Java - Python bridge                                        
        from snappy import jpy    
        
        
        # The GeoPos class represents a geographical position measured in longitudes and latitudes.
        # http://step.esa.int/docs/v2.0/apidoc/engine/org/esa/snap/core/datamodel/GeoPos.html
        geoPos = jpy.get_type('org.esa.snap.core.datamodel.GeoPos') 
        
        # A PixelPos represents a position or point in a pixel coordinate system.
        # http://step.esa.int/docs/v2.0/apidoc/engine/org/esa/snap/core/datamodel/PixelPos.html
        pixelPos = jpy.get_type('org.esa.snap.core.datamodel.PixelPos')  
        
        geoCoding = data.getSceneGeoCoding()
        sceneUL = pixelPos(0 + 0.5, 0 + 0.5)
        sceneUR = pixelPos(data.getSceneRasterWidth() - 1 + 0.5, 0 + 0.5)
        sceneLL = pixelPos(0 + 0.5, data.getSceneRasterHeight() - 1 + 0.5)
        sceneLR = pixelPos(data.getSceneRasterWidth() - 1 + 0.5, data.getSceneRasterHeight() - 1 + 0.5)   
        
        gp_ul = geoCoding.getGeoPos(sceneUL, geoPos())
        gp_ur = geoCoding.getGeoPos(sceneUR, geoPos())
        gp_ll = geoCoding.getGeoPos(sceneLL, geoPos())
        gp_lr = geoCoding.getGeoPos(sceneLR, geoPos())
        
        coo_left  = [ gp_ul.getLon(), gp_ll.getLon()]
        coo_right = [ gp_ur.getLon(), gp_lr.getLon()]
        coo_lower = [ gp_ll.getLat(), gp_lr.getLat()]
        coo_upper = [ gp_ul.getLat(), gp_ur.getLat()]
        
        # Get Bounding Box
        bbox = [min(coo_left), max(coo_right), min(coo_lower), max(coo_upper)]
        
        # Get Pixel Size (GSD) [Degree]
        d_upper_EW = coo_right[0] - coo_left[0]
        d_lower_EW = coo_right[1] - coo_left[1]
        
        pxSzE_deg = d_upper_EW / data.getSceneRasterWidth()
        pxSzW_deg = d_lower_EW / data.getSceneRasterWidth()
        
        pxSz_EW_deg = (pxSzE_deg + pxSzW_deg) / 2.0
        
        d_left_NS   = coo_upper[0] - coo_lower[0]
        d_right_NS  = coo_upper[1] - coo_lower[1]
        
        pxSzS_deg = d_left_NS / data.getSceneRasterHeight()
        pxSzN_deg = d_right_NS / data.getSceneRasterHeight()        
        pxSz_NS_deg = (pxSzS_deg + pxSzN_deg) / 2.0
        
        return bbox, pxSz_EW_deg, pxSz_NS_deg
    
    def deg2m(self, bbox_SN, pxSz_EW_deg, pxSz_NS_deg):  
        from math import cos
        from math import pi   
        
        # Get Pixel Size (GSD) [Meter]
        avg_NS_deg = (bbox_SN[2] + bbox_SN[3]) / 2.0
        avg_NS_rad = avg_NS_deg * pi / 180.0
        
        pxSz_EW_m  = cos(avg_NS_rad) * length_1deg_equ * (pxSz_EW_deg[0] + pxSz_EW_deg[1]) / 2 * km2m
        pxSz_NS_m  = length_1deg_mer * (pxSz_NS_deg[0] + pxSz_NS_deg[1]) / 2 * km2m 
        
        return pxSz_EW_m, pxSz_NS_m
    
    def m2deg(self, bbox_SN, pxSz_EW_m, pxSz_NS_m):
        from math import cos
        from math import pi   
        
        # Get Pixel Size (GSD) [Degree]
        avg_NS_deg = (bbox_SN[2] + bbox_SN[3]) / 2.0
        avg_NS_rad = avg_NS_deg * pi / 180.0
        
        pxSz_EW_deg = pxSz_EW_m / ( cos(avg_NS_rad) * length_1deg_equ * km2m)
        pxSz_NS_deg = pxSz_NS_m / ( length_1deg_mer * km2m)
        
        return pxSz_EW_deg, pxSz_NS_deg
        