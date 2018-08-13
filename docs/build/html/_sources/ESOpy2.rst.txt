.. ESO_chile_python_team documentation master file, created by
   sphinx-quickstart on Mon Aug 13 12:21:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _ESOpy2:


ESOpy2.0
--------
--------
This page summarize the ESOpy2.0 orginaize in early 2018 at ESO chile.

Rationale
^^^^^^^^^
* **Why?**

The python programming language is becoming one of the most used language in the world. It is used by one of the greatest companies like Google, Yahoo, IBM, Nokia, etc. In science as well it is developping fast. THE LHC is using python, NASA is using python (JWST pipelines are written primarily in python), ESO and the VLT are becoming python-friendly and the E-ELT will make great use of Python. In this spirit, the python team decided to organize a second edition of the Python Boot camp that had a great success a year ago. The ESOpy2.0 aims at providing a (non-exhaustive) overview of the python language and its use in science and operations.

* **What?** The V2.0 of the camp will span 3 days: 

    * The first day is aimed at beginners only (and therefore optional) After a brief introduction of the language a serie of activities will be proposed to the participants to familiarize with the very basix of the language: Libraries, datatypes, data collections, FITS file handling, basic plotting, scripting, functions... No requirements are needed, except having python 3.5+ installed on your laptop.
    * The second and third day are aimed at everybody willing to improve her/his python knowledge. Each day will be split into two parts. In the morning few lectures about librairies/topics will be given with direct hands-on exercices. The afternoons will be dedicated to small projects that will be developed by groups of trainees and presented at the end of the camp. Both science-oriented and Operation-oriented exercices and projects will be proposed


* **When and Where**: ESOpy will take place in Vitacura on the 8-9-10 of January.


Team
^^^^
R. Thomas (Chair), B. Dias, E. Sedaghati, F. Vogt, I. Munoz, A. Razza & J. Bolmer

Program
^^^^^^^


* Day 01 Morning session (9h30 --> 13h,  Material: :download:`ESOpy_1st_day.tar.gz <./files/ESOpy_1st_day.tar.gz>`)

    * 09:30 - 10:00: Introduction (R. Thomas) T
    * 10:00 - 11:00: Python as an object oriented language (E. Sedaghati) E
    * 11:30 - 13:00: Python language I (I. Munoz) E


* Day 01 Afternoon session (14h-->17h40)
  
    * 14:00 - 15:00: Python language II (I. Munoz) E
    * 15:00 - 16:00: Interacting with external file (A. Razza) E
    * 16:30 - 17:00: Terminal interface (or how to leave your code in peace) (R. Thomas) E
    * 17:00 - 17:40: Basic matplotlib manipulation (R. Thomas) E


* Day 02 Morning session (9h --> 13h, Material: :download:`ESOpy_2nd_day.tar.gz <./files/ESOpy_2nd_day.tar.gz>`)

    * 09:00 - 09:15: Introduction (B. Dias) T
    * 09:15 - 09:45: Functional programming (I. Munoz) T
    * 09:45 - 11:00: Astropy (A. Razza) E
    * 11:30 - 12:00: Paranal Python Library (I. Munoz) T
    * 12:00 - 13:00: Aplpy and advanced plotting for Astronomy (F. Voigt) E


* Day 02 Afternoon session (14h-->17h30)

    * 14:00 - 16:00: Projects
    * 16:30 - 17:30: Projects


* Day 03 Morning session (9h30 --> 13h, Material: :download:`ESOpy_3rd_day.tar.gz <./files/ESOpy_3rd_day.tar.gz>`)

    * 09:00 - 11:00: Scientific coding with Numpy and Scipy (R. Thomas) E
    * 11:30 - 12:15: Distributing python packages/github (F. Voigt) T
    * 12:15 - 13:00: An example of advanced computing package: PyMc (J. Bolmer) E


* Day 03 Afternoon session (14h-->17h30)
  
    * 14:00 - 16:00: Projects
    * 16:30 - 17:00: Projects
    * 17:00 - 17:30: Short presentation (5min) with a summary of each project



Projects
^^^^^^^^

The Afternoons of the 2nd and 3rd day were dedicated to the development of small projects. Each project was proposed and taken care of by a tutor. Six projects were proposed:

* **P1: Where do we look at?:** This projects aims at creating a prototype of live display of ESO telescope during the night.
* **P2: Error Database:** The idea is to create an error database for Paranal. This would link error messages from the log of different systems to the troubleshooting. This program would fetch an error from a log file and display informations about this error (#of occurence, trouble shooting, last occurence...).
* **P3: Finding charts:** This project aims at creating a program that computes automatically finding charts.
* **P4: IDL2PYTHON:** The idea here is to convert idl programs to python codes.
* **P5: Visibility plots:** It aims at creating a program that display the visibility of a celestial object given the position on earth, the object coordinates and the time of observation.
* **P6: QC0 for FORS2 in imaging mode:** The aim is to create a program that computes the QC0 parameters of the imaging mode of FORS2.

A detail presentation of the project can be found here:  Material: :download:`ESOpy2_projects.tar.gz <./files/ESOpy2_projects.tar.gz>`

