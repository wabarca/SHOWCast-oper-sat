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
import math                                                  # Import math
import glob, os
from matplotlib.image import imread                          # Read an image from a file into an array
import os                                                    # Miscellaneous operating system interfaces
from os.path import dirname, abspath                         # Return a normalized absolutized version of the pathname path 
import sys                                                   # Import the "system specific parameters and functions" module
from cartopy.feature.nightshade import Nightshade            # Draws a polygon where there is no sunlight for the given datetime.
from html_update import update                               # Update the HTML animation 
from remap import remap                                      # Import the Remap function
import matplotlib.patheffects as PathEffects
import warnings
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
path_proc = path[:-7]

# Read the image
file = Dataset(path_proc)

# Read the satellite 
satellite = getattr(file, 'platform_ID')

# Read the main variable
variable = list(file.variables.keys())[0]

# Read the units
variable_units = str(file.variables[variable].units)
if (variable_units == 'K'):
    variable_units = 'C'

# Read the product name
prod_name = getattr(file, 'title')

# Add "SEC" to the product name to identify that is a sector product
sector = sys.argv[9] 
sector = sector[:-3]

# Desired resolution
resolution = int(sys.argv[6])

# Read the resolution
band_resolution_km = getattr(file, 'spatial_resolution')
band_resolution_km = float(band_resolution_km[:band_resolution_km.find("km")])

# Division factor to reduce image size
f = math.ceil(float(resolution / band_resolution_km))

#print(resolution)
#print(band_resolution_km)
#print(f)

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

# Choose the visualization extent (min lon, min lat, max lon, max lat)
extent = [float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])]

# Call the reprojection funcion
grid = remap(path_proc, variable, extent, resolution, h, a, b, longitude, x1, y1, x2, y2)

# Read the data returned by the function 
data = grid.ReadAsArray() 

# Convert from int16 to uint16
data = data.astype(np.float64)

#print(data.shape)
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
if (variable == 'HT'):  
    # ACHAF
    colors = ["#000000", "#804000", "#ff00ff", "#0000ff", "#00ffff", "#00ff00", "#ffff00", "#ff0000", "#c0c0c0", "#ffffff"]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    vmin = 0
    vmax = 15000
    thick_interval = 1000
    product = "CLDHGT" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'TEMP'):  
    # ACHTF
    cmap = 'jet'
    vmin = -95
    vmax = 30
    # vmin = 180
    # vmax = 300
    thick_interval = 10
    data -= 273.15    
    data[data == 0] = np.nan
    product = "CLDTMP" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'BCM'): 
    # ACMF
    colors = ["#ffffff"]
    cmap = matplotlib.colors.ListedColormap(colors)
    vmin = 0
    vmax = 2
    thick_interval = 1
    data[data == 0] = np.nan
    product = "CLDMSK" + sector
    data[data == 255] = np.nan
    data[data == 0] = np.nan
elif (variable == 'Phase'): 
    # ACTPF
    colors = ["#00ffff", "#00ff00", "#30782a", "#ff0000"]#, "#000000"]
    cmap = matplotlib.colors.ListedColormap(colors)
    vmin = 1
    vmax = 4
    thick_interval = 1
    data[data == 0] = np.nan
    data[data == 5] = np.nan    
    product = "CLDPHA" + sector
    data[data >= 5] = np.nan
    data[data == 0] = np.nan
elif (variable == 'AOD'): 
    # AODF
    cmap = 'jet'
    vmin = 0
    vmax = 1
    thick_interval = 0.1
    product = "AEROPT" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'COD'): 
    # CODF
    cmap = 'jet'
    vmin = 0
    vmax = 100
    thick_interval = 10
    product = "CLDOPT" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'PSD'): 
    # CPSF
    cmap = 'jet'
    vmin = 0
    vmax = 100
    thick_interval = 10
    product = "CLDPAS" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'PRES'): 
    # CTPF
    cmap = 'jet'
    vmin = 0
    vmax = 1050
    thick_interval = 100
    product = "CLDPRE" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'FSC'): 
    # FSCF
    cmap = 'gist_stern'
    vmin = 0
    vmax = 1
    thick_interval = 0.1
    product = "SNOWCO" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'LST'):
    # LSTF
    cmap = 'jet'
    # vmin = -83.15
    # vmax = 61.85
    # thick_interval = 10
    vmin = 5
    vmax = 40
    thick_interval = 5
    product = "LSTSKN" + sector
    data[data >= 335] = 0
    data[data == 190] = np.nan
    data -= 273.15    
    data[data == min(data[0])] = np.nan
elif (variable == 'RRQPE'):
    # RRQPE
    # colors = ["#69d7dc","#0939f0","#79f648","#408624","#fcf64a","#ecac33","#eb611e","#ac240b"]
    # cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    cmap = 'jet'
    vmin = 0
    vmax = 60
    thick_interval = 5
    data[data == 0] = np.nan
    product = "RRQPEF" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
elif (variable == 'SST'):
    # SSTF
    cmap = 'jet'
    # vmin = -5.15
    # vmax = 34.85
    vmin = 27
    vmax = 33
    data -= 273.15    
    thick_interval = 1
    data[data == max(data[0])] = np.nan   
    data[data == min(data[0])] = np.nan
    # Read the DQF data
    #data_DQF = file.variables['DQF'][::f ,::f]
    # Call the reprojection funcion
    grid = remap(path_proc, 'DQF', extent, resolution, h, a, b, longitude, x1, y1, x2, y2)
    # Read the data returned by the function 
    data_DQF = grid.ReadAsArray()
    data_DQF = data_DQF.astype(np.float64)  
    data[data_DQF != 0] = np.nan
    product = "SSTSKN" + sector
elif (variable == 'TPW'):
    # TPW
    colors = ["#bc8462", "#ae656f", "#a44a79", "#962e97", "#6158c5", "#2b8ffb", "#5fcdff", "#94fff0", "#a5ff94", "#fff88c", "#ffbf52", "#ec7b27", "#b84827", "#a1333d", "#bd5478", "#cc6a99", "#d982b8"]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    vmin = 0
    vmax = 80
    thick_interval = 0.1
    product = "TOTPWA" + sector
    data[data == max(data[0])] = np.nan
    data[data == min(data[0])] = np.nan
#------------------------------------------------------------------------------------------------------
# Plot configuration
plot_config = {
"resolution": band_resolution_km, 
"dpi": 150, 
"states_color": 'black', "states_width": 0.5, 
"countries_color": 'black', "countries_width": 0.5,
"continents_color": 'black', "continents_width": 0.5,
"grid_color": 'white', "grid_width": 0.5, "grid_interval": 1.0,
"vmin": vmin, "vmax": vmax, "cmap": cmap,
"title_text": "GOES-16 " + prod_name + " [" + variable_units + "]", "title_size": 8, "title_x_offset": int(data.shape[1] * 0.01), "title_y_offset": data.shape[0] - int(data.shape[0] * 0.016), 
"thick_interval": thick_interval, "cbar_labelsize": 8, "cbar_labelpad": -int(data.shape[0] * 0.0),
"file_name_id_1": "G16",  "file_name_id_2": product 
}
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
fname = os.path.join(main_dir + '//Maps//', 'eo_base_2020_clean_geo.png')
ax.imshow(imread(fname), origin='upper', transform=ccrs.PlateCarree(), extent=[-180, 180, -90, 90], zorder=1)
date = datetime(int(year), int(month), int(day), int(hour))

# Plot the image
if (variable == 'RRQPE'):
    # from matplotlib import colors, cm
    # norm = colors.LogNorm(vmin, vmax, clip='False')
    # img = ax.imshow(data, norm=norm, origin='upper', extent=img_extent, cmap=plot_config["cmap"], zorder=2)
    img = ax.imshow(data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], origin='upper', extent=img_extent, cmap=plot_config["cmap"], zorder=2)
else:
    img = ax.imshow(data, vmin=plot_config["vmin"], vmax=plot_config["vmax"], origin='upper', extent=img_extent, cmap=plot_config["cmap"], zorder=2)

# To put colorbar inside picture
axins1 = inset_axes(ax, width="100%", height="2%", loc='lower center', borderpad=0.0)
  
if sector == "_SLV":
    grid_interval=1.0
    # Add states and provinces
    shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//El_Salvador_departamentos.shp').geometries())
    ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["states_color"],facecolor='none', linewidth=plot_config["states_width"], zorder=3)
    # Add countries
    shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//Centro_America.shp').geometries())
    ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["countries_color"],facecolor='none', linewidth=plot_config["countries_width"], zorder=4)
else:
    grid_interval=5.0
    # Add countries 
    shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//Centro_America.shp').geometries()) 
    ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["countries_color"],facecolor='none', linewidth=plot_config["countries_width"], zorder=3)
    # Add continents
    shapefile = list(shpreader.Reader(main_dir + '//Shapefiles//GSHHS_h_L1_clipped.shp').geometries())
    ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor=plot_config["continents_color"],facecolor='none', linewidth=plot_config["continents_width"], zorder=4)

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Hurricane tracks 
#---------------------------------------------------------------------------------------------
# Required libs
import urllib.request
import zipfile
from tropycal import realtime
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Invest: plot monitoring areas
#---------------------------------------------------------------------------------------------
# Cleaning NHC working dir
for files in glob.glob(main_dir + "//Shapefiles//nhc//*"):
    os.remove(files)
# Downloading latest GIS data for selected monitoring areas:
nhc_gis_files = "https://www.nhc.noaa.gov/xgtwo/gtwo_shapefiles.zip"
urllib.request.urlretrieve(nhc_gis_files, main_dir + "//Shapefiles//nhc//gtwo_shapefiles.zip")
with zipfile.ZipFile(main_dir + "//Shapefiles//nhc//gtwo_shapefiles.zip", 'r') as zip_ref:
    zip_ref.extractall(main_dir + "//Shapefiles//nhc//")
# Reading NHC shapefiles
shp_files = []
for filename in glob.glob(main_dir + '//Shapefiles//nhc//gtwo_areas_*.shp'):
    shp_files.append(os.path.normpath(filename))
for filename in glob.glob(main_dir + '//Shapefiles//nhc//gtwo_points_*.shp'):
    shp_files.append(os.path.normpath(filename))
for filename in glob.glob(main_dir + '//Shapefiles//nhc//gtwo_lines_*.shp'):
    shp_files.append(os.path.normpath(filename))
# Add probabilities areas
shapefile = list(shpreader.Reader(shp_files[0]).records())
areas_low = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) < 40]
areas_medium = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) >= 40 and float(x.attributes['PROB2DAY'].replace("%", "")) <= 60]
areas_high = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) > 60]
# Plotting probabilities ares
ax.add_geometries(areas_low, ccrs.PlateCarree(), edgecolor='gold',facecolor='yellow',alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
ax.add_geometries(areas_medium, ccrs.PlateCarree(), edgecolor='darkorange',facecolor='orange',alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
ax.add_geometries(areas_high, ccrs.PlateCarree(), edgecolor='darkred',facecolor='red',alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
# Add trajectories areas
shapefile = list(shpreader.Reader(shp_files[2]).records())
trajectories_low = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) < 40]
trajectories_medium = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) >= 40 and float(x.attributes['PROB2DAY'].replace("%", "")) <= 60]
trajectories_high = [x.geometry for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) > 60]
# Plotting trajectories
ax.add_geometries(trajectories_low, ccrs.PlateCarree(), edgecolor='gold',facecolor='none', alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
ax.add_geometries(trajectories_medium, ccrs.PlateCarree(), edgecolor='darkorange',facecolor='none', alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
ax.add_geometries(trajectories_high, ccrs.PlateCarree(), edgecolor='darkred',facecolor='none', alpha=0.4, linewidth=plot_config["states_width"]*6, zorder=5)
# Add positions
shapefile = list(shpreader.Reader(shp_files[1]).records())
points_low = [x for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) < 40]
points_medium = [x for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) >= 40 and float(x.attributes['PROB2DAY'].replace("%", "")) <= 60]
points_high = [x for x in shapefile if float(x.attributes['PROB2DAY'].replace("%", "")) > 60]
# Plotting positions and labels
for pl in points_low:
    ax.scatter(pl.geometry.x,pl.geometry.y, marker='X', s=150, edgecolor='black', facecolor='gold', transform=ccrs.PlateCarree(), zorder=6)
    if float(pl.attributes['PROB7DAY'].replace("%", "")) < 40:
        text = ax.text(pl.geometry.x+0.5,pl.geometry.y-0.5,'7d: '+pl.attributes['PROB7DAY'],color='gold', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    elif float(pl.attributes['PROB7DAY'].replace("%", "")) >= 40 and float(pl.attributes['PROB7DAY'].replace("%", "")) <= 60:
        text = ax.text(pl.geometry.x+0.5,pl.geometry.y-0.5,'7d: '+pl.attributes['PROB7DAY'],color='orange', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    else:
        text = ax.text(pl.geometry.x+0.5,pl.geometry.y-0.5,'7d: '+pl.attributes['PROB7DAY'],color='red', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(pl.geometry.x+0.5,pl.geometry.y+0.5,'2d: '+pl.attributes['PROB2DAY'],color='gold', fontsize='large', fontweight='bold',zorder=6)
    text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
for pm in points_medium:
    ax.scatter(pm.geometry.x,pm.geometry.y, marker='X', s=150, edgecolor='black', facecolor='orange', transform=ccrs.PlateCarree(), zorder=6)
    if float(pm.attributes['PROB7DAY'].replace("%", "")) < 40:
        text = ax.text(pm.geometry.x+0.5,pm.geometry.y-0.5,'7d: '+pm.attributes['PROB7DAY'],color='gold', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    elif float(pm.attributes['PROB7DAY'].replace("%", "")) >= 40 and float(pm.attributes['PROB7DAY'].replace("%", "")) <= 60:
        text = ax.text(pm.geometry.x+0.5,pm.geometry.y-0.5,'7d: '+pm.attributes['PROB7DAY'],color='orange', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    else:
        text = ax.text(pm.geometry.x+0.5,pm.geometry.y-0.5,'7d: '+pm.attributes['PROB7DAY'],color='red', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(pm.geometry.x+0.5,pm.geometry.y+0.5,'2d: '+pm.attributes['PROB2DAY'],color='orange', fontsize='large', fontweight='bold',zorder=6)
    text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
for ph in points_high:
    ax.scatter(ph.geometry.x,ph.geometry.y, marker='X', s=150, edgecolor='black', facecolor='red', transform=ccrs.PlateCarree(), zorder=6)
    if float(ph.attributes['PROB7DAY'].replace("%", "")) < 40:
        text = ax.text(ph.geometry.x+0.5,ph.geometry.y-0.5,'7d: '+ph.attributes['PROB7DAY'],color='gold', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    elif float(ph.attributes['PROB7DAY'].replace("%", "")) >= 40 and float(ph.attributes['PROB7DAY'].replace("%", "")) <= 60:
        text = ax.text(ph.geometry.x+0.5,ph.geometry.y-0.5,'7d: '+ph.attributes['PROB7DAY'],color='orange', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    else:
        text = ax.text(ph.geometry.x+0.5,ph.geometry.y-0.5,'7d: '+ph.attributes['PROB7DAY'],color='red', fontsize='large', fontweight='bold',zorder=6)
        text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(ph.geometry.x+0.5,ph.geometry.y+0.5,'2d: '+ph.attributes['PROB2DAY'],color='red', fontsize='large', fontweight='bold',zorder=6)
    text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
# Reading realtime active NHC data:
realtime_obj = realtime.Realtime()
# Extracting list of active system names
tsystems = realtime_obj.list_active_storms(basin='all')
# Checking if a system name is an Invest or not
for name in tsystems:
    storm = realtime_obj.get_storm(name)
    if storm.invest == True:
        print(name + " is an invest!")
    else:
        print(name + " is not an invest!")
        #---------------------------------------------------------------------------------------------
        # Invest: plot monitoring areas
        #---------------------------------------------------------------------------------------------
        # Cleaning NHC working dir
        for files in glob.glob(main_dir + "//Shapefiles//nhc//*"):
            os.remove(files)
        # Downloading latest GIS data for selected storm:
        nhc_gis_files = "https://www.nhc.noaa.gov/gis/forecast/archive/"+name.lower()+"_5day_latest.zip"
        urllib.request.urlretrieve(nhc_gis_files, main_dir + "//Shapefiles//nhc//"+name.lower()+"_5day_latest.zip")
        with zipfile.ZipFile(main_dir + "//Shapefiles//nhc//"+name.lower()+"_5day_latest.zip", 'r') as zip_ref:
             zip_ref.extractall(main_dir + "//Shapefiles//nhc//")
        # Reading NHC shapefiles
        shp_files = []
        for filename in glob.glob(main_dir + '//Shapefiles//nhc//'+name.lower()+'*_5day_lin.shp'):
            shp_files.append(os.path.normpath(filename))
        for filename in glob.glob(main_dir + '//Shapefiles//nhc//'+name.lower()+'*_5day_pgn.shp'):
            shp_files.append(os.path.normpath(filename))
        for filename in glob.glob(main_dir + '//Shapefiles//nhc//'+name.lower()+'*_5day_pts.shp'):
            shp_files.append(os.path.normpath(filename))
        # Add line trajectory
        shapefile = list(shpreader.Reader(shp_files[0]).geometries())
        ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='white',facecolor='none', linewidth=plot_config["states_width"]*4, zorder=7)
        # Add probabilities cone
        shapefile = list(shpreader.Reader(shp_files[1]).geometries())
        ax.add_geometries(shapefile, ccrs.PlateCarree(), edgecolor='black',facecolor='white', alpha=0.4,linewidth=plot_config["states_width"]*4, zorder=8)
        # Add positions
        shapefile = list(shpreader.Reader(shp_files[2]).geometries())
        # Plotting positions and labels
        ax.scatter([shapefile.x for shapefile in shapefile],[shapefile.y for shapefile in shapefile], edgecolor='black', facecolor='red', transform=ccrs.PlateCarree(), zorder=9)
        shapefile = list(shpreader.Reader(shp_files[2]).records())
        for field in shapefile:
            text = ax.text((field.attributes['LON']+0.5),(field.attributes['LAT']+0.5),field.attributes['DVLBL'],color='blue', fontsize='large', fontweight='bold',zorder=10)
            text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='w')])

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
# Add coastlines, borders and gridlines
gl = ax.gridlines(color=plot_config["grid_color"], alpha=0.5, linestyle='--', linewidth=plot_config["grid_width"], xlocs=np.arange(-180, 180, grid_interval), ylocs=np.arange(-180, 180, grid_interval), draw_labels=True, zorder=11)
gl.bottom_labels = False
gl.right_labels = False
gl.xpadding = -2
gl.ypadding = -2
gl.xlabel_style = {'size': 6, 'weight': 'bold', 'color': 'black'}
gl.ylabel_style = {'size': 6, 'weight': 'bold', 'color': 'black'}

# Remove the outline border
ax.outline_patch.set_visible(False)
  
# Add a title
plt.annotate(plot_config["title_text"] + " " + date_formated , xy=(0.015,0.965), xycoords='figure fraction', fontsize=plot_config["title_size"], fontweight='bold', color='white', bbox=dict(boxstyle="round",fc=(0.0, 0.0, 0.0), ec=(1., 1., 1.)), zorder=12)

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
    ax.plot(xpt, ypt, str(mtype), color=str(mcolor), markersize=int(msize), transform=ccrs.Geodetic(), markeredgewidth=1.0, markeredgecolor=(0, 0, 0, 1), zorder=13)
    txt = ax.text(xpt+x_offset , ypt+y_offset, label, fontsize=int(size), fontweight='bold', color=str(col), transform=ccrs.Geodetic(), zorder=14)
    txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# Add logos / images to the plot
my_logo = plt.imread(main_dir + '//Logos//my_logo.webp')
newax = fig.add_axes([0.84, 0.05, 0.15, 0.15], anchor='SW', zorder=15) #  [left, bottom, width, height]. All quantities are in fractions of figure width and height.
newax.imshow(my_logo)
newax.axis('off')

if (variable == 'Phase'): 
	# Add a legend to the plot
	my_legend = plt.imread(main_dir + '//Legends//PHASE_legend.webp')
	newax = fig.add_axes([0.87, 0.87, 0.12, 0.12], anchor='NE', zorder=16) #  [left, bottom, width, height]. All quantities are in fractions of figure width and height.
	newax.imshow(my_legend)
	newax.axis('off')

# Add a colorbar
ticks = np.arange(plot_config["vmin"], plot_config["vmax"], plot_config["thick_interval"]).tolist()     
ticks = plot_config["thick_interval"] * np.round(np.true_divide(ticks,plot_config["thick_interval"]))
ticks = ticks[1:]
cb = fig.colorbar(img, cax=axins1, orientation="horizontal", ticks=ticks)
cb.outline.set_visible(False)
cb.ax.tick_params(width = 0)
cb.ax.xaxis.set_tick_params(pad=plot_config["cbar_labelpad"])
cb.ax.xaxis.set_ticks_position('top')
cb.ax.tick_params(axis='x', colors='black', labelsize=plot_config["cbar_labelsize"])

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
os.remove(path_proc +'.aux.xml')

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
