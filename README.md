# sendobox - Sentinel Download Toolbox

[Documentation sendobox.github.io](https://sendobox.github.io/sendobox/)

Sentinel Download ToolBox (SenDoBox) - A batch processing tool for downloading Sentinel satellite data

## About

sendobox is a tool for downloading a vast amount of Sentinel satellite data in an easy and structured way. 
With a specified area of intrest (aoi) and a starting and end date, all queried Sentinel images can be downloaded in one go. 
Some preprocessing functions for creating subsets and mosaic are also included. The programm can be operated with a graphical user interface 
or from the command line. All paramters for the query of the satellite data are stored in one singe input text file.

The software is licensed under the GNU General Public License. If you use this project for your research, please cite this accordingly.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

* First get all dependencies working.
* It is recommended to also install snappy, a link between python and SNAP (ESA Toolbox), for preprocessing the downloaded data. 
A installation guide can be found in the [Documentation sendobox.github.io](https://sendobox.github.io/sendobox/) und the installation section.

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

## Built With

* [python2.7](https://www.python.org/download/releases/2.7/) - sendobox is only compatible with python 2.7 right now
* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub

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


## Contributing

Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and should be submitted in the form of new issues and/or pull requests on GitHub.

## Authors

* **Buergmann Tatjana** - *Initial work* 
* **Stark Thomas** - *Initial work* - [github](https://github.com/stark-t)

* **Dr.-Ing. Michael Schmitt** - *Supervision*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

The sendobox software was written by Tatjana Buergmann and Thomas Stark under supervision of Michael Schmitt in the frame of a study project in photogrammetry and remote sensing at Technical University of Munich.

## License

The software is licensed under the GNU General Public License v3 or later. If you are interested in licensing the software for commercial purposes, without disclosing your modifications, please contact the authors.


## Acknowledgments

* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub
* [Andreas Baumann](http://forum.step.esa.int/users/abgbaumann/activity) - Adaption of the mosaic procedure
* Hat tip to anyone who's code was used


