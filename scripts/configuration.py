########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import tkFileDialog

# Read configuration .txt file and save lines to variables
def read_txt(config_file):
    input = []

    for line in config_file:
        line = line.strip()
        if line:
            input.append(line)
        else:
            input.append('')
    config_file.close()

    # save input data in corresponding variables
    username = input[0]
    password = input[1]
    start_date = input[2]
    end_date = input[3]
    aoi = input[4]
    platform = input[5]
    max_cloud_cover = input[6]
    download_path = input[7]
    image_id = input[8]
    download_options = input[9]
    image_path = input[10]
    preprocessing_options = input[11]

    return username, password, start_date, end_date, aoi, platform, max_cloud_cover, download_path, image_id, download_options, image_path, preprocessing_options

# Write configuration .txt file with given variables
def write_txt(username=None, password=None, start_date=None, end_date=None, aoi=None, platform=None, max_cloud_cover=None, download_path=None, image_id=None, download_options=None, image_path=None, preprocessing_options=None):
    config_file = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=(('Text','*.txt'),("All Files", "*.*")))
    if username:
        config_file.write(username+'\n')
    else:
        config_file.write('\n')
    if password:
        config_file.write(password+'\n')
    else:
        config_file.write('\n')
    if start_date:
        config_file.write(start_date+'\n')
    else:
        config_file.write('\n')
    if end_date:
        config_file.write(end_date+'\n')
    else:
        config_file.write('\n')
    if aoi:
        config_file.write(aoi+'\n')
    else:
        config_file.write('\n')
    if platform:
        config_file.write(platform+'\n')
    else:
        config_file.write('\n')
    if max_cloud_cover:
        config_file.write(max_cloud_cover+'\n')
    else:
        config_file.write('\n')
    if download_path:
        config_file.write(download_path+'\n')
    else:
        config_file.write('\n')
    if image_id:
        config_file.write(image_id+'\n')
    else:
        config_file.write('\n')
    if download_options:
        config_file.write(download_options+'\n')
    else:
        config_file.write('\n')
    if image_path:
        config_file.write(image_path+'\n')
    else:
        config_file.write('\n')
    if preprocessing_options:
        config_file.write(preprocessing_options+'\n')
    else:
        config_file.write('\n')