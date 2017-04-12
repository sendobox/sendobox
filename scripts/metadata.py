########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import os

# Method for saving metadata of the images in a csv file to the given output path
def export(api, images, output_path):

    # GeoJSON FeatureCollection containing footprints and metadata of the scenes
    metadata = api.get_footprints()#images
    properties = [metadata.features[i].properties for i in range(0, len(images))]

    # Create folder structure if it does not exist yet
    if not os.path.exists(output_path+'\Sentinel-1'):
        os.makedirs(output_path+'\Sentinel-1')
    if not os.path.exists(output_path + '\Sentinel-2'):
        os.makedirs(output_path+'\Sentinel-2')

    # Prepare .csv files (one for Sentinel-1, one for Sentinel-2)
    output_sentinel1 = open(output_path + '/Sentinel-1/sentinel-1.csv', 'w')
    output_sentinel1.write('id;image_id;mode;product_type;polarisation;orbit_direction;sensing_date;product_id\n')
    output_sentinel1.close()

    output_sentinel2 = open(output_path + '/Sentinel-2/sentinel-2.csv', 'w')
    output_sentinel2.write('id;image_id;mode;product_type;orbit_direction;sensing_date;product_id\n')
    output_sentinel2.close()

    output_sentinel1 = open(output_path + '/Sentinel-1/sentinel-1.csv', 'a')
    output_sentinel2 = open(output_path + '/Sentinel-2/sentinel-2.csv', 'a')

    zeile_sentinel1 = 1
    zeile_sentinel2 = 1

    # Write metadata to .csv files
    for i in range(0, len(properties)):

        if properties[i]['platformname'] == 'Sentinel-1':
            output_sentinel1.write(str(zeile_sentinel1)+';')
            output_sentinel1.write(properties[i]['identifier']+';')
            output_sentinel1.write(properties[i]['sensoroperationalmode'] + ';')
            output_sentinel1.write(properties[i]['producttype'] + ';')
            output_sentinel1.write(properties[i]['polarisationmode'] + ';')
            output_sentinel1.write(properties[i]['orbitdirection'] + ';')
            output_sentinel1.write(properties[i]['date_beginposition'] + ';')
            output_sentinel1.write(properties[i]['product_id'] + ';')
            output_sentinel1.write('\n')
            zeile_sentinel1 += 1

        elif properties[i]['platformname'] == 'Sentinel-2':
            output_sentinel2.write(str(zeile_sentinel2)+';')
            output_sentinel2.write(properties[i]['identifier']+';')
            output_sentinel2.write(properties[i]['sensoroperationalmode'] + ';')
            output_sentinel2.write(properties[i]['producttype'] + ';')
            output_sentinel2.write(properties[i]['orbitdirection'] + ';')
            output_sentinel2.write(properties[i]['date_beginposition'] + ';')
            output_sentinel2.write(properties[i]['product_id'] + ';')
            output_sentinel2.write('\n')
            zeile_sentinel2 += 1

    output_sentinel1.close()
    output_sentinel2.close()