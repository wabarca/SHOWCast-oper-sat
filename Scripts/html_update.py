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
import glob                           # Unix style pathname pattern expansion
import os                             # Miscellaneous operating system interfaces
from os.path import dirname, abspath  # Return a normalized absolutized version of the pathname path
import sys                            # Import the "system specific parameters and functions" module
import datetime                       # Basic Date and Time types
import time as t                      # Time access and conversion
from shutil import copyfile           # Copy files
from PIL import Image                 # Python Imaging Library
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
def update(satellite, product, nfiles, outdir, vis_dir,sector):
    # Start the time counter
    #print('Script started.')
    #start = t.time()

    # Create the visualization directory if it doesn't exist
    out_dir = vis_dir

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # Create the satellite output directory if it doesn't exist
    out_dir = vis_dir + satellite

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # Create the product output directory if it doesn't exist
    out_dir = vis_dir + satellite + '//' + product + '//'
    gif_dir = out_dir
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # Read all the file names in the Output dir as a list
    files = []

    # Directory
    directory = outdir + satellite + '//' + product + '//'

    # File identifier
    #identifier = satellite + "_" + product + '*.png'
    identifier = satellite + "_" + product + '*.webp'

    # Rename identifier
    rename_id = satellite + "_" + product + '_'

    # Add to the list the files in the dir that matches the identifier
    for filename in sorted(glob.glob(directory + identifier)):
        files.append(filename)

    # Maximum number of frames
    max_files = nfiles

    # Keep on the list only the max number of files
    files = files[-max_files:]

    # Copy the files to the HTML Output folder, following the HTML naming convention
    for idx, val in enumerate(files):
        src = val
        #dst = out_dir + rename_id + str(idx + 1) + '.png'
        dst = out_dir + rename_id + str(idx + 1) + '.webp'

        # Convert from PNG to WebP
        #from PIL import Image
        #from PIL.WebPImagePlugin import Image
        #im = Image.open(val).convert("RGB")
        #im = Image.open(val)
        #im.save(out_dir + rename_id + str(idx + 1) + '.webp', format = "WebP", lossless = True)
        copyfile(src, dst)

    # Get the number of files on the folder
    num_files = len(files)
    # Get the difference of desired files and available files
    diff_files = max_files - num_files

    # If there are less files than the maximum HTML animation files, repeat the last one "x" times
    if diff_files > 0:
        for i in range(diff_files):
            #print(num_files + i + 1)
            #dst = out_dir + rename_id + str(num_files + i + 1) + '.png'
            dst = out_dir + rename_id + str(num_files + i + 1) + '.webp'
            # print(dst)

            #from PIL import Image
            #from PIL.WebPImagePlugin import Image

            #im = Image.open(files[-1])
            #im.save(out_dir + rename_id + str(num_files + i + 1) + '.webp', format = "WebP", lossless = True)

            copyfile(files[-1], dst)

    # Create the quicklook directory if it doesn't exist
    out_dir = vis_dir + 'QuickLooks//'

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    # Create the thumbnail of the last file
    thumb_dir = vis_dir + 'QuickLooks//' + rename_id + 'quicklook.webp'
    copyfile(files[-1], dst)
    im = Image.open(files[-1])
    if sector=='_ATL':
        size = (1920,785)
    elif sector=='_PAC':
        size = (1920,960)
    elif sector=='_ATN':
        size = (1920,791)
    else:
        size = (1920,1080)
    im = im.resize(size)
    im.save(thumb_dir)

    # Function to create a GIF
    # Check if the file is locked by previus process
    # def is_locked(filepath):
    #     locked = None
    #     file_object = None
    #     if os.path.exists(filepath):
    #         try:
    #             buffer_size = 8
    #             # Opening file in append mode and read the first 8 characters.
    #             file_object = open(filepath, 'a', buffer_size)
    #             if file_object:
    #                 locked = False
    #         except IOError as message:
    #             locked = True
    #         finally:
    #             if file_object:
    #                 file_object.close()
    #     return locked

    # def wait_for_file(filepath):
    #     wait_time = 5
    #     while is_locked(filepath):
    #         time.sleep(wait_time)

    # def make_gif(frame_folder, rename_id):
    #     # for image in sorted(glob.glob(f"{frame_folder}/*.webp")):
    #     #     wait_for_file(image)
    #     frames = [Image.open(image) for image in sorted(glob.glob(f"{frame_folder}/*.webp"))]
    #     frame_one = frames[0]
    #     frame_one.save(gif_dir + rename_id + ".gif", format="GIF", append_images=frames, save_all=True, duration=500, loop=0)

    # # Create GIF
    # make_gif(gif_dir,rename_id)
