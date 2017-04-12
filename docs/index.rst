COLMAP
======

.. figure:: images/sparse.png
    :alt: Sparse reconstruction of central Rome.
    :figclass: align-center

    Sparse model of central Rome using 21K photos produced by COLMAP's SfM
    pipeline.

.. figure:: images/dense.png
    :alt: Dense reconstruction of landmarks.
    :figclass: align-center

    Dense models of several landmarks produced by COLMAP's MVS pipeline.


About
-----

COLMAP is a general-purpose Structure-from-Motion (SfM) and Multi-View Stereo
(MVS) pipeline with a graphical and command-line interface. It offers a wide
range of features for reconstruction of ordered and unordered image collections.
The software is licensed under the GNU General Public License. If you use this
project for your research, please cite::

    @inproceedings{schoenberger2016sfm,
        author = {Sch\"{o}nberger, Johannes Lutz and Frahm, Jan-Michael},
        title = {Structure-from-Motion Revisited},
        booktitle={IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
        year={2016},
    }

    @inproceedings{schoenberger2016mvs,
        author = {Sch\"{o}nberger, Johannes Lutz and Zheng, Enliang and Pollefeys, Marc and Frahm, Jan-Michael},
        title = {Pixelwise View Selection for Unstructured Multi-View Stereo},
        booktitle={European Conference on Computer Vision (ECCV)},
        year={2016},
    }

The latest source code is available at `GitHub
<https://github.com/colmap/colmap>`_. COLMAP builds on top of existing works and
when using specific algorithms within COLMAP, please also cite the original
authors, as specified in the source code.


Download
--------

Executables and other resources can be downloaded from
http://people.inf.ethz.ch/jschoenb/colmap/.


Getting Started
---------------

1. Download the `pre-built binaries
   <http://people.inf.ethz.ch/jschoenb/colmap/>`_ or build the library manually
   (see :ref:`Installation <installation>`).
2. Download one of the provided datasets (see :ref:`Datasets <datasets>`)
   or use your own images.
3. Watch the short introductory video at
   `YouTube <https://www.youtube.com/watch?v=P-EC0DzeVEU>`_ or read the
   :ref:`Tutorial <tutorial>` for more details.


Support
-------

Please, use the `Google Group <https://groups.google.com/forum/#!forum/colmap>`_
(colmap@googlegroups.com) for questions and the `GitHub issue tracker
<https://github.com/colmap/colmap>`_ for bug reports, feature
requests/additions, etc.


Contents
--------

.. toctree::
   :maxdepth: 2

   install
   tutorial
   database
   cameras
   format
   datasets
   gui
   cli
   faq
   contribution
   license
   bibliography


Acknowledgments
---------------

The library was written by `Johannes L. Schönberger
<http://people.inf.ethz.ch/jschoenb/>`_. Funding was provided by his PhD advisors
`Jan-Michael Frahm <http://frahm.web.unc.edu/>`_ and
`Marc Pollefeys <https://www.inf.ethz.ch/personal/marc.pollefeys/>`_.
