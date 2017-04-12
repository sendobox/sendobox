########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import configuration
import query
import download
import preprocessing

# Get path of configuration file
config_file_path = raw_input("Please type the path of your .txt configuration file: ")
config_file = open(config_file_path, "r")

# Retrieve input parameters from configuration file
[username, password, start_date, end_date, area_of_interest, platform, max_cloud_cover, download_path, product_id,
 download_options, image_path, preprocessing_options] = configuration.read_txt(config_file)

# Query images
[api, images] = query.query_images(username, password, start_date, end_date, area_of_interest, platform, max_cloud_cover)

# Download images
download.start(api, images, download_path, product_id, download_options, area_of_interest)

# Preprocessing
preprocessing.start(image_path, area_of_interest, preprocessing_options)