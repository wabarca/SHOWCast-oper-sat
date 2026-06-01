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
import cartopy.crs as ccrs  # Plot maps
import cartopy
import datetime  # Basic Date and Time types
from PIL.WebPImagePlugin import Image
import warnings
from mpl_toolkits.axes_grid1.inset_locator import (
    inset_axes,
)  # Add a child inset axes to this existing axes.
from html_update import update  # Update the HTML animation
from cartopy.feature.nightshade import (
    Nightshade,
)  # Draws a polygon where there is no sunlight for the given datetime.
from matplotlib.image import imread  # Read an image from a file into an array
from netCDF4 import Dataset  # Read / Write NetCDF4 files

# Library to convert julian day to dd-mm-yyyy
from datetime import datetime, timedelta
import time as t  # Time access and conversion
import sys  # Import the "system specific parameters and functions" module
import matplotlib.pyplot as plt  # Plotting library
import cartopy.io.shapereader as shpreader  # Import shapefiles
import matplotlib.colors  # Matplotlib colors
import glob  # Unix style pathname pattern expansion
from os.path import (
    dirname,
    abspath,
)  # Return a normalized absolutized version of the pathname path
import os  # Miscellaneous operating system interfaces
import numpy as np  # Scientific computing with Python
import re  # Regular expression operations
import matplotlib.patheffects as PathEffects

__author__ = "Diego Souza"
__copyright__ = (
    "Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL"
)
__credits__ = ["Diego Souza"]
__license__ = "GPL"
__version__ = "2.4.0"
__maintainer__ = "Diego Souza"
__email__ = "diego.souza@inpe.br"
__status__ = "Production"
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# Required modules
# --------------------------------
# to run in a pure text terminal:
import matplotlib

matplotlib.use("Agg")
# --------------------------------

# Ignore possible warnings

warnings.filterwarnings("ignore")
# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
# Start the time counter
print("Script started.")
start_time = t.time()

# SHOWCast directory:
main_dir = dirname(dirname(abspath(__file__)))

###############################################################################
# Reading the Data
###############################################################################

# Path to the image file
path = sys.argv[1]

# Add "SEC" to the product name to identify that is a sector product
sector = sys.argv[9]

# Open the file using the NetCDF4 library
file = Dataset(path[:-4])

# Define the extent
extent = [
    float(sys.argv[2]),
    float(sys.argv[3]),
    float(sys.argv[4]),
    float(sys.argv[5]),
]
min_lon = extent[0]
max_lon = extent[2]
min_lat = extent[1]
max_lat = extent[3]

# Define KM_PER_DEGREE
KM_PER_DEGREE = 111.32

# Calculate the total number of degrees in lat and lon
deg_lon = extent[2] - extent[0]
deg_lat = extent[3] - extent[1]

# Calculate the number of pixels
resolution = int(sys.argv[6])
sizex = (KM_PER_DEGREE * deg_lon) / resolution
sizey = (KM_PER_DEGREE * deg_lat) / resolution

# Reading lats and lons
lats = file.variables["lat"][:]
lons = file.variables["lon"][:]

# Latitude lower and upper index
latli = np.argmin(np.abs(lats - extent[1]))
latui = np.argmin(np.abs(lats - extent[3]))

# Longitude lower and upper index
lonli = np.argmin(np.abs(lons - extent[0]))
lonui = np.argmin(np.abs(lons - extent[2]))

# Extract the Sea Surface Temperature
data = file.variables["analysed_sst"][:, latli:latui, lonli:lonui]
# data[data == 0] = np.nan

# Return a reshaped matrix
data = data.squeeze()

# Flip the y axis
data = np.flipud(data)

# Getting the file time and date
add_seconds = int(file.variables["time"][0])
date = datetime(1981, 1, 1, 12) + timedelta(seconds=add_seconds) - timedelta(days=1)
date_formated = date.strftime("%Y-%m-%d")
date_file = date.strftime("%Y%m%d%H%M")
# print(date_formated)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
if sector == "_SLV":
    # Configuration
    # colors = ["#0000a1", "#0000fe", "#0034ff", "#0356fc", "#0199fc", "#01daff", "#238e25", "#00a001", "#4bcc4e", "#62fe64", "#f5fe81", "#ffff02", "#ffb200", "#fd5106", "#ff2600", "#fb6a94", "#b52c64"]
    colors = [
        "#0053fe",
        "#006bfe",
        "#0083fe",
        "#0099fd",
        "#00affd",
        "#00c4fd",
        "#00d9fe",
        "#00eeff",
        "#02f800",
        "#00e800",
        "#00d400",
        "#00bf00",
        "#00a300",
        "#6fcd00",
        "#a9dc00",
        "#d7e600",
        "#e7d000",
        "#e7b100",
        "#e68a00",
        "#dc4d00",
    ]

    # colors = [
    #     "#DDFF00",
    #     "#DFF600",
    #     "#E2ED00",
    #     "#E4E400",
    #     "#E6DB00",
    #     "#E8D200",
    #     "#EBC900",
    #     "#EDC000",
    #     "#EFB600",
    #     "#F1AD00",
    #     "#F4A400",
    #     "#F69B00",
    #     "#F89200",
    #     "#FA8900",
    #     "#FD8000",
    #     "#FF7700",
    # ]
    cmap = matplotlib.colors.ListedColormap(colors)
    # cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    cmap.set_over("#2f0114")
    cmap.set_under("#32190d")
    # cmap = 'hot'
    # cmap = matplotlib.cm.get_cmap('hot_r')
    # cmap.set_over('#b52c64') #orig
    # cmap.set_under('#0000a1') #orig
    vmin = 23
    vmax = 33
    thick_interval = 1.0
    grid_interval = 1.0
else:
    # Configuration
    # colors = ["#0000a1", "#0000fe", "#0034ff", "#0356fc", "#0199fc", "#01daff", "#238e25", "#00a001", "#4bcc4e", "#62fe64", "#f5fe81", "#ffff02", "#ffb200", "#fd5106", "#ff2600", "#fb6a94", "#b52c64"]
    colors = [
        "#690011",
        "#540246",
        "#6f0066",
        "#8e0184",
        "#2d0798",
        "#4b2eac",
        "#6959c2",
        "#00009e",
        "#001ef9",
        "#0053fe",
        "#0089fe",
        "#00b1fd",
        "#00e5ff",
        "#02f800",
        "#00cf01",
        "#00a300",
        "#e7f000",
        "#e7b100",
        "#e67b00",
        "#dc4d00",
        "#c40f00",
        "#7d0000",
        "#bc602d",
        "#8f4824",
        "#5c2f17",
    ]
    # cmap = matplotlib.colors.ListedColormap(colors)
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    cmap.set_over("#2f0114")
    cmap.set_under("#32190d")
    # cmap = 'hot'
    # cmap = matplotlib.cm.get_cmap('hot_r')
    # cmap.set_over('#b52c64') #orig
    # cmap.set_under('#0000a1') #orig
    vmin = 0.0
    vmax = 40.0
    thick_interval = 5
    grid_interval = 5.0
prod_title = "NOAA Coral Reef Watch Daily 5km SST (Temperatura de Superficie del Mar)"
satellite = "MUL"
product = "SSTCOR"

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# Plot configuration
plot_config = {
    "resolution": resolution,
    "dpi": 150,
    "states_width": 0.5,
    "countries_width": 0.5,
    "continents_width": 0.5,
    "grid_color": "black",
    "grid_width": 0.3,
    "vmin": vmin,
    "vmax": vmax,
    "cmap": cmap,
    "title_text": prod_title + " ",
    "title_size": 8,
    "title_x_offset": int(sizex * 0.01),
    "title_y_offset": sizey - int(sizey * 0.016),
    "thick_interval": thick_interval,
    "cbar_labelsize": 7,
    "cbar_labelpad": -int(sizey * 0.0),
    "file_name_id_1": satellite,
    "file_name_id_2": product + sector,
}
if sector == "_SLV":
    states_color = "white"
    countries_color = "white"
    continents_color = "white"
else:
    states_color = "black"
    countries_color = "black"
    continents_color = "black"


# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
if sector == "_ATL":
    # Choose the plot size (width x height, in inches)
    fig = plt.figure(
        figsize=(1920 / float(plot_config["dpi"]), 785 / float(plot_config["dpi"])),
        dpi=plot_config["dpi"],
    )
elif sector == "_PAC":
    fig = plt.figure(
        figsize=(1920 / float(plot_config["dpi"]), 960 / float(plot_config["dpi"])),
        dpi=plot_config["dpi"],
    )
elif sector == "_ATN":
    fig = plt.figure(
        figsize=(1920 / float(plot_config["dpi"]), 791 / float(plot_config["dpi"])),
        dpi=plot_config["dpi"],
    )
else:
    fig = plt.figure(
        figsize=(1920 / float(plot_config["dpi"]), 1080 / float(plot_config["dpi"])),
        dpi=plot_config["dpi"],
    )

# Define the projection
proj = ccrs.PlateCarree()
# Use the PlateCarree projection in cartopy
ax = plt.axes([0, 0, 1, 1], projection=proj)
img_extent = [extent[0], extent[2], extent[1], extent[3]]
# Add a background image
# ax.stock_img()
if sector == "_SLV":
    fname = os.path.join(main_dir + "//Maps//", "Layout2.png")
    ax.imshow(
        imread(fname),
        origin="upper",
        transform=ccrs.PlateCarree(),
        extent=[-92.930, -83.803, 10.78, 15.750],
        zorder=1,
    )
else:
    fname = os.path.join(main_dir + "//Maps//", "eo_base_2020_clean_geo.png")
    ax.imshow(
        imread(fname),
        origin="upper",
        transform=ccrs.PlateCarree(),
        extent=[-180, 180, -90, 90],
        zorder=1,
    )

# date = datetime(int(year), int(month), int(day), int(hour))
# ax.add_feature(Nightshade(date, alpha=0.7), zorder=2)

# Plot the image
img = ax.imshow(
    data,
    vmin=plot_config["vmin"],
    vmax=plot_config["vmax"],
    origin="upper",
    extent=img_extent,
    cmap=plot_config["cmap"],
    zorder=2,
)

# To put colorbar inside picture
axins1 = inset_axes(ax, width="1%", height="25%", loc="upper right", borderpad=0.0)

if sector == "_SLV":
    # Add states and provinces
    shapefile = list(
        shpreader.Reader(
            main_dir + "//Shapefiles//El_Salvador_departamentos.shp"
        ).geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor=states_color,
        facecolor="none",
        linewidth=plot_config["states_width"],
        zorder=3,
    )

    # Add countries
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//Centro_America.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor=countries_color,
        facecolor="none",
        linewidth=plot_config["countries_width"],
        zorder=4,
    )
else:
    # Add countries
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//Centro_America.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor=countries_color,
        facecolor="none",
        linewidth=plot_config["countries_width"],
        zorder=3,
    )

    # Add continents
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//GSHHS_h_L1_clipped.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor=continents_color,
        facecolor="none",
        linewidth=plot_config["continents_width"],
        zorder=4,
    )

# Add ENSO regions 1-2,3,4,3-4
if sector == "_PAC":
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//ENSO_region_1-2.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor="blue",
        facecolor="none",
        linewidth=4 * plot_config["states_width"],
        zorder=3,
    )
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//ENSO_region_3.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor="red",
        facecolor="none",
        linewidth=4 * plot_config["states_width"],
        zorder=3,
    )
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//ENSO_region_4.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor="green",
        facecolor="none",
        linewidth=4 * plot_config["states_width"],
        zorder=3,
    )
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//ENSO_region_3-4.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor="dimgray",
        facecolor="gray",
        alpha=0.5,
        linewidth=4 * plot_config["states_width"],
        zorder=4,
    )
elif sector == "_ATN":
    # Add ENSO ATN
    shapefile = list(
        shpreader.Reader(main_dir + "//Shapefiles//ENSO_region_atn.shp").geometries()
    )
    ax.add_geometries(
        shapefile,
        ccrs.PlateCarree(),
        edgecolor="red",
        facecolor="none",
        linewidth=4 * plot_config["countries_width"],
        zorder=3,
    )

if sector == "_PAC":
    text = ax.text(
        -85,
        0.5,
        "1+2",
        color="black",
        horizontalalignment="center",
        fontsize="large",
        fontweight="bold",
        zorder=5,
    )
    # text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(
        -105,
        -5.5,
        "3",
        color="black",
        horizontalalignment="center",
        verticalalignment="top",
        fontsize="large",
        fontweight="bold",
        zorder=5,
    )
    # text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(
        -175,
        -5.5,
        "4",
        color="black",
        horizontalalignment="center",
        verticalalignment="top",
        fontsize="large",
        fontweight="bold",
        zorder=5,
    )
    # text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
    text = ax.text(
        -145,
        5.5,
        "3.4",
        color="black",
        horizontalalignment="center",
        fontsize="large",
        fontweight="bold",
        zorder=5,
    )
    # text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])
elif sector == "_ATN":
    text = ax.text(
        -45,
        20.5,
        "ATN",
        color="black",
        horizontalalignment="center",
        fontsize="large",
        fontweight="bold",
        zorder=5,
    )
    # text.set_path_effects([PathEffects.withStroke(linewidth=1.5, foreground='k')])

if sector == "_ATL":
    # Add a title
    plt.annotate(
        plot_config["title_text"] + " " + date_formated,
        xy=(0.015, 0.95),
        xycoords="figure fraction",
        fontsize=plot_config["title_size"],
        fontweight="bold",
        color="white",
        bbox=dict(boxstyle="round", fc=(0.0, 0.0, 0.0), ec=(1.0, 1.0, 1.0)),
        zorder=5,
    )
elif sector == "_ATN":
    plt.annotate(
        plot_config["title_text"] + " " + date_formated,
        xy=(0.015, 0.945),
        xycoords="figure fraction",
        fontsize=plot_config["title_size"],
        fontweight="bold",
        color="white",
        bbox=dict(boxstyle="round", fc=(0.0, 0.0, 0.0), ec=(1.0, 1.0, 1.0)),
        zorder=5,
    )
else:
    # Add a title
    plt.annotate(
        plot_config["title_text"] + " " + date_formated,
        xy=(0.015, 0.965),
        xycoords="figure fraction",
        fontsize=plot_config["title_size"],
        fontweight="bold",
        color="white",
        bbox=dict(boxstyle="round", fc=(0.0, 0.0, 0.0), ec=(1.0, 1.0, 1.0)),
        zorder=5,
    )


# Add coastlines, borders and gridlines
gl = ax.gridlines(
    color=plot_config["grid_color"],
    alpha=0.25,
    linestyle="--",
    linewidth=plot_config["grid_width"],
    xlocs=np.arange(-180, 180, grid_interval),
    ylocs=np.arange(-180, 180, grid_interval),
    draw_labels=True,
    zorder=6,
)
gl.bottom_labels = False
gl.right_labels = False
gl.xpadding = -2
gl.ypadding = -2
if sector == "_SLV":
    gl.xlabel_style = {"size": 6, "weight": "bold", "color": "white"}
    gl.ylabel_style = {"size": 6, "weight": "bold", "color": "white"}
else:
    gl.xlabel_style = {"size": 6, "weight": "bold", "color": "black"}
    gl.ylabel_style = {"size": 6, "weight": "bold", "color": "black"}


# Remove the outline border
ax.outline_patch.set_visible(False)

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

# Add logos / images to the plot
my_logo = plt.imread(main_dir + "//Logos//my_logo.webp")
if sector == "_ATL":
    newax = fig.add_axes(
        [0.908, 0.0, 0.10, 0.10], anchor="S", zorder=7
    )  # [left, bottom, width, height]. All quantities are in fractions of figure width and height.
else:
    newax = fig.add_axes(
        [0.9, 0.0, 0.10, 0.10], anchor="S", zorder=7
    )  # [left, bottom, width, height]. All quantities are in fractions of figure width and height.
newax.imshow(my_logo)
newax.axis("off")

# Add a colorbar
ticks = np.arange(
    plot_config["vmin"], plot_config["vmax"], plot_config["thick_interval"]
).tolist()
ticks = plot_config["thick_interval"] * np.round(
    np.true_divide(ticks, plot_config["thick_interval"])
)
ticks = ticks[1:]
cb = fig.colorbar(img, cax=axins1, orientation="vertical", ticks=ticks)
if sector == "_SLV":
    cb.set_label(
        label="[ °C ]", color="white", size=plot_config["title_size"], weight="bold"
    )
    cb.ax.tick_params(
        axis="y", width=0.5, colors="white", labelsize=plot_config["cbar_labelsize"]
    )
else:
    cb.set_label(
        label="[ °C ]", color="black", size=plot_config["title_size"], weight="bold"
    )
    cb.ax.tick_params(
        axis="y", width=0.5, colors="black", labelsize=plot_config["cbar_labelsize"]
    )
cb.outline.set_visible(True)
cb.ax.yaxis.set_tick_params(pad=plot_config["cbar_labelpad"])
cb.ax.yaxis.set_ticks_position("left")
cb.ax.yaxis.set_label_position("left")

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
product = product + sector

# Create the satellite output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Create the product output directory if it doesn't exist
out_dir = (sys.argv[7]) + satellite + "//" + product + "//"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Save the image
plt.savefig(
    out_dir
    + plot_config["file_name_id_1"]
    + "_"
    + plot_config["file_name_id_2"]
    + "_"
    + date_file
    + ".png",
    facecolor="black",
)  # , bbox_inches='tight', pad_inches=0, facecolor='black')

# Convert to webp

im = Image.open(
    out_dir
    + plot_config["file_name_id_1"]
    + "_"
    + plot_config["file_name_id_2"]
    + "_"
    + date_file
    + ".png"
)
im.save(
    out_dir
    + plot_config["file_name_id_1"]
    + "_"
    + plot_config["file_name_id_2"]
    + "_"
    + date_file
    + ".webp",
    format="WebP",
    lossless=True,
)
im.close()

# Update the animation
nfiles = 25
update(satellite, product, nfiles, sys.argv[7], sys.argv[8], sector)

# Delete aux files
os.remove(
    out_dir
    + plot_config["file_name_id_1"]
    + "_"
    + plot_config["file_name_id_2"]
    + "_"
    + date_file
    + ".png"
)

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
# Put the processed file on the log
import datetime

with open(
    main_dir + "//Logs//gnc_log_" + str(datetime.datetime.now())[0:10] + ".txt", "a"
) as log:
    log.write(str(datetime.datetime.now()))
    log.write("\n")
    log.write(path + "\n")
    log.write("\n")
# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

print("Total processing time:", round((t.time() - start_time), 2), "seconds.")
