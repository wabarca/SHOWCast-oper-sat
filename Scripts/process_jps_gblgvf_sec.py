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
__version__ = "2.5.0"
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
import re                                                    # Regular expression operations
import numpy as np                                           # Scientific computing with Python
import os                                                    # Miscellaneous operating system interfaces
from os.path import dirname, abspath                         # Return a normalized absolutized version of the pathname path 
import glob                                                  # Unix style pathname pattern expansion
import matplotlib.colors                                     # Matplotlib colors
import cartopy, cartopy.crs as ccrs                          # Plot maps
import cartopy.io.shapereader as shpreader                   # Import shapefiles
import matplotlib.pyplot as plt                              # Plotting library
import sys                                                   # Import the "system specific parameters and functions" module
import time as t                                             # Time access and conversion
from datetime import datetime, timedelta                     # Library to convert julian day to dd-mm-yyyy
from netCDF4 import Dataset                                  # Read / Write NetCDF4 files
from matplotlib.image import imread                          # Read an image from a file into an array
from cartopy.feature.nightshade import Nightshade            # Draws a polygon where there is no sunlight for the given datetime.
from html_update import update                               # Update the HTML animation 
from mpl_toolkits.axes_grid1.inset_locator import inset_axes # Add a child inset axes to this existing axes.
# Ignore possible warnings
import warnings
warnings.filterwarnings("ignore")
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Start the time counter
print('Script started.')
start_time = t.time()  

# SHOWCast directory:
main_dir = dirname(dirname(abspath(__file__)))
 
###############################################################################
# Reading the Data
###############################################################################
  
# Path to the image file
path = sys.argv[1]
path_im = path[:-7]
# Reading the sector
sector = sys.argv[9]
sector = sector[:-3]
# Open the file using the NetCDF4 library
file = Dataset(path_im)

# Define the extent
extent = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]
min_lon = extent[0]; max_lon = extent[2]; min_lat = extent[1]; max_lat = extent[3]

# Define KM_PER_DEGREE
KM_PER_DEGREE = 111.32

# Calculate the total number of degrees in lat and lon
deg_lon = extent[2] - extent[0]
deg_lat = extent[3] - extent[1]

# Calculate the number of pixels
resolution = int(sys.argv[6])
sizex = (KM_PER_DEGREE * deg_lon) /  resolution
sizey = (KM_PER_DEGREE * deg_lat) /  resolution
       
# Reading lats and lons 
lats = file.variables['latitude'][:]
lons = file.variables['longitude'][:]
 
# Latitude lower and upper index
latli = np.argmin( np.abs( lats - extent[1] ) )
latui = np.argmin( np.abs( lats - extent[3] ) )
 
# longitude lower and upper index
lonli = np.argmin( np.abs( lons - extent[0] ) )
lonui = np.argmin( np.abs( lons - extent[2] ) )
 
# Extract the data
data = file.variables['gvf_4km'][ latui:latli , lonli:lonui ]

# Getting the file time and date from the file name
start = (path[path.find("_s")+2:path.find("_e")])
end = (path[path.find("_e")+2:path.find("_c")])

date_formated = start[0:4] + '-' + start[4:6] + '-' + start[6:8] + ' to ' + end[0:4] + '-' + end[4:6] + '-' + end[6:8]
date_file = end[0:4] + end[4:6] + end[6:8]

#print(date_formated) 
#print(date_file) 
 
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Configuration
colors = ["#ccc1b1", "#b29569", "#96782c", "#7d8c28", "#75a014", "#67a100", "#529400", "#3d8700", "#1d7300", "#006000", "#004700", "#003800", "#002800", "#001400"]
cmap = matplotlib.colors.ListedColormap(colors)
cmap.set_over('#001400')
cmap.set_under('#ccc1b1')
vmin = 0.0
vmax = 1.0

thick_interval = 0.1
prod_title = 'JPSS VIIRS Fracción de vegetación verde (GVF) Composición semanal a 4km'
satellite = 'JPS'
product = 'GBLGVF'

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Plot configuration
plot_config = {
"resolution": resolution, 
"dpi": 150, 
"states_color": 'white', "states_width": 0.5, 
"countries_color": 'white', "countries_width": 0.5,
"continents_color": 'white', "continents_width": 0.5,
"grid_color": 'white', "grid_width": 0.3, "grid_interval": 5.0,
"vmin": vmin, "vmax": vmax, "cmap": cmap,
"title_text": prod_title + " ", "title_size": 8, "title_x_offset": int(sizex * 0.01), "title_y_offset": sizey - int(sizey * 0.016),
"thick_interval": thick_interval, "cbar_labelsize": 7, "cbar_labelpad": -int(sizey * 0.0),
"file_name_id_1": satellite,  "file_name_id_2": product + sector
}

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Choose the plot size (width x height, in inches)
fig = plt.figure(figsize=(1920/float(plot_config["dpi"]), 1080/float(plot_config["dpi"])), dpi=plot_config["dpi"])

# Define the projection
proj = ccrs.PlateCarree()

# Use the PlateCarree projection in cartopy
ax = plt.axes([0, 0, 1, 1], projection=proj)
img_extent = [extent[0], extent[2], extent[1], extent[3]]

# Add a background image
# ax.stock_img()
# fname = os.path.join(main_dir + '//Maps//', 'Layout1.png')
# ax.imshow(imread(fname), origin='upper', transform=ccrs.PlateCarree(), extent=[-100.0571149, -72.6764651, 5.6755730, 20.6259927], zorder=1)
#date = datetime(int(year), int(month), int(day), int(hour))
#ax.add_feature(Nightshade(date, alpha=0.7), zorder=2)

import cartopy.feature as cfeature
land = ax.add_feature(cfeature.LAND, facecolor='black', zorder=1)
ocean = ax.add_feature(cfeature.OCEAN, facecolor='black', zorder=2)

# Plot the image
img = ax.imshow(data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], origin='upper', extent=img_extent, cmap=plot_config["cmap"], zorder=3)
    
# To put colorbar inside picture
axins1 = inset_axes(ax, width="1%", height="25%", loc='upper right', borderpad=0.0)
  
# Add states and provinces
# shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//El_Salvador_departamentos.shp').geometries())
# ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["states_color"],facecolor='none', linewidth=plot_config["states_width"], zorder=4)

# Add countries
shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//Centro_America.shp').geometries())
ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["countries_color"],facecolor='none', linewidth=plot_config["countries_width"], zorder=4)

# Add continents
shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//GSHHS_h_L1_clipped.shp').geometries())
ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["continents_color"],facecolor='none', linewidth=plot_config["continents_width"], zorder=5)
  
# Add coastlines, borders and gridlines
gl = ax.gridlines(color=plot_config["grid_color"], alpha=1.0, linestyle='--', linewidth=plot_config["grid_width"], xlocs=np.arange(-180, 180, plot_config["grid_interval"]), ylocs=np.arange(-180, 180, plot_config["grid_interval"]), draw_labels=True, zorder=6)
gl.bottom_labels = False
gl.right_labels = False
gl.xpadding = -2
gl.ypadding = -2
gl.xlabel_style = {'size': 6, 'weight': 'bold', 'color': 'white'}
gl.ylabel_style = {'size': 6, 'weight': 'bold', 'color': 'white'}

# Remove the outline border
ax.outline_patch.set_visible(False)
  
# Add a title
plt.annotate(plot_config["title_text"] + " " + date_formated , xy=(0.015,0.965), xycoords='figure fraction', fontsize=plot_config["title_size"], fontweight='bold', color='white', bbox=dict(boxstyle="round",fc=(0.0, 0.0, 0.0), ec=(1., 1., 1.)), zorder=7)    
    
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Add logos / images to the plot
my_logo = plt.imread(main_dir + '//Logos//my_logo.webp')
newax = fig.add_axes([0.9, 0.0, 0.10, 0.10], anchor='S', zorder=8) #  [left, bottom, width, height]. All quantities are in fractions of figure width and height.
newax.imshow(my_logo)
newax.axis('off')

# Add a colorbar
ticks = np.arange(plot_config["vmin"], plot_config["vmax"], plot_config["thick_interval"]).tolist()     
ticks = plot_config["thick_interval"] * np.round(np.true_divide(ticks,plot_config["thick_interval"]))
ticks = ticks[1:]
cb = fig.colorbar(img, cax=axins1, orientation="vertical", ticks=ticks)
cb.set_label(label='GVF', color='white', size=plot_config["title_size"], weight='bold')
cb.outline.set_visible(True)
cb.outline.set_edgecolor('black')
cb.outline.set_linewidth(0.2)
cb.ax.yaxis.set_tick_params(pad=plot_config["cbar_labelpad"])
cb.ax.yaxis.set_ticks_position('left')
cb.ax.yaxis.set_label_position('left')

cb.ax.tick_params(axis='y', width = 0.5, colors='white',  labelsize=plot_config["cbar_labelsize"])

#---------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 
product = product + sector
# Create the satellite output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite
if not os.path.exists(out_dir):
   os.mkdir(out_dir)

# Create the product output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite + '//' + product + '//'
if not os.path.exists(out_dir):
   os.mkdir(out_dir)
                     
# Save the image
plt.savefig(out_dir + plot_config["file_name_id_1"] + "_" + plot_config["file_name_id_2"] + "_" + date_file + '.png', facecolor='black')

# Convert to webp
from PIL.WebPImagePlugin import Image          
im = Image.open(out_dir + plot_config["file_name_id_1"] + "_" + plot_config["file_name_id_2"] + "_" + date_file + '.png')
im.save(out_dir + plot_config["file_name_id_1"] + "_" + plot_config["file_name_id_2"] + "_" + date_file + '.webp', format = "WebP", lossless = True)
im.close()

# Update the animation
nfiles = 25
update(satellite, product, nfiles, sys.argv[7], sys.argv[8],sector)

# Delete aux files
os.remove(out_dir + plot_config["file_name_id_1"] + "_" + plot_config["file_name_id_2"] + "_" + date_file + '.png')  

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Put the processed file on the log
import datetime # Basic Date and Time types
with open(main_dir + '//Logs//gnc_log_' + str(datetime.datetime.now())[0:10] + '.txt', 'a') as log:
 log.write(str(datetime.datetime.now()))
 log.write('\n')
 log.write(path + '\n')
 log.write('\n')
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

print('Total processing time:', round((t.time() - start_time),2), 'seconds.') 