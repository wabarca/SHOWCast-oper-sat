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
from netCDF4 import Dataset                                  # Read / Write NetCDF4 files
from mpl_toolkits.axes_grid1.inset_locator import inset_axes # Add a child inset axes to this existing axes.
from datetime import datetime, timedelta                     # Library to convert julian day to dd-mm-yyyy
from cpt_convert import loadCPT                              # Import the CPT convert function
from matplotlib.colors import LinearSegmentedColormap        # Linear interpolation for color maps
import matplotlib.pyplot as plt                              # Plotting library
import matplotlib.colors                                     # Matplotlib colors
import numpy as np                                           # Scientific computing with Python
import cartopy, cartopy.crs as ccrs                          # Plot maps
import cartopy.io.shapereader as shpreader                   # Import shapefiles
import time as t                                             # Time access and conversion
from matplotlib.image import imread                          # Read an image from a file into an array
import os                                                    # Miscellaneous operating system interfaces
from os.path import dirname, abspath                         # Return a normalized absolutized version of the pathname path
import sys                                                   # Import the "system specific parameters and functions" module
from cartopy.feature.nightshade import Nightshade            # Draws a polygon where there is no sunlight for the given datetime.
from html_update import update                               # Update the HTML animation
import warnings
from remap import remap                                      # Import the Remap function
warnings.filterwarnings("ignore")
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Start the time counter
print('Script started.')
start = t.time()

# SHOWCast directory:
main_dir = dirname(dirname(abspath(__file__)))

# Image path
path = (sys.argv[1])

# Remove the composite id
path_proc = path[:-4]

# Read the image
file = Dataset(path_proc)

# Read the satellite
satellite = getattr(file, 'platform_ID')
#------ esto es nuevo en GOES-19 --------

# Read the main variable
variable = list(file.variables.keys())[0]

# Read the units
variable_units = str(file.variables[variable].units)

# Add "SEC" to the product name to identify that is a sector product
sector = sys.argv[9]

# Read the product name
prod_name = getattr(file, 'title')

# Desired resolution
resolution = int(sys.argv[6])
band_resolution_km = int(sys.argv[6])

# Read the resolution
band_resolution_km = getattr(file, 'spatial_resolution')
band_resolution_km = float(band_resolution_km[:band_resolution_km.find("km")])

# Get the central longitude
longitude = file.variables['geospatial_lat_lon_extent'].geospatial_lon_center
# Read the central longitude
longitude = file.variables['goes_imager_projection'].longitude_of_projection_origin

# Read the semi major axis
a = file.variables['goes_imager_projection'].semi_major_axis

# Read the semi minor axis
b = file.variables['goes_imager_projection'].semi_minor_axis

# Calculate the image extent
h = file.variables['goes_imager_projection'].perspective_point_height
x1 = file.variables['x_image_bounds'][0] * h
x2 = file.variables['x_image_bounds'][1] * h
y1 = file.variables['y_image_bounds'][1] * h
y2 = file.variables['y_image_bounds'][0] * h
#-----------------------------------------------------


# Choose the visualization extent (min lon, min lat, max lon, max lat)
extent = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]

# Call the reprojection funcion
grid = remap(path_proc, variable, extent, resolution, h, a, b, longitude, x1, y1, x2, y2)

# Read the data returned by the function
data = grid.ReadAsArray()

# Convert from int16 to uint16
data = data.astype(np.float64)

# Define KM_PER_DEGREE
KM_PER_DEGREE = 111.32

# Compute grid dimension
sizex = int(((extent[2] - extent[0]) * KM_PER_DEGREE) / resolution)
sizey = int(((extent[3] - extent[1]) * KM_PER_DEGREE) / resolution)

# Reading the file time and date
add_seconds = int(file.variables['time_bounds'][0])
date = datetime(2000,1,1,12) + timedelta(seconds=add_seconds)
date_formated = date.strftime('%Y-%m-%d %H:%M UTC')
date_file = date.strftime('%Y%m%d%H%M')
year = date.strftime('%Y')
month = date.strftime('%m')
day = date.strftime('%d')
hour = date.strftime('%H')
minutes = date.strftime('%M')

# Read the data
#data = file.variables[variable][:,:][::1,::1]

# Read the lats
#lats = file.variables['lat'][:]

# Read the lons
#lons = file.variables['lon'][:]

# Convert from int16 to uint16
#data = data.astype(np.float64)

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
if (variable == 'RSR'):
    # RSRF
    # colors = ["#a200ae", "#1911e6", "#007bd7", "#5fff00", "#ffff00", "#ff7c00", "#ff0000"]
    # cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    cmap = 'jet'
    vmin = 0
    vmax = 1000
    thick_interval = 100
    data[data == 0] = np.nan
    product = "RSRADI" + sector
elif (variable == 'DSR'):
    # DSRF
    # colors = ["#a200ae", "#1911e6", "#007bd7", "#5fff00", "#ffff00", "#ff7c00", "#ff0000"]
    # cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    cmap = 'jet'
    vmin = 0
    vmax = 1000
    thick_interval = 100
    data[data == 0] = np.nan
    product = "DSRADI" + sector
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Plot configuration
plot_config = {
"resolution": band_resolution_km,
"dpi": 150,
"states_color": 'gold', "states_width": 0.5,
"countries_color": 'gold', "countries_width": 0.5,
"continents_color": 'gold', "continents_width": 0.5,
"grid_color": 'white', "grid_width": 0.5, "grid_interval": 5.0,
"vmin": vmin, "vmax": vmax, "cmap": 'jet',
"title_text": "GOES-19 " + prod_name + " ["+variable_units+"]", "title_size": 8, "title_x_offset": int(sizex * 0.01), "title_y_offset": sizey - int(sizey * 0.016),
"thick_interval": thick_interval, "cbar_labelsize": 8, "cbar_labelpad": -int(sizey * 0.0),
"file_name_id_1": "G19",  "file_name_id_2": product
}
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Choose the plot size (width x height, in inches)
fig = plt.figure(figsize=(1920/float(plot_config["dpi"]), 1080/float(plot_config["dpi"])), dpi=plot_config["dpi"])

# Define the projection
proj = ccrs.PlateCarree()

# Use the PlateCarree projection in cartopy
ax = plt.axes([0, 0, 1, 1], projection=proj)
ax.set_extent([extent[0], extent[2], extent[1], extent[3]], ccrs.PlateCarree())

# Define the image extent
img_extent = [extent[0], extent[2], extent[1], extent[3]]

# Add a background image
#ax.stock_img()
# fname = os.path.join(main_dir + '//Maps//', 'world.topo.bathy.200408.3x5400x2700.jpg')
# ax.imshow(imread(fname), origin='upper', transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90], zorder=1)
fname = os.path.join(main_dir + '//Maps//', 'Layout1.png')
ax.imshow(imread(fname), origin='upper', transform=ccrs.PlateCarree(), extent=[-100.057, -72.676, 5.8, 20.63], zorder=1)

# date = datetime(int(year), int(month), int(day), int(hour))

# Plot the image
# img = ax.pcolormesh(lons, lats, data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], cmap=plot_config["cmap"],transform=ccrs.PlateCarree(), shading='gouraud', zorder=2)
# img = ax.pcolormesh(lons, lats, data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], cmap=plot_config["cmap"],transform=ccrs.PlateCarree(), alpha=0.7, zorder=2)
img = ax.pcolormesh(data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], cmap=plot_config["cmap"],transform=ccrs.PlateCarree(), alpha=0.7, zorder=2)

# To put colorbar inside picture
axins1 = inset_axes(ax, width="1%", height="25%", loc='upper right', borderpad=0.0)

# Add states and provinces
# shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//El_Salvador_departamentos.shp').geometries())
# ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["states_color"],facecolor='none', linewidth=plot_config["states_width"], zorder=4)

# Add countries
shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//Centro_America.shp').geometries())
ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["countries_color"],facecolor='none', linewidth=plot_config["countries_width"], zorder=3)

# Add continents
shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//GSHHS_h_L1_clipped.shp').geometries())
ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["continents_color"],facecolor='none', linewidth=plot_config["continents_width"], zorder=4)

# Add coastlines, borders and gridlines
gl = ax.gridlines(color=plot_config["grid_color"], alpha=0.5, linestyle='--', linewidth=plot_config["grid_width"], xlocs=np.arange(-180, 180, plot_config["grid_interval"]), ylocs=np.arange(-180, 180, plot_config["grid_interval"]), draw_labels=True, zorder=5)
gl.bottom_labels = False
gl.right_labels = False
gl.xpadding = -2
gl.ypadding = -2
gl.xlabel_style = {'size': 6, 'weight': 'bold', 'color': 'white'}
gl.ylabel_style = {'size': 6, 'weight': 'bold', 'color': 'white'}

# Remove the outline border
ax.outline_patch.set_visible(False)

# Add a title
plt.annotate(plot_config["title_text"] + " " + date_formated , xy=(0.015,0.965), xycoords='figure fraction', fontsize=plot_config["title_size"], fontweight='bold', color='white', bbox=dict(boxstyle="round",fc=(0.0, 0.0, 0.0), ec=(1., 1., 1.), zorder=6))

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Add labels to specific coordinates

import configparser
conf = configparser.ConfigParser()
conf.read(main_dir + '//Utils//Labels//labels_g16_cam.ini')

labels, city_lons, city_lats, x_offsets, y_offsets, sizes, colors, marker_types, marker_colors, marker_sizes = [],[],[],[],[],[],[],[],[],[]

for each_section in conf.sections():
    for (each_key, each_val) in conf.items(each_section):
        if (each_key == 'label'): labels.append(each_val)
        if (each_key == 'lon'): city_lons.append(float(each_val))
        if (each_key == 'lat'): city_lats.append(float(each_val))
        if (each_key == 'x_offset'): x_offsets.append(float(each_val))
        if (each_key == 'y_offset'): y_offsets.append(float(each_val))
        if (each_key == 'size'): sizes.append(int(each_val))
        if (each_key == 'color'): colors.append(each_val)
        if (each_key == 'marker_type'): marker_types.append(each_val)
        if (each_key == 'marker_color'): marker_colors.append(each_val)
        if (each_key == 'marker_size'): marker_sizes.append(each_val)

import matplotlib.patheffects as PathEffects
for label, xpt, ypt, x_offset, y_offset, size, col, mtype, mcolor, msize in zip(labels, city_lons, city_lats, x_offsets, y_offsets, sizes, colors, marker_types, marker_colors, marker_sizes):
    ax.plot(xpt, ypt, str(mtype), color=str(mcolor), markersize=int(msize), transform=ccrs.Geodetic(), markeredgewidth=1.0, markeredgecolor=(0, 0, 0, 1), zorder=7)
    txt = ax.text(xpt+x_offset , ypt+y_offset, label, fontsize=int(size), fontweight='bold', color=str(col), transform=ccrs.Geodetic(), zorder=8)
    txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Add logos / images to the plot
my_logo = plt.imread(main_dir + '//Logos//my_logo.webp')
newax = fig.add_axes([0.9, 0.0, 0.10, 0.10], anchor='S', zorder=9) #  [left, bottom, width, height]. All quantities are in fractions of figure width and height.
newax.imshow(my_logo)
newax.axis('off')

# Add a colorbar
ticks = np.arange(plot_config["vmin"], plot_config["vmax"], plot_config["thick_interval"]).tolist()
ticks = plot_config["thick_interval"] * np.round(np.true_divide(ticks,plot_config["thick_interval"]))
ticks = ticks[1:]
cb = fig.colorbar(img, cax=axins1, orientation="vertical", ticks=ticks)
cb.outline.set_visible(True)
cb.outline.set_edgecolor('black')
cb.outline.set_linewidth(0.2)
cb.ax.yaxis.set_tick_params(pad=plot_config["cbar_labelpad"])
cb.ax.yaxis.set_ticks_position('left')
cb.ax.yaxis.set_label_position('left')
cb.set_label('[ '+variable_units+' ]', color='white', size=plot_config["cbar_labelsize"], weight='bold')
cb.ax.tick_params(axis='y', width = 0.5, colors='white', labelsize=plot_config["cbar_labelsize"])

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

# Create the satellite output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite
if not os.path.exists(out_dir):
   os.mkdir(out_dir)

# Create the product output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite + '//' + product + '//'
if not os.path.exists(out_dir):
   os.mkdir(out_dir)

# Save the image
plt.savefig(out_dir + plot_config["file_name_id_1"] + "_" + plot_config["file_name_id_2"] + "_" + date_file + '.png', facecolor='black')#, bbox_inches='tight', pad_inches=0, facecolor='black')
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

print('Total processing time:', round((t.time() - start),2), 'seconds.')
