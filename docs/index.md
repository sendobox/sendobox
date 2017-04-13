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
  * [Access to ESA Datahub](#)
  * [Query for Image Acquisition](#)
  * [Download and Archiving](#)
  * [Preprocessing](#)
* [Appendix](#appendix)
  * [Contributing](#contributing)
  * [Authors](#authors)
  * [License](#license)
  * [Acknowledgments](#acknowledgments)



## Getting Started
[Table of Contents](#table-of-contents)

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

* First get all dependencies working [Requirements](#requirements).
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

```
matplotlib
snappy
geojson
shapely
sentinelsat
```

#### Built With:

* [python2.7](https://www.python.org/download/releases/2.7/) - sendobox is only compatible with python 2.7 right now
* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub

### Installation

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

1. GUI

The gui gives an option to load and save a paramter file. Download options are 
![GUI](/images/GUI.png)


2. Command Line


## Frontend Development
[Table of Contents](#table-of-contents)
### Graphical User Interface GUI

### Command Line Tool

## Backend Development
[Table of Contents](#table-of-contents)
## Appendix
[Table of Contents](#table-of-contents)

### Contributing

Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and should be submitted in the form of new issues and/or pull requests on GitHub.

### Authors

* **Buergmann Tatjana** - *Initial work* 
* **Stark Thomas** - *Initial work* - [github](https://github.com/stark-t)

* **Dr.-Ing. Michael Schmitt** - *Supervision*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

The sendobox software was written by Tatjana Buergmann and Thomas Stark under supervision of Michael Schmitt in the frame of a study project in photogrammetry and remote sensing at Technical University of Munich.

### License

The software is licensed under the GNU General Public License v3 or later. If you are interested in licensing the software for commercial purposes, without disclosing your modifications, please contact the authors.


### Acknowledgments

* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub
* [Andreas Baumann](http://forum.step.esa.int/users/abgbaumann/activity) - Adaption of the mosaic procedure
* Hat tip to anyone who's code was used


