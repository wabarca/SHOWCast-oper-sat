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
__author__ = "Diego Souza"
__copyright__ = "Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL"
__credits__ = ["Diego Souza"]
__license__ = "GPL"
__version__ = "2.4.0"
__maintainer__ = "Diego Souza"
__email__ = "diego.souza@inpe.br"
__status__ = "Production"
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Required modules
#--------------------------------
#to run in a pure text terminal:
import matplotlib
matplotlib.use('Agg')
#--------------------------------
import pygrib                                                # Provides a high-level interface to the ECWMF ECCODES C library for reading GRIB files
from datetime import datetime, timedelta                     # Library to convert julian day to dd-mm-yyyy
import time as t                                             # Time access and conversion
import sys                                                   # Import the "system specific parameters and functions" module
import os                                                    # Miscellaneous operating system interfaces
from os.path import dirname, abspath                         # Return a normalized absolutized version of the pathname path
from html_update import update                               # Update the HTML animation
import warnings                                              # Warning control
warnings.filterwarnings("ignore")
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# Start the time counter
print('Script started.')
start = t.time()

# SHOWCast directory:
main_dir = dirname(dirname(abspath(__file__)))

# For logging purposes
print(sys.argv[1])
path = (sys.argv[1])[:-16]

# If it is for South Americas
if ('d6.gif' in path):
    print("South America")

else: # If it is for Caribbean
    print("Caribbean")
    print(path)
    path1 = path.replace('crb3','crb1')
    print(path1)
    path2 = path.replace('crb3','crb2')
    print(path2)
    path3 = path
    print(path3)

    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------

    # Product name
    satellite = "IDK"
    product   = "CRWQPF_SEC"

    # Create the satellite output directory if it doesn't exist
    out_dir = (sys.argv[7]) + satellite
    if not os.path.exists(out_dir):
       os.mkdir(out_dir)

    # Create the product output directory if it doesn't exist
    out_dir = (sys.argv[7]) + satellite + '//' + product + '//'
    if not os.path.exists(out_dir):
       os.mkdir(out_dir)

    #------------------------------------------------------------------------------------------------------

    # Create the satellite output directory if it doesn't exist
    out_dir_html = main_dir + '//HTML//Output//' + satellite
    if not os.path.exists(out_dir_html):
       os.mkdir(out_dir_html)

    # Create the product output directory if it doesn't exist
    out_dir_html = main_dir + '//HTML//Output//' + satellite + '//' + product + '//'
    if not os.path.exists(out_dir_html):
       os.mkdir(out_dir_html)

    #------------------------------------------------------------------------------------------------------

    # Create the satellite output directory if it doesn't exist
    out_dir_quicklooks = main_dir + '//HTML//Output//QuickLooks//'
    if not os.path.exists(out_dir_quicklooks):
       os.mkdir(out_dir_quicklooks)

    #------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------

    from shutil import copyfile
    from PIL.WebPImagePlugin import Image

    copyfile(path1, out_dir + 'crb1.gif')
    copyfile(path2, out_dir + 'crb2.gif')
    copyfile(path3, out_dir + 'crb3.gif')

    copyfile(path1, out_dir_html + 'crb1.gif')
    copyfile(path2, out_dir_html + 'crb2.gif')
    copyfile(path3, out_dir_html + 'crb3.gif')

    copyfile(path1, out_dir_quicklooks + 'crb1_quicklook.png')
    copyfile(path2, out_dir_quicklooks + 'crb2_quicklook.png')
    copyfile(path3, out_dir_quicklooks + 'crb3_quicklook.png')

    # Convert to webp
    im = Image.open(out_dir + 'crb1.gif')
    im.save(out_dir + 'crb1.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir + 'crb2.gif')
    im.save(out_dir + 'crb2.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir + 'crb3.gif')
    im.save(out_dir + 'crb3.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_html + 'crb1.gif')
    im.save(out_dir_html + 'crb1.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_html + 'crb2.gif')
    im.save(out_dir_html + 'crb2.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_html + 'crb3.gif')
    im.save(out_dir_html + 'crb3.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_quicklooks + 'crb1_quicklook.png')
    im.save(out_dir_quicklooks + 'crb1_quicklook.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_quicklooks + 'crb2_quicklook.png')
    im.save(out_dir_quicklooks + 'crb2_quicklook.webp', format = "WebP", lossless = True)
    im.close()

    # Convert to webp
    im = Image.open(out_dir_quicklooks + 'crb3_quicklook.png')
    im.save(out_dir_quicklooks + 'crb3_quicklook.webp', format = "WebP", lossless = True)
    im.close()

    os.remove(out_dir + 'crb1.gif')
    os.remove(out_dir + 'crb2.gif')
    os.remove(out_dir + 'crb3.gif')

    os.remove(out_dir_html + 'crb1.gif')
    os.remove(out_dir_html + 'crb2.gif')
    os.remove(out_dir_html + 'crb3.gif')

    os.remove(out_dir_quicklooks + 'crb1_quicklook.png')
    os.remove(out_dir_quicklooks + 'crb2_quicklook.png')
    os.remove(out_dir_quicklooks + 'crb3_quicklook.png')


#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# Put the processed file on the log
import datetime # Basic Date and Time types
import pathlib  # Object-oriented filesystem paths
# Get the file modification time
mtime = datetime.datetime.fromtimestamp(pathlib.Path(path).stat().st_mtime).strftime('%Y%m%d%H%M%S')
# Write to the log
with open(main_dir + '//Logs//gnc_log_' + str(datetime.datetime.now())[0:10] + '.txt', 'a') as log:
    log.write(str(datetime.datetime.now()))
    log.write('\n')
    log.write(path + '_c' + mtime + '\n')
    log.write('\n')

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# Total processing time
print('Total processing time:', round((t.time() - start),2), 'seconds.')
