########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

import base64
from Tkinter import *

# Get entries from widgets
def get(textbox_username=None, textbox_password=None, textbox_start_date=None, textbox_end_date=None,textbox_aoi=None,
        variable_sentinel1=None, variable_sentinel2=None, textbox_cloud_cover=None, textbox_download_path=None,
        textbox_product_id=None, variable_save_metadata=None, variable_plot_footprints=None,
        variable_download_test_image=None, variable_download_all=None, textbox_image_path=None, variable_mosaick=None,
        variable_subset=None):

    return_list = []
    if textbox_username:
        username = textbox_username.get().strip()
        return_list.append(username)
    if textbox_password:
        password = base64.b64encode(textbox_password.get().strip())
        return_list.append(password)
    if textbox_start_date:
        start_date = textbox_start_date.get().strip()
        try:
            start_date_list = start_date.split('.')
            start_date = start_date_list[2]+start_date_list[1]+start_date_list[0]
        except:
            if start_date == '':
                pass
            else:
                raise ValueError('Start date needs to be in the format of dd.mm.yyyy')
        return_list.append(start_date)
    if textbox_end_date:
        end_date = textbox_end_date.get().strip()
        try:
            end_date_list = end_date.split('.')
            end_date = end_date_list[2]+end_date_list[1]+end_date_list[0]
        except:
            if end_date == '':
                pass
            else:
                raise ValueError('End date needs to be in the format of dd.mm.yyyy')
        return_list.append(end_date)
    if textbox_aoi:
        aoi = textbox_aoi.get().strip()
        return_list.append(aoi)
    if variable_sentinel1 or variable_sentinel2:
        if variable_sentinel1.get() == 1 and variable_sentinel2.get() == 0:
            platform = 'Sentinel-1';
        elif variable_sentinel1.get() == 0 and variable_sentinel2.get() == 1:
            platform = 'Sentinel-2';
        else:
            platform = None;
        return_list.append(platform)
    if textbox_cloud_cover:
        max_cloud_cover = textbox_cloud_cover.get().strip()
        return_list.append(max_cloud_cover)
    if textbox_download_path:
        download_path = textbox_download_path.get().strip()
        return_list.append(download_path)
    if textbox_product_id:
        product_id = str(textbox_product_id.get()).strip()
        return_list.append(product_id)
    if variable_save_metadata or variable_plot_footprints or variable_download_test_image or variable_download_all:
        download_options = ''
        if variable_save_metadata.get() == 1:
            download_options=download_options+'save_metadata '
        if variable_plot_footprints.get() == 1:
            download_options=download_options+'plot_footprints '
        if variable_download_test_image.get() == 1:
            download_options=download_options+'download_test_image '
        if variable_download_all.get() == 1:
            download_options=download_options+'download_all '
        return_list.append(download_options)
    if textbox_image_path:
        image_path = str(textbox_image_path.get()).strip()
        return_list.append(image_path)
    if variable_subset or variable_mosaick:
        preprocessing_options = ''
        if variable_mosaick.get() == 1 and variable_subset.get() == 0:
            preprocessing_options=preprocessing_options+'mosaick '
        elif variable_subset.get() == 1 and variable_mosaick.get() == 0:
            preprocessing_options=preprocessing_options+'subset '
        elif variable_subset.get() == 1 and variable_mosaick.get() == 1:
            preprocessing_options = preprocessing_options+'subset '+'mosaick '
        else:
            preprocessing_options = ''
        return_list.append(preprocessing_options)

    return return_list

# Set widget entries
def set(username, password, start_date, end_date, aoi, platform, max_cloud_cover, download_path, download_options, image_id, image_path,
        preprocessing_options, textbox_username, textbox_password, textbox_start_date, textbox_end_date, textbox_aoi,
        variable_sentinel1, variable_sentinel2, textbox_cloud_cover, textbox_download_path, textbox_image_id, variable_save_metadata,
        variable_plot_footprints, variable_download_test_image, variable_download_all, textbox_image_path, variable_mosaick, variable_subset):

    textbox_username.insert(INSERT, username)
    textbox_password.insert(INSERT, base64.b64decode(password))
    if start_date != '':
        start_date = start_date[6:8]+'.'+start_date[4:6]+'.'+start_date[0:4]
    textbox_start_date.insert(INSERT, start_date)
    if end_date != '':
        end_date = end_date[6:8] + '.' + end_date[4:6] + '.' + end_date[0:4]
    textbox_end_date.insert(INSERT, end_date)
    textbox_aoi.insert(INSERT, aoi)
    if platform == 'Sentinel-1':
        variable_sentinel1.set(1)
        variable_sentinel2.set(0)
    if platform == 'Sentinel-2':
        variable_sentinel1.set(0)
        variable_sentinel2.set(1)
    if platform == None or platform == '':
        variable_sentinel1.set(1)
        variable_sentinel2.set(1)
    textbox_cloud_cover.insert(INSERT, max_cloud_cover)
    textbox_download_path.insert(INSERT, download_path)
    textbox_image_id.insert(INSERT, image_id)
    if "save_metadata" in download_options:
        variable_save_metadata.set(1)
    if "plot_footprints" in download_options:
        variable_plot_footprints.set(1)
    if "download_test_image" in download_options:
        variable_download_test_image.set(1)
    if "download_all" in download_options:
        variable_download_all.set(1)
    textbox_image_path.insert(INSERT, image_path)
    if "mosaick" in preprocessing_options:
        variable_mosaick.set(1)
    if "subset" in preprocessing_options:
        variable_subset.set(1)