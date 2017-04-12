########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import matplotlib.pyplot as plt
import json

def plot(api, images, aoi):
    # GeoJSON FeatureCollection containing footprints and properties of the scenes
    metadata = api.get_footprints()#images
    properties = [metadata.features[i].properties for i in range(0, len(images))]
    footprints = [metadata.features[i].geometry.coordinates for i in range(0,len(images))]

    # Get coordinates of the Area of Interest (AOI)
    with open(aoi) as geojson_file:
        geojson = json.load(geojson_file)
    for feature in geojson['features']:
        polygon = (feature['geometry'])
    aoi_coordinates = polygon['coordinates']
    aoi_x_coordinates = [aoi_coordinates[0][i][0] for i in range(0,len(aoi_coordinates[0]))]
    aoi_y_coordinates = [aoi_coordinates[0][i][1] for i in range(0,len(aoi_coordinates[0]))]

    plt.ion()

    # Plot Footprints and AOI
    for i in range(0,len(images)):
        plt.plot(*zip(*footprints[i][0]), label='Image '+str(properties[i]['product_id']), linestyle='dashed')
        plt.plot(aoi_x_coordinates, aoi_y_coordinates, 'r')
        plt.legend()

    plt.show()