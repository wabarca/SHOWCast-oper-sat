#######################################################################################################
# LICENSE
# Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
# General Public License as published by the Free Software Foundation, either version 3 of the License, 
# or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
# Public License for more details.
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see http://www.gnu.org/licenses/.
#######################################################################################################
__author__ = "William Abarca"
__copyright__ = "Copyright (C) 2023 - MARN - EL SALVADOR"
__credits__ = ["William Abarca"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "William Abarca"
__email__ = "wabarca@ambiente.gob.sv"
__status__ = "Production"
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Required modules
#--------------------------------
#to run in a pure text terminal:
# import matplotlib
# matplotlib.use('Agg')
#--------------------------------
# import pygrib                                                # Provides a high-level interface to the ECWMF ECCODES C library for reading GRIB files
# from datetime import datetime, timedelta                     # Library to convert julian day to dd-mm-yyyy
# from matplotlib.colors import LinearSegmentedColormap        # Linear interpolation for color maps
# from mpl_toolkits.axes_grid1.inset_locator import inset_axes # Add a child inset axes to this existing axes.
# import matplotlib.colors                                     # Matplotlib colors
# import matplotlib.pyplot as plt                              # Plotting library
# import numpy as np                                           # Scientific computing with Python
# import cartopy, cartopy.crs as ccrs                          # Plot maps
# import cartopy.io.shapereader as shpreader                   # Import shapefiles
import time as t                                             # Time access and conversion
import sys                                                   # Import the "system specific parameters and functions" module
# import math                                                  # Import math
import glob, os                                                    # Miscellaneous operating system interfaces
from os.path import dirname, abspath                         # Return a normalized absolutized version of the pathname path 
# from html_update import update                               # Update the HTML animation 
import warnings                                              # Warning control
warnings.filterwarnings("ignore")
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Start the time counter
print('Script started.')
start = t.time()  

# For logging purposes
path = (sys.argv[1])[:-16]

# Read the sector
sector = sys.argv[9]

# Extracting directory
gfs_data = os.path.dirname(path)
for files in glob.glob(gfs_data+"//*"):
    os.remove(files)

# Total processing time
print('Total processing time:', round((t.time() - start),2), 'seconds.') 
