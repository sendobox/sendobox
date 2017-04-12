########################################################################################################################
#
#   Toolbox for batch downloading and preprocessing of Sentinel satellite data from Sentinels Scientific Data Hub
#   Contributors: Thomas Stark & Tatjana Buergmann (TU Munich)
#   Date: March 29, 2017
#
########################################################################################################################

# Import Tkinter dependencies
import Tkinter
from Tkinter import *
import tkFont
import tkFileDialog

# Import Modules
import configuration
import entries
import query
import download
import preprocessing

main_window = Tk()
main_window.wm_title("Sentinel Download Toolbox")

custom_font = tkFont.Font(family="Arial", size=10)
title_font = tkFont.Font(family="Arial", size=11, weight=tkFont.BOLD)

########################################################################################################################
# General Functions
########################################################################################################################

# Method for selecting all text in an entry widget (when pressing ctrl+a)
def select_all(event):
    event.widget.select_range(0, END)
    return "break"

# Method for deleting entries in all entry widgets (when pressing clear button)
def clear_all():
    textbox_username.delete(0, END)
    textbox_password.delete(0, END)
    textbox_start_date.delete(0, END)
    textbox_end_date.delete(0, END)
    textbox_aoi.delete(0, END)
    variable_sentinel1.set(0)
    variable_sentinel2.set(0)
    textbox_cloud_cover.delete(0, END)
    textbox_download_path.delete(0, END)
    textbox_product_id.delete(0, END)
    variable_save_metadata.set(0)
    variable_plot_footprints.set(0)
    variable_download_test_image.set(0)
    variable_download_all.set(0)
    textbox_image_path.delete(0, END)
    variable_mosaick.set(0)
    variable_subset.set(0)
    query_status.set('')
    download_status.set('')
    preprocessing_status.set('')

# Method for loading a configuration file
def load_config():
    config_file = tkFileDialog.askopenfile("r")
    # Get parameters from .txt file
    [username, password, start_date, end_date, area_of_interest, platform, max_cloud_cover, download_path, image_id, download_options,
     image_path, preprocessing_options] = configuration.read_txt(config_file)
    # Clear old values
    clear_all()
    # Set new settings
    entries.set(username, password, start_date, end_date, area_of_interest, platform, max_cloud_cover, download_path, download_options,
                image_id, image_path, preprocessing_options, textbox_username, textbox_password, textbox_start_date,
                textbox_end_date, textbox_aoi, variable_sentinel1, variable_sentinel2, textbox_cloud_cover, textbox_download_path,
                textbox_product_id, variable_save_metadata, variable_plot_footprints, variable_download_test_image,
                variable_download_all, textbox_image_path, variable_mosaick, variable_subset)

# Method for saving a configuration file
def save_configuration():
    try:
        [username, password, start_date, end_date, aoi, platform, max_cloud_cover, download_path, download_options, product_id, image_path,
         preprocessing_options] = entries.get(textbox_username, textbox_password, textbox_start_date, textbox_end_date,
                                              textbox_aoi, variable_sentinel1, variable_sentinel2, textbox_cloud_cover, textbox_download_path,
                                              textbox_product_id, variable_save_metadata, variable_plot_footprints,
                                              variable_download_test_image, variable_download_all, textbox_image_path,
                                              variable_mosaick, variable_subset)
    except ValueError:
        preprocessing_status.set(ValueError.message)
    configuration.write_txt(username, password, start_date, end_date, aoi, platform, max_cloud_cover, download_path, download_options,
                            product_id, image_path, preprocessing_options)

########################################################################################################################
# 1. Login
########################################################################################################################

label_login = Label(main_window, text="1. Login to Sentinels Scientific Data Hub", font=title_font)
label_login.grid(column=0, row=0, columnspan=4, sticky=W)

# Username
label_username = Label(main_window, text="Username:", font=custom_font)
label_username.grid(column=0, row=1, sticky=W)

textbox_username = Entry(main_window, font=custom_font)
textbox_username.grid(column=1, row=1, columnspan=2, sticky=W+E)
textbox_username.bind("<Control-Key-a>", select_all)
textbox_username.focus_set()

# Password
label_password = Label(main_window, text="Password:", font=custom_font)
label_password.grid(column=0, row=2, sticky=W)

textbox_password = Entry(main_window, show='*', font=custom_font)
textbox_password.grid(column=1, row=2, columnspan=2, sticky=W+E)
textbox_password.bind("<Control-Key-a>", select_all)

button_load_config = Tkinter.Button(main_window, text='Load configuration', command=load_config, font=custom_font)
button_load_config.grid(column=3, row=1, columnspan=2, rowspan=2)

########################################################################################################################
# 2. Query
########################################################################################################################

label_query = Label(main_window, text="2. Query options", font=title_font)
label_query.grid(column=0, row=3, columnspan=2, sticky=W)

# Start date
label_start_date = Label(main_window, text="Start date:", font=custom_font)
label_start_date.grid(column=0, row=4, sticky=W)

textbox_start_date = Entry(main_window, font=custom_font)
textbox_start_date.grid(column=1, row=4, columnspan=2, sticky=W+E)
textbox_start_date.bind("<Control-Key-a>", select_all)

# End date
label_end_date = Label(main_window, text="End date:", font=custom_font)
label_end_date.grid(column=0, row=5, sticky=W)

textbox_end_date = Entry(main_window, font=custom_font)
textbox_end_date.grid(column=1, row=5, columnspan=2, sticky=W+E)
textbox_end_date.bind("<Control-Key-a>", select_all)

# Area Of Interest (AOI)
label_aoi = Label(main_window, text="Area of Interest:", font=custom_font)
label_aoi.grid(column=0, row=6, sticky=W)

textbox_aoi = Entry(main_window, font=custom_font)
textbox_aoi.grid(column=1, row=6, columnspan=3, sticky=W+E)

# File dialog to get the AOI filename
def get_aoi_filename():
    global aoi_filename
    aoi_filename = tkFileDialog.askopenfilename(filetypes=[('geojson files', '.geojson'), ('all files', '.*')])
    textbox_aoi.insert(INSERT, aoi_filename)

button_aoi = Tkinter.Button(main_window, text='Open file', command=get_aoi_filename)
button_aoi.grid(column=4, row=6, sticky=W+E)

# Platform
label_platform = Label(main_window, text="Platform:", font=custom_font)
label_platform.grid(column=0, row=7, sticky=W)

# Checkbox for Sentinel-1
global variable_sentinel1
variable_sentinel1 = IntVar()
checkbutton_sentinel1 = Checkbutton(main_window, text="Sentinel-1", variable=variable_sentinel1, onvalue=1, offvalue=0,
                                    font=custom_font)
checkbutton_sentinel1.grid(column=1, row=7, sticky=W)

# Checkbox for Sentinel-2
global variable_sentinel2
variable_sentinel2 = IntVar()
checkbutton_sentinel2 = Checkbutton(main_window, text="Sentinel-2", variable=variable_sentinel2, onvalue=1, offvalue=0,
                                    font=custom_font)
checkbutton_sentinel2.grid(column=2, row=7, sticky=W)

# Maximum Cloud Cover Percentage
label_cloud_cover = Label(main_window, text="Max. Cloud Cover:", font=custom_font)
label_cloud_cover.grid(column=0, row=8, sticky=W)

textbox_cloud_cover = Entry(main_window, font=custom_font)
textbox_cloud_cover.grid(column=1, row=8, columnspan=2, sticky=W+E)
textbox_cloud_cover.bind("<Control-Key-a>", select_all)

# Query
def start_query():
    query_status.set('Processing query...')
    # Read input parameters from entry widgets
    global aoi
    [username, password, start_date, end_date, aoi, platform, max_cloud_cover] = entries.get(textbox_username, textbox_password,
                                                                            textbox_start_date, textbox_end_date,
                                                                            textbox_aoi, variable_sentinel1,
                                                                            variable_sentinel2, textbox_cloud_cover)
    # Delete already existing api reference and images
    global api, images
    if 'api' in globals():
        del api
    if 'images' in globals():
        del images
    # Query images by given input parameters
    [api, images] = query.query_images(username, password, start_date, end_date, aoi, platform, max_cloud_cover, query_status)

button_query = Tkinter.Button(main_window, text='Start Query', command=start_query, font=custom_font)
button_query.grid(column=1, row=9, sticky=W)

# Status bar of the query section
query_status = Tkinter.StringVar()
label_query_status = Label(main_window, textvariable=query_status, font=custom_font)
label_query_status.grid(column=1, row=10, sticky=W)

########################################################################################################################
# 3. Download
########################################################################################################################

label_download = Label(main_window, text="3. Download options", font=title_font)
label_download.grid(column=0, row=11, columnspan=2, sticky=W)

# Download path
label_download_path = Label(main_window, text="Download path:", font=custom_font)
label_download_path.grid(column=0, row=12, sticky=W)

textbox_download_path = Entry(main_window, font=custom_font)
textbox_download_path.grid(column=1, row=12, columnspan=3, sticky=W + E)
textbox_download_path.bind("<Control-Key-a>", select_all)

# File dialog to get the path where downloads should be stored
def get_download_path():
    global download_path
    download_path = tkFileDialog.askdirectory()
    textbox_download_path.insert(INSERT, download_path)

button_download_path = Tkinter.Button(main_window, text='Open directory', command=get_download_path)
button_download_path.grid(column=4, row=12, sticky=W+E)

# Product ID
label_product_id = Label(main_window, text="Product ID:", font=custom_font)
label_product_id.grid(column=0, row=13, sticky=W)

textbox_product_id = Entry(main_window, font=custom_font)
textbox_product_id.grid(column=1, row=13, columnspan=2, sticky=W + E)
textbox_product_id.bind("<Control-Key-a>", select_all)

# Download options

# Save Metadata
global variable_save_metadata
variable_save_metadata = IntVar()
checkbutton_save_metadata = Checkbutton(main_window, text="Save Metadata", variable=variable_save_metadata, onvalue=1, offvalue=0,
                                        font=custom_font)
checkbutton_save_metadata.grid(column=1, row=14, sticky=W)

# Plot Footprints
global variable_plot_footprints
variable_plot_footprints = IntVar()
checkbutton_plot_footprints = Checkbutton(main_window, text="Plot Footprints", variable=variable_plot_footprints, onvalue=1, offvalue=0,
                                          font=custom_font)
checkbutton_plot_footprints.grid(column=2, row=14, sticky=W)

# Download one test image
global variable_download_test_image
variable_download_test_image = IntVar()
checkbutton_download_test_image = Checkbutton(main_window, text="Download test image",
                                              variable=variable_download_test_image, onvalue=1, offvalue=0, font=custom_font)
checkbutton_download_test_image.grid(column=3, row=14, sticky=W)

# Download all queried images
global variable_download_all
variable_download_all = IntVar()
checkbutton_download_all = Checkbutton(main_window, text="Download all", variable=variable_download_all, onvalue=1, offvalue=0,
                                       font=custom_font)
checkbutton_download_all.grid(column=4, row=14, sticky=W)

# Status bar of the download section
download_status = Tkinter.StringVar()
label_download_status = Label(main_window, textvariable=download_status, font=custom_font)
label_download_status.grid(column=1, row=16, sticky=W)

# Download
def start_download():
    download_status.set('Processing download...')
    # get download path and download options from entry widgets
    [download_path, product_id, download_options] = entries.get(None, None, None, None, None, None, None, None,
                                                                textbox_download_path, textbox_product_id,
                                                                variable_save_metadata, variable_plot_footprints,
                                                                variable_download_test_image, variable_download_all)
    download.start(api, images, download_path, product_id , download_options, aoi, download_status)

button_download = Tkinter.Button(main_window, text='Start Download', command=start_download, font=custom_font)
button_download.grid(column=1, row=15, sticky=W+E)

########################################################################################################################
# 4. Preprocessing
########################################################################################################################

label_preprocessing = Label(main_window, text="4. Preprocessing", font=title_font)
label_preprocessing.grid(column=0, row=17, columnspan=2, sticky=W)

# Image path (of the to be processed images)
label_image_path = Label(main_window, text="Image path:", font=custom_font)
label_image_path.grid(column=0, row=18, sticky=W)

textbox_image_path = Entry(main_window, font=custom_font)
textbox_image_path.grid(column=1, row=18, columnspan=3, sticky=W+E)
textbox_image_path.bind("<Control-Key-a>", select_all)

def get_image_path():
    image_path = tkFileDialog.askdirectory()
    textbox_image_path.insert(INSERT, image_path)

button_image_path = Tkinter.Button(main_window, text='Open directory', command=get_image_path)
button_image_path.grid(column=4, row=18, sticky=W+E)

# Preprocessing options
# Checkbox Mosaick
global variable_mosaick
variable_mosaick = IntVar()
checkbutton_mosaick= Checkbutton(main_window, text="Mosaick", variable=variable_mosaick, onvalue=1, offvalue=0, font=custom_font)
checkbutton_mosaick.grid(column=1, row=19, sticky=W)

# Checkbox Subset
global variable_subset
variable_subset= IntVar()
checkbutton_subset= Checkbutton(main_window, text="Create subset", variable=variable_subset, onvalue=1, offvalue=0, font=custom_font)
checkbutton_subset.grid(column=2, row=19, sticky=W)

# Preprocessing
def start_preprocessing():
    preprocessing_status.set('Preprocessing...')
    [image_path,preprocessing_options] = entries.get(None, None, None, None, None, None, None, None, None, None, None,
                                                     None, None, None, textbox_image_path, variable_mosaick,
                                                     variable_subset)
    preprocessing.start(image_path, aoi, preprocessing_options)

button_preprocess = Tkinter.Button(main_window, text='Start Preprocessing', command=start_preprocessing,
                                   font=custom_font)
button_preprocess.grid(column=1, row=20, sticky=W+E)

preprocessing_status = Tkinter.StringVar()
label_preprocessing_status = Label(main_window, textvariable=preprocessing_status, font=custom_font)
label_preprocessing_status.grid(column=1, row=22, sticky=W)

# Clear all
button_clear_all= Tkinter.Button(main_window, text='Clear all', command=clear_all, font=custom_font)
button_clear_all.grid(column=2, row=20, sticky=W+E)

# Create configuration file
button_create_config = Tkinter.Button(main_window, text='Save configuration', command=save_configuration,
                                      font=custom_font)
button_create_config.grid(column=3, row=20, columnspan=2)

main_window.mainloop()