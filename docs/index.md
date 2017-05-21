# sendobox - Sentinel Download Toolbox

[View on Github](https://github.com/sendobox/sendobox)

Sentinel Download ToolBox (SenDoBox) - A batch processing tool for downloading Sentinel satellite data

## About

sendobox is a tool for downloading a vast amount of Sentinel satellite data in an easy and structured way. 
With a specified area of intrest (aoi) and a starting and end date, all queried Sentinel images can be downloaded in one go. 
Some preprocessing functions for creating subsets and mosaic are also included. The programm can be operated with a graphical user interface 
or from the command line. All paramters for the query of the satellite data are stored in one singe input text file.

The software is licensed under the GNU General Public License. If you use this project for your research, please cite this accordingly.

## Table of Contents

* [Gettings Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
* [Guide and Example](#guide-and-example)
* [Frontend Development](#frontend-development)
  * [Graphical User Interface GUI](#graphical-user-interface-gui)
  * [Command Line Tool](#command-line-tool)
* [Backend Development](#backend-development)
  * [Access to ESA Datahub](#access-to-esa-datahub)
  * [Query for Image Acquisition](#query-for-image-acquisition)
  * [Download and Archiving](#download-and-archiving)
  * [Preprocessing](#preprocessing)
* [Appendix](#appendix)
  * [Contributing](#contributing)
  * [Authors](#authors)
  * [License](#license)
  * [Acknowledgments](#acknowledgments)



## Getting Started
[Table of Contents](#table-of-contents)

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

* First get all dependencies working [Requirements](#requirements).
* Sendobox is build with python2.7. For guaranteed working order it is adviced to also use python 2.7. 
* It is recommended to also install snappy, a link between python and SNAP (ESA Toolbox), for preprocessing the downloaded data. 
A installation guide can be found in the [Installation](#installation) section.

* Specify your area of interest (aoi) from [geojson](http://geojson.io/#map=2/20.0/0.0) and store it in your sendobox directory.
* Configure your parameter textfile:

| Line  | Parameter |
| ------------- | ------------- |
| 1  | username  |
| 2  | password  |
| 3  | start date dd.mm.yyyy  |
| 4  | end date dd.mm.yyyy  |
| 5  | area of intrest  |
| 6  | platform  |
| 7  | maximum cloud coverage  |
| 8  | download path  |
| 9  | image id  |
| 10  | download options  |
| 11  | preprocessing path  |
| 12  | preprocessing options  |

An example can be found in the turorial folder of sendobox.

### Dependencies

#### Requirements

These packages can be installed speratly or with the requirements.txt file.

```
pip install -r requirements.txt
```

List all dependencies:

* [matplotlib](https://matplotlib.org/users/installing.html)
* [snappy](https://senbox.atlassian.net/wiki/display/SNAP/Configure+Python+to+use+the+SNAP-Python+%28snappy%29+interface)
* [geojson](https://pypi.python.org/pypi/geojson#installation)
* [shapely](https://pypi.python.org/pypi/Shapely)
* [sentinelsat](https://github.com/ibamacsr/sentinelsat)


#### Built With:

* [python2.7](https://www.python.org/download/releases/2.7/) - sendobox is only compatible with python 2.7 right now
* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub

### Installation

* Installation Repository

Download the zip folder or clone repository.

```
$ git clone https://github.com/sendobox/sendobox.git
```

Check if all dependencies are installed and launch a python interpreter or a python console.

1. Console:
```
$ cd <sendobox-clone-dir>
```
```
$ python console.py
```
```
$ Please type the path of your .txt configuration file: <sendobox-input.txt-dir>
```
2. GUI:
```
$ cd <sendobox-clone-dir>
```
```
$ python gui.py
```
Load or create your own `input.txt` file.


* Installation SNAP-Python

The snappy.py installation is only required if you want to take advantage of the preprocessing features for creating a 
subset or a mosaic. Following is a step by step series that tell you how to get a development env running. SNAP-python
is a link between the ESA SNAP Toolbox and python, which sendobox uses to create subsets and mosaics.

Configure Python to use the SNAP-Python (snappy) interface:

* The easiest way to configure your Python installation for the usage SNAP-Python (snappy) interface is to do it 
during the installation of SNAP. Within the installer it you can simply activate a checkbox and select the path to the python executable.

* If you already have SNAP installed and want to add the SNAP-python interface, you have to generate the Python 
module snappy configured for the current SNAP installation and your Python interpreter <python-exe> into the .snap/snap-python
directory of the user home directory.

1. In your terminal go to the bin directory of SNAP
```
$ cd <snap-install-dir>/bin
```
Unix:
```
$ ./snappy-conf <python-exe>
```
Windows:
```
$ snappy-conf <python-exe> 
```

2. Test if snappy installation was succesful
```
$ cd <snappy-dir>
$ <python-exe>     (start your Python interpreter)
```
Then try the following code:
```
from snappy import ProductIO
p = ProductIO.readProduct('snappy/testdata/MER_FRS_L1B_SUBSET.dim')
list(p.getBandNames())
```

3. Configure python-snappy path

To effectively use the SNAP Python API from Python, the  snappy module must be detectable by your Python interpreter. There are a number of ways to achieve this. To make snappy permanently accessible, you could install it into your Python installation. On the command line (shell, terminal window on Unixes, cmd on Windows), type
```
$ cd <snappy-dir>/snappy
$ <python-exe> setup.py install
```

If you encounter any problems with this approach, you can also try to copy the <snappy-dir>/snappy directory directly into the site-packages directory of your Python installation. Secondly, you could also temporarily or permanently set your PYTHONPATH environment variable:

export PYTHONPATH=$PYTHONPATH:<snappy-dir>   (on Unix OS)
set PYTHONPATH=%PYTHONPATH%;<snappy-dir>    (on Windows OS)

Finally, you could also append <snappy-dir> to the sys.path variable in your Python code before importing snappy:
```
import sys
sys.path.append('<snappy-dir>') # or sys.path.insert(1, '<snappy-dir>')
import snappy
```


## Guide and Example
[Table of Contents](#table-of-contents)

The tutorial folder provides a working paramter file and geojson file to test the software via the gui or from the command line.

**Graphical User Interface - GUI**

The gui gives an option to load and save a paramter file and the following download options: 

For saving the metadata for both Sentinel 1 and Sentinel 2 data in two seperate .csv files:
```
Save Metadata
```

For plotting the footprints of the queried data:
```
Plot Footprints
``` 

Downloading the first image of the queried data:
```
Download test image
``` 

Download all queried data:
```
Download all
``` 

The preprocesisng options are:

Create a mosaic with two images from fitting orbits:
```mosaic``` 

Create a subset for the area of intrest: 
```subset``` 

**Command Line**

Launch the `console.py` file and the command line tool will ask for the path to your input.txt parameter file. Once
specified the download and preprocessing will start automatically.



## Frontend Development
[Table of Contents](#table-of-contents)
### Graphical User Interface GUI

The Graphical User Interface (GUI) was implemented using the Python package Tkinter. All labels,
buttons, checkboxes and textboxes were arranged in a grid layout.

The Interface was split into 4 parts:
* Login
* Query
* Download
* Preprocessing

For every part, there is a status bar where status and error messages are shown. After all entries
have been made, there is an opportunity to save them in a configuration file (.txt) in order to reuse
them for another query or download. Subsequently, the configuration can be reloaded and all ent-
ries are automatically filled out. The configuration file can also be created manually using a specific
convention (see table 3.1). The GUI python program imports python modules for the query, download and preprocessing 
parts as well as a module for reading and writing entries and a module for
loading and saving the configuration.

| Line  | Parameter |
| ------------- | ------------- |
| 1  | username  |
| 2  | password  |
| 3  | start date dd.mm.yyyy  |
| 4  | end date dd.mm.yyyy  |
| 5  | area of intrest  |
| 6  | platform  |
| 7  | maximum cloud coverage  |
| 8  | download path  |
| 9  | image id  |
| 10  | download options  |
| 11  | preprocessing path  |
| 12  | preprocessing options  |

### Command Line Tool

Alternatively, there is a python program for using the same functions as implemented for the GUI
using a simple console input for the path of the configuration file. Afterwards download and prepro-
cessing starts automatically.

It should be noted that the command line tool is due for some changes, to make it more stable as soon as possible.

## Backend Development
[Table of Contents](#table-of-contents)

### Access to ESA Datahub

In order to use the functionalities of the Sentinel Scientific Data Hub a registration on their webpage
is necessary: [scihub](https://scihub.copernicus.eu/dhus/). Afterwards, login dates (username and password) 
can be used for the download toolbox. In this part only username and password inputs are requested. 
Input errors are checked when running the query and an error message will be shown in the query status bar.

### Query for Image Acquisition

The next step is querying images using a certain area of interest and time period. First the Sentinel
API needs to be accessed using the queried login dates. Since the API Hub is dedicated to users
of scripting interfaces, this is the preferred API to use. If the API Hub cannot be accessed the Open
Hub is used instead. For querying images an area of interest needs to be selected. So far, this is
realized using a .geojson file. On the webpage geojson.io a geojson file can intuitively be created
by dragging out a rectangle.


Start and end dates are entered in the form of dd.mm.yyyy. Furthermore, a specific platform can
be entered e.g. Sentinel-1 or Sentinel-2. If none or both checkboxes are checked, images of both platforms are queried. 
Optionally the maximum cloud cover can be entered as a percentage e.g.
30%. 

The number of images found by the query is shown in the status bar. For further information
about the images (footprints and metadata) the download section can be used.

### Download and Archiving

Several options are given for download:
* Download metadata
* Plot Footprints
* Download a single image using its product id
* Download all images from the query

Downloaded images and metadata are saved in a certain folder structure. Two folders are created:
One for Sentinel-1 and for Sentinel-2 data.

**Save relevant Metadata**

For each folder (or platform, respectively) a metadata file (.csv) is created. For Sentinel-2 data the
following parameters are saved:
* ID (starting from 1)
* Image ID
* Mode
* Product Type
* Orbit Direction
* Sensing Date
* Product ID
For Sentinel-1 data additionally the Polarization is written in the metadata file.

**Visualizing queried Footprints**

For each queried image a footprint can be plotted to see if it alligns with the selected area of interest. The query for
Sentinel data only uses an intersection of the aoi and the footprint for its queried data and not if the aoi is fully contained 
in the footprint.

Using `matplotlib` a figure is plotted to show all images with its ID and the area of interest.

**Download queried Sentinel Data**

The queried images are downloaded into an archive. Depending on the platform a folder is created that stores all downloaded
images.

`api.download(properties[i]['product_id'], output_path+'\Sentinel-1', check_existing=True)`

To check if the download is complete, the included `check_existing` checksum md5 UUID comparisson is done to ensure the downloaded file is not corrupt and already downloaded.
If True and a fully downloaded file with the same name exists on the disk, verify its integrity using its MD5 checksum. Re-download in case of non-matching checksums.

In this case we use the `SubsetOp` and the `MosaicOp` auf SNAP to process the data in the archive.

### Preprocessing

**SNAP-Python Interface `snappy.py`**

The preprocessing is handled by ESA's SNAP toolbox via the python interface `snappy.py`. All operators from SNAP are 
available to use via the interface in python.

**Resampling Sentinel 2 Data**

The bands of Sentinel 2 come in three different ground resolutions of 10m, 20m and 60m. To create a subset for all 12 Bands
a resample method has to be done. In the case of sendobox all bands are resampled to 10m with the nearest neighbor operator.

**Polarisation Sentinel 1 Data**

For Sentinel 1 data the polarization has to be accounted for before one can create a subset. Right now only HH polarized data works since that
is the most common polarization. That should change with the next updates.

**Creating a subset for the aoi** 

The geojson file from the parameter file is used to create the subset. The subset is written into the directory as its original file as
a geotiff file.

**Mosaic for two imagaes**

The mosaicing is using two images from the archive directory to create a mosaic of the area of intrest if not all of the image is
contained in the aoi.

The mosaic procedure is using two 

## Appendix
[Table of Contents](#table-of-contents)

### Whishlist

In future updates we want to adress the following improvements, problems and bugs:

* Update the `console.py` to be more functional and add a help argument.
* Improve the documentation with html elements, pictures and more in depth analysis including code commentary.
* Work on the preprocessing stabillity.
  * Subset for all polarizations.
  * Choose from all available resample options.
  * Make output format available in the parameter file.
  * Mosaic for all 12 Bands.
* Only download datasets contained in the area of intrest and not intersecting the aoi.
* Rewrite the code into objective oriented programming using clases in a seperate oop branch.


### Contributing

Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and should be submitted in the form of new issues and/or pull requests on GitHub.

### Authors

* **Buergmann Tatjana** - *Initial work* 
* **Stark Thomas** - *Initial work* - [github profile](https://github.com/stark-t)

* **Dr. Michael Schmitt** - *Supervision*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

The sendobox software was written by Tatjana Buergmann and Thomas Stark under supervision of Michael Schmitt in the frame of a study project in photogrammetry and remote sensing at Technical University of Munich.

### License

The software is licensed under the GNU General Public License v3 or later. If you are interested in licensing the software for commercial purposes, without disclosing your modifications, please contact the authors.


### Acknowledgments

* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub
* [Andreas Baumann](http://forum.step.esa.int/users/abgbaumann/activity) - Adaption of the mosaic procedure
* Hat tip to anyone who's code was used


