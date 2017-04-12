# sendobox - Sentinel Download Toolbox

[https://sendobox.github.io/sendobox/](https://sendobox.github.io/sendobox/)

Sentinel Download ToolBox (SenDoBox) - A batch processing tool for downloading Sentinel satellite data

## About

sendobox is a tool for downloading a vast amount of Sentinel satellite data in an easy and structured way. With a specified area of intrest (aoi) and a starting and end date, all queried Sentinel images can be downloaded in one go. Some preprocessing functions for creating subsets and mosaic are also included.

The software is licensed under the GNU General Public License. If you use this project for your research, please cite this accordingly.

## [create an anchor](#anchors-in-markdown)

test

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

* First get all dependencies working.
* It is recommended to also install snappy, a link between python and SNAP (ESA Toolbox), for preprocessing the downloaded data.

* Area of interest (aoi) from [geojson](http://geojson.io/#map=2/20.0/0.0)
* Configure your parameter textfile:

```
1 User
2 Password
...
```

### Dependencies

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

### Installing

A step by step series of examples that tell you have to get a development env running. 

Installing snappy

```
Link to readme install file?
```

## Guide & example

```
GUI
```

```
console
```



## Built With

* [python2.7](https://www.python.org/download/releases/2.7/) - The framework used
* [sentinelsat](https://github.com/ibamacsr/sentinelsat) - Access to the API of Copernicus Data Hub

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

