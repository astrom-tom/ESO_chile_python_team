.. ESO_chile_python_team documentation master file, created by
   sphinx-quickstart on Mon Aug 13 12:21:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _ESOpy3:


ESOpy3.0
--------
--------
This is the webpage of ESOpy3.0 organized in April 2019 at ESO chile.

Rationale
^^^^^^^^^

WHY?
====
The Python programming language is one of the most used programming language in the world. It is used on a daily basis by one of the biggest companies in the world like Google, Yahoo, IBM, Nokia, etc… In the science world the use of python is growing fast as well. The LHC is using python, NASA is using python (JWST pipelines are written primarily in python), ESO is becoming python-friendly (with SciOpsPy) and the E-ELT will make great use of it.
In this spirit, the python team decided to organize a third edition of the Python Boot camp that had a great success a year ago. The ESOpy v3.0 aims at providing a (non-exhaustive) overview of the python language and its use in science and operations.
 
WHAT?
=====
The V3.0 of the camp will take the same skeleton as last year and will last 3 days:
The first day is aimed at beginners only. After a brief introduction of the language a serie of lectures and activities will be proposed to the participants in order to familiarize with the very basics of the language: Libraries, datatypes, data collections, FITS file handling, basic plotting, scripting, functions…. No requirements are needed, except having python (3.7) installed on your laptop.
 
The second and third day are aimed at everybody willing to improve her/his python knowledge. Each day will be split into two parts. In the morning few lectures about libraries/topic will be given with direct hands-on exercises. The afternoons will be dedicated to small projects that will be developed by groups of trainees and presented at the end of the camp. Both science-oriented and Paranal-operation-oriented projects will be proposed.
 
WHEN AND WHERE?
===============
ESOpy3.0 will take place at ESO-Vitacura on the 15, 16 and 17 of April.


Team
====
R. Thomas (Chair), E. Sedaghati, F. Vogt, I. Munoz, A. Razza

Material
========

You can find here the python installation document :download:`here <./files/ESOpy3_0_instal_v2.pdf>`. Please come on the workshop with everything installed. We will not have time to spend time installing >30 python environment.

Note: It seems that the dfitspy installation on Mac poses some problem with the libmagic library. The trick is to install the python-magic-bin package from pip: pip install python-magic-bin


Program
=======


* Day 01 Morning session (9h30 --> 13h,  Material: **SOON**
  
    * 09:30 - 10:00: Introduction (Romain) :download:`(Material) <./files/ESOpy3_Introduction_RThomas.pdf>`
    * 10:00 - 11:00: Python language  Basics I  (Ivan) :download:`(Material) <./files/Ivan_Basics.tar.gz>`
    * 11:30 - 13:00: Python language  Basics II (Ivan)

* Day 01 Afternoon session (14h-->17h40)
  
    * 14:00 - 15:00: Python language Basics III (Ivan)
    * 15:00 - 16:00: Reading/writing ascii files in python (Romain) :download:`(Material) <./files/ESOpy3_Reading_writing_Romain.ipynb>`
    * 16:20 - 17:15: Functions in Python (Elyar)  :download:`(Material) <./files/ESOpy3_Functions_Elyar.ipynb>`
    * 17:15 - 18:00: Numpy: Introduction to the numpy array (Romain) :download:`(Material) <./files/ESEpy3_Numpy_Romain.ipynb>`

* Day 02 Morning session (9h --> 13h, Material: **SOON**

  Images for the two first classes: https://drive.google.com/open?id=1GyZ2VszfpD02JcdteAySOvAl0zYb-xMG
        
    * 09:30 - 10:15: Fits file handling with Python (Alessandro)  :download:`(Material) <./files/ESOpy3_FitsFiles_Alessandro.ipynb>`
    * 10:15 - 11:15: Classes in Python: object-oriented programming (Elyar) :download:`(Material) <./files/Classes.ipynb>`
    * 11:30 - 12:15: Testing (Ivan) :download:`(Material) <./files/testing.tar.gz>`

    * 12:15 - 13:00: Command line interfaces (CLI) in python (Romain) :download:`(Material) <./files/ESO_parsing.tar.gz>`

* Day 02 Afternoon session (14h-->17h30)

    * 14:00 - 16:00: Projects
    * 16:30 - 17:30: Projects

* Day 03 Morning session (9h30 --> 13h, Material: **SOON**)

    * 09:00 - 10:15: Scientific coding with Scipy (Romain)
    * 10:15 - 11:15: Astro-coordinates and database query in Python (Frederic)
    * 11:30 - 12:15: Advanced Matplotlib manipulations (Frederic)
    * 12:15 - 13:00: How to code for Paranal (Romain) :download:`(Material) <./files/Paranal_modul.tar.gz>`


* Day 03 Afternoon session (14h-->17h30)
  
    * 14:00 - 16:00: Projects
    * 16:30 - 17:00: Projects
    * 17:00 - 17:30: Short presentation (5min) with a summary of each project


Projects
========

The description of all the project can be found here: :download:`(Material) <./files/ALL.pdf>`

Please have a look and pick up your project in the following google form: https://docs.google.com/forms/d/e/1FAIpQLSeSmTx5w0e6nIM4be9puvH3hjRB7KaehzMj8jr9AW9JHt5vVw/viewform?usp=sf_link 


* **P1: dfits|fitsort**: transforming the classic dfits|fitsort into python (CLI + fits file search) [Romain] :download:`(Material) <./files/dfits.tar.gz>`

* **P2: catmatch**: Matching catalogs in python (CLI, numpy, standard library) [Romain] :download:`(Material) <./files/catmatch.tar.gz>`


* **P3: PSF building** [Alessandro] :download:`(Material) <./files/PSF_project.pdf>`
   

* **P4: Tapping into ADS with python** [Frederic] :download:`(Material) <./files/astroquery_project_info.pdf>`
  
* **P5: specstack**: create a program that stack spectra of galaxies (Numpy, CLI, matplotlib) [Romain] :download:`(Material) <./files/Spectral_stack.tar.gz>`

* **P6: Visibility plots** [Elyar]: Visibility of a celestial object given the position on earth, the object coordinates and the time of observation. :download:`(Material) <./files/VIS_plot_project.pdf>`

* **P7: All-sky images manipulation** [Julien]: star registration, photometry and archive query :download:`(Material) <./files/APICAM_photometry_python_project.pdf>`

