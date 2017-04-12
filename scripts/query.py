########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

from sentinelsat.sentinel import *
from sentinelsat.sentinel import get_coordinates
import base64

def query_images(username, password, start_date, end_date, aoi, platform, max_cloud_cover, query_status=None):
    global images
    password = base64.b64decode(password)
    if max_cloud_cover is not None or max_cloud_cover!='':
        cloud_cover_percentage = '[0 TO '+max_cloud_cover+']'
    try:

        # Try to connect to ApiHub, else use SciHub
        try:
            api = SentinelAPI(username, password, 'https://scihub.copernicus.eu/apihub/')
        except:
            api = SentinelAPI(username, password, 'https://scihub.copernicus.eu/dhus/')

        # Search images by polygon, start and end date, and SciHub query keywords
        if platform == None or platform == '' and max_cloud_cover == None or max_cloud_cover == '':
            images = api.query(get_coordinates(aoi), start_date, end_date)
        elif platform != None and max_cloud_cover != None or max_cloud_cover != '':
            if platform=='Sentinel-1':
                images = api.query(get_coordinates(aoi), start_date, end_date, platformname=platform)
            else:
                images = api.query(get_coordinates(aoi), start_date, end_date, platformname=platform, cloudcoverpercentage = cloud_cover_percentage)
        elif platform == None or platform == '' and max_cloud_cover != None or max_cloud_cover != '':
            images = api.query(get_coordinates(aoi), start_date, end_date, cloudcoverpercentage = cloud_cover_percentage)
        else:
            images = api.query(get_coordinates(aoi), start_date, end_date, platformname=platform)

        if query_status is not None:
            if len(images)==1:
                query_status.set(str(len(images)) + " image found.")
            else:
                query_status.set(str(len(images)) + " images found.")

    except SentinelAPIError as apiError:
        error_message = apiError.msg.replace('\n',' ').replace('# ','')
        if query_status is not None:
            query_status.set(error_message)

    return api, images