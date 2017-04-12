########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import os
import metadata
import footprints

# Check downloading options and start according actions
def start(api, images, download_path, product_id, download_options, aoi, download_status=None):
    if 'save_metadata' in download_options:
        metadata.export(api, images, download_path)
        if download_status:
            download_status.set('Metadata downloaded.')
    if 'plot_footprints' in download_options:
        footprints.plot(api, images, aoi)
        if download_status:
            download_status.set('Footprints plotted.')
    if 'download_test_image' in download_options:
        image(api, product_id, download_path)
        if download_status:
            download_status.set('Test image downloaded.')
    if 'download_all' in download_options:
        all(api, download_path, images)
        if download_status:
            download_status.set('Images downloaded.')
    elif download_options==None or download_options=='':
        if download_status:
            download_status.set('Please select a download option.')
        else:
            pass

# Method for downloading all queried images
def all(api, output_path, images):
    metadata = api.get_footprints()#images
    properties = [metadata.features[i].properties for i in range(0, len(images))]
    if not os.path.exists(output_path+'\Sentinel-1'):
        os.makedirs(output_path+'\Sentinel-1')
    if not os.path.exists(output_path + '\Sentinel-2'):
        os.makedirs(output_path+'\Sentinel-2')
    for i in range(0, len(properties)):
        if properties[i]['platformname'] == 'Sentinel-1':
            api.download(properties[i]['product_id'], output_path+'\Sentinel-1', check_existing=True)
        elif properties[i]['platformname'] == 'Sentinel-2':
            api.download(properties[i]['product_id'], output_path+'\Sentinel-2', check_existing=True)

# Method for downloading one image by its product id
def image(api, product_id, output_path):
    api.download(product_id, output_path)