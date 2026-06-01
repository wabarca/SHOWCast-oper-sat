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
__copyright__ = (
    "Copyright (C) 2021 - INPE - NATIONAL INSTITUTE FOR SPACE RESEARCH - BRAZIL"
)
__credits__ = ["Diego Souza"]
__license__ = "GPL"
__version__ = "2.4.0 SV edition"
__maintainer__ = "Diego Souza"
__email__ = "diego.souza@inpe.br"
__status__ = "Production"

# ------------------------------------------------------------------------------------------------------

# Required Libraries
import glob  # Unix style pathname pattern expansion
import os  # Miscellaneous operating system interfaces
import sys  # Import the "system specific parameters and functions" module
from os.path import (
    dirname,
    abspath,
)  # Return a normalized absolutized version of the pathname path
import datetime  # Basic Date and Time types
import time as t  # Time access and conversion

# ------------------------------------------------------------------------------------------------------

start = t.time()  # Start the time counter

# Python environment
python_env = sys.argv[1]

# Ingestion directory
ingest_dir = sys.argv[2]

# SHOWCast directory:
showcast_dir = dirname(dirname(abspath(__file__)))

# SHOWCast process number
showcast_process = int(sys.argv[3])

# SHOWCast visualization directory
vis_dir = sys.argv[4]

# Variable that will store the desired products
products = []

# ------------------------------------------------------------------------------------------------------
# GOES-19 - ABI INDIVIDUAL BANDS - EL SALVADOR
# ------------------------------------------------------------------------------------------------------
g16_band02_slv = True  # GOES-19 L2 CMI - Band 02 - USER SECTOR

g16_band02_slv_process = 1
g16_band02_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_band02_slv_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_band02_slv_max_files = 5
g16_band02_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band02_slv_resolution = 0.5
g16_band02_slv_config = "_SLV"
g16_band02_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band02_slv_output = showcast_dir + "//Output//"

products.append("g16_band02_slv")
# ------------------------------------------------------------------------------------------------------
g16_band13_slv = True  # GOES-19 L2 CMI - Band 13 - USER SECTOR

g16_band13_slv_process = 1
g16_band13_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_band13_slv_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_band13_slv_max_files = 5
g16_band13_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band13_slv_resolution = 2
g16_band13_slv_config = "_SLV"
g16_band13_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band13_slv_output = showcast_dir + "//Output//"

products.append("g16_band13_slv")
# ------------------------------------------------------------------------------------------------------
g16_band08_slv = True  # GOES-19 L2 CMI - Band 08 - USER SECTOR

g16_band08_slv_process = 1
g16_band08_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_band08_slv_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_band08_slv_max_files = 5
g16_band08_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band08_slv_resolution = 2
g16_band08_slv_config = "_SLV"
g16_band08_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band08_slv_output = showcast_dir + "//Output//"

products.append("g16_band08_slv")
# ------------------------------------------------------------------------------------------------------
g16_band09_slv = True  # GOES-19 L2 CMI - Band 09 - USER SECTOR

g16_band09_slv_process = 1
g16_band09_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_band09_slv_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_band09_slv_max_files = 5
g16_band09_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band09_slv_resolution = 2
g16_band09_slv_config = "_SLV"
g16_band09_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band09_slv_output = showcast_dir + "//Output//"

products.append("g16_band09_slv")
# ------------------------------------------------------------------------------------------------------
g16_band10_slv = True  # GOES-19 L2 CMI - Band 10 - USER SECTOR

g16_band10_slv_process = 1
g16_band10_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_band10_slv_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_band10_slv_max_files = 5
g16_band10_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band10_slv_resolution = 2
g16_band10_slv_config = "_SLV"
g16_band10_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band10_slv_output = showcast_dir + "//Output//"

products.append("g16_band10_slv")
# ------------------------------------------------------------------------------------------------------
g16_band04_slv = True  # GOES-19 L2 CMI - Band 04 - USER SECTOR

g16_band04_slv_process = 1
g16_band04_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band04//"
g16_band04_slv_identifier = "*L2-CMIPF-M*C04_G19*.nc"
g16_band04_slv_max_files = 5
g16_band04_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band04_slv_resolution = 2
g16_band04_slv_config = "_SLV"
g16_band04_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band04_slv_output = showcast_dir + "//Output//"

products.append("g16_band04_slv")
# ------------------------------------------------------------------------------------------------------
g16_band12_slv = True  # GOES-19 L2 CMI - Band 12 - USER SECTOR

g16_band12_slv_process = 1
g16_band12_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band12//"
g16_band12_slv_identifier = "*L2-CMIPF-M*C12_G19*.nc"
g16_band12_slv_max_files = 5
g16_band12_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band12_slv_resolution = 2
g16_band12_slv_config = "_SLV"
g16_band12_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band12_slv_output = showcast_dir + "//Output//"

products.append("g16_band12_slv")
# ------------------------------------------------------------------------------------------------------
g16_band14_slv = True  # GOES-19 L2 CMI - Band 14 - USER SECTOR

g16_band14_slv_process = 1
g16_band14_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band14//"
g16_band14_slv_identifier = "*L2-CMIPF-M*C14_G19*.nc"
g16_band14_slv_max_files = 5
g16_band14_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_band14_slv_resolution = 2
g16_band14_slv_config = "_SLV"
g16_band14_slv_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band14_slv_output = showcast_dir + "//Output//"

products.append("g16_band14_slv")
# ------------------------------------------------------------------------------------------------------
# GOES-19 - ABI INDIVIDUAL BANDS - CENTRAL AMERICA
# ------------------------------------------------------------------------------------------------------
g16_band02_cam = True  # GOES-19 L2 CMI - Band 02 - USER SECTOR

g16_band02_cam_process = 2
g16_band02_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_band02_cam_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_band02_cam_max_files = 5
g16_band02_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band02_cam_resolution = 0.5
g16_band02_cam_config = "_CAM"
g16_band02_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band02_cam_output = showcast_dir + "//Output//"

products.append("g16_band02_cam")
# ------------------------------------------------------------------------------------------------------
g16_band13_cam = True  # GOES-19 L2 CMI - Band 13 - USER SECTOR

g16_band13_cam_process = 2
g16_band13_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_band13_cam_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_band13_cam_max_files = 5
g16_band13_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band13_cam_resolution = 2
g16_band13_cam_config = "_CAM"
g16_band13_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band13_cam_output = showcast_dir + "//Output//"

products.append("g16_band13_cam")
# ------------------------------------------------------------------------------------------------------
g16_band08_cam = True  # GOES-19 L2 CMI - Band 08 - USER SECTOR

g16_band08_cam_process = 2
g16_band08_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_band08_cam_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_band08_cam_max_files = 5
g16_band08_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band08_cam_resolution = 2
g16_band08_cam_config = "_CAM"
g16_band08_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band08_cam_output = showcast_dir + "//Output//"

products.append("g16_band08_cam")
# ------------------------------------------------------------------------------------------------------
g16_band09_cam = True  # GOES-19 L2 CMI - Band 09 - USER SECTOR

g16_band09_cam_process = 2
g16_band09_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_band09_cam_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_band09_cam_max_files = 5
g16_band09_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band09_cam_resolution = 2
g16_band09_cam_config = "_CAM"
g16_band09_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band09_cam_output = showcast_dir + "//Output//"

products.append("g16_band09_cam")
# ------------------------------------------------------------------------------------------------------
g16_band10_cam = True  # GOES-19 L2 CMI - Band 10 - USER SECTOR

g16_band10_cam_process = 2
g16_band10_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_band10_cam_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_band10_cam_max_files = 5
g16_band10_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band10_cam_resolution = 2
g16_band10_cam_config = "_CAM"
g16_band10_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band10_cam_output = showcast_dir + "//Output//"

products.append("g16_band10_cam")
# ------------------------------------------------------------------------------------------------------
g16_band04_cam = True  # GOES-19 L2 CMI - Band 04 - USER SECTOR

g16_band04_cam_process = 2
g16_band04_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band04//"
g16_band04_cam_identifier = "*L2-CMIPF-M*C04_G19*.nc"
g16_band04_cam_max_files = 5
g16_band04_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band04_cam_resolution = 2
g16_band04_cam_config = "_CAM"
g16_band04_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band04_cam_output = showcast_dir + "//Output//"

products.append("g16_band04_cam")
# ------------------------------------------------------------------------------------------------------
g16_band12_cam = True  # GOES-19 L2 CMI - Band 12 - USER SECTOR

g16_band12_cam_process = 2
g16_band12_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band12//"
g16_band12_cam_identifier = "*L2-CMIPF-M*C12_G19*.nc"
g16_band12_cam_max_files = 5
g16_band12_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band12_cam_resolution = 2
g16_band12_cam_config = "_CAM"
g16_band12_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band12_cam_output = showcast_dir + "//Output//"

products.append("g16_band12_cam")
# ------------------------------------------------------------------------------------------------------
g16_band14_cam = True  # GOES-19 L2 CMI - Band 14 - USER SECTOR

g16_band14_cam_process = 2
g16_band14_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band14//"
g16_band14_cam_identifier = "*L2-CMIPF-M*C14_G19*.nc"
g16_band14_cam_max_files = 5
g16_band14_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_band14_cam_resolution = 2
g16_band14_cam_config = "_CAM"
g16_band14_cam_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band14_cam_output = showcast_dir + "//Output//"

products.append("g16_band14_cam")
# ------------------------------------------------------------------------------------------------------
# GOES-19 - ABI INDIVIDUAL BANDS - CENTRAL AMERICA
# ------------------------------------------------------------------------------------------------------
g16_band02_atl = True  # GOES-19 L2 CMI - Band 02 - USER SECTOR

g16_band02_atl_process = 3
g16_band02_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_band02_atl_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_band02_atl_max_files = 5
g16_band02_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band02_atl_resolution = 1
g16_band02_atl_config = "_ATL"
g16_band02_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band02_atl_output = showcast_dir + "//Output//"

products.append("g16_band02_atl")
# ------------------------------------------------------------------------------------------------------
g16_band13_atl = True  # GOES-19 L2 CMI - Band 13 - USER SECTOR

g16_band13_atl_process = 3
g16_band13_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_band13_atl_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_band13_atl_max_files = 5
g16_band13_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band13_atl_resolution = 2
g16_band13_atl_config = "_ATL"
g16_band13_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band13_atl_output = showcast_dir + "//Output//"

products.append("g16_band13_atl")
# ------------------------------------------------------------------------------------------------------
g16_band08_atl = True  # GOES-19 L2 CMI - Band 08 - USER SECTOR

g16_band08_atl_process = 3
g16_band08_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_band08_atl_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_band08_atl_max_files = 5
g16_band08_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band08_atl_resolution = 2
g16_band08_atl_config = "_ATL"
g16_band08_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band08_atl_output = showcast_dir + "//Output//"

products.append("g16_band08_atl")
# ------------------------------------------------------------------------------------------------------
g16_band09_atl = True  # GOES-19 L2 CMI - Band 09 - USER SECTOR

g16_band09_atl_process = 3
g16_band09_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_band09_atl_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_band09_atl_max_files = 5
g16_band09_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band09_atl_resolution = 2
g16_band09_atl_config = "_ATL"
g16_band09_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band09_atl_output = showcast_dir + "//Output//"

products.append("g16_band09_atl")
# ------------------------------------------------------------------------------------------------------
g16_band10_atl = True  # GOES-19 L2 CMI - Band 10 - USER SECTOR

g16_band10_atl_process = 3
g16_band10_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_band10_atl_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_band10_atl_max_files = 5
g16_band10_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band10_atl_resolution = 2
g16_band10_atl_config = "_ATL"
g16_band10_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band10_atl_output = showcast_dir + "//Output//"

products.append("g16_band10_atl")
# ------------------------------------------------------------------------------------------------------
g16_band04_atl = True  # GOES-19 L2 CMI - Band 04 - USER SECTOR

g16_band04_atl_process = 3
g16_band04_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band04//"
g16_band04_atl_identifier = "*L2-CMIPF-M*C04_G19*.nc"
g16_band04_atl_max_files = 5
g16_band04_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band04_atl_resolution = 2
g16_band04_atl_config = "_ATL"
g16_band04_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band04_atl_output = showcast_dir + "//Output//"

products.append("g16_band04_atl")
# ------------------------------------------------------------------------------------------------------
g16_band12_atl = True  # GOES-19 L2 CMI - Band 12 - USER SECTOR

g16_band12_atl_process = 3
g16_band12_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band12//"
g16_band12_atl_identifier = "*L2-CMIPF-M*C12_G19*.nc"
g16_band12_atl_max_files = 5
g16_band12_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band12_atl_resolution = 2
g16_band12_atl_config = "_ATL"
g16_band12_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band12_atl_output = showcast_dir + "//Output//"

products.append("g16_band12_atl")
# ------------------------------------------------------------------------------------------------------
g16_band14_atl = True  # GOES-19 L2 CMI - Band 14 - USER SECTOR

g16_band14_atl_process = 3
g16_band14_atl_directory = ingest_dir + "GOES-R-CMI-Imagery//Band14//"
g16_band14_atl_identifier = "*L2-CMIPF-M*C14_G19*.nc"
g16_band14_atl_max_files = 5
g16_band14_atl_extent = [-120, 0.0, -10.0, 45.0]
g16_band14_atl_resolution = 2
g16_band14_atl_config = "_ATL"
g16_band14_atl_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band14_atl_output = showcast_dir + "//Output//"

products.append("g16_band14_atl")

# ------------------------------------------------------------------------------------------------------
# GOES-19 - ABI INDIVIDUAL BANDS - EL SALVADOR/GUATEMALA/HONDURAS
# ------------------------------------------------------------------------------------------------------
g16_band02_egh = True  # GOES-19 L2 CMI - Band 02 - USER SECTOR

g16_band02_egh_process = 4
g16_band02_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_band02_egh_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_band02_egh_max_files = 5
g16_band02_egh_extent = [-93, 11, -82.333, 17]
g16_band02_egh_resolution = 0.5
g16_band02_egh_config = "_EGH"
g16_band02_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band02_egh_output = showcast_dir + "//Output//"

products.append("g16_band02_egh")
# ------------------------------------------------------------------------------------------------------
g16_band13_egh = True  # GOES-19 L2 CMI - Band 13 - USER SECTOR

g16_band13_egh_process = 4
g16_band13_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_band13_egh_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_band13_egh_max_files = 5
g16_band13_egh_extent = [-93, 11, -82.333, 17]
g16_band13_egh_resolution = 2
g16_band13_egh_config = "_EGH"
g16_band13_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band13_egh_output = showcast_dir + "//Output//"

products.append("g16_band13_egh")
# ------------------------------------------------------------------------------------------------------
g16_band08_egh = True  # GOES-19 L2 CMI - Band 08 - USER SECTOR

g16_band08_egh_process = 4
g16_band08_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_band08_egh_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_band08_egh_max_files = 5
g16_band08_egh_extent = [-93, 11, -82.333, 17]
g16_band08_egh_resolution = 2
g16_band08_egh_config = "_EGH"
g16_band08_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band08_egh_output = showcast_dir + "//Output//"

products.append("g16_band08_egh")
# ------------------------------------------------------------------------------------------------------
g16_band09_egh = True  # GOES-19 L2 CMI - Band 09 - USER SECTOR

g16_band09_egh_process = 4
g16_band09_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_band09_egh_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_band09_egh_max_files = 5
g16_band09_egh_extent = [-93, 11, -82.333, 17]
g16_band09_egh_resolution = 2
g16_band09_egh_config = "_EGH"
g16_band09_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band09_egh_output = showcast_dir + "//Output//"

products.append("g16_band09_egh")
# ------------------------------------------------------------------------------------------------------
g16_band10_egh = True  # GOES-19 L2 CMI - Band 10 - USER SECTOR

g16_band10_egh_process = 4
g16_band10_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_band10_egh_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_band10_egh_max_files = 5
g16_band10_egh_extent = [-93, 11, -82.333, 17]
g16_band10_egh_resolution = 2
g16_band10_egh_config = "_EGH"
g16_band10_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band10_egh_output = showcast_dir + "//Output//"

products.append("g16_band10_egh")
# ------------------------------------------------------------------------------------------------------
g16_band04_egh = True  # GOES-19 L2 CMI - Band 04 - USER SECTOR

g16_band04_egh_process = 4
g16_band04_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band04//"
g16_band04_egh_identifier = "*L2-CMIPF-M*C04_G19*.nc"
g16_band04_egh_max_files = 5
g16_band04_egh_extent = [-93, 11, -82.333, 17]
g16_band04_egh_resolution = 2
g16_band04_egh_config = "_EGH"
g16_band04_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band04_egh_output = showcast_dir + "//Output//"

products.append("g16_band04_egh")
# ------------------------------------------------------------------------------------------------------
g16_band12_egh = True  # GOES-19 L2 CMI - Band 12 - USER SECTOR

g16_band12_egh_process = 4
g16_band12_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band12//"
g16_band12_egh_identifier = "*L2-CMIPF-M*C12_G19*.nc"
g16_band12_egh_max_files = 5
g16_band12_egh_extent = [-93, 11, -82.333, 17]
g16_band12_egh_resolution = 2
g16_band12_egh_config = "_EGH"
g16_band12_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band12_egh_output = showcast_dir + "//Output//"

products.append("g16_band12_egh")
# ------------------------------------------------------------------------------------------------------
g16_band14_egh = True  # GOES-19 L2 CMI - Band 14 - USER SECTOR

g16_band14_egh_process = 4
g16_band14_egh_directory = ingest_dir + "GOES-R-CMI-Imagery//Band14//"
g16_band14_egh_identifier = "*L2-CMIPF-M*C14_G19*.nc"
g16_band14_egh_max_files = 5
g16_band14_egh_extent = [-93, 11, -82.333, 17]
g16_band14_egh_resolution = 2
g16_band14_egh_config = "_EGH"
g16_band14_egh_script = showcast_dir + "//Scripts//process_g1X_bands_sec.py"
g16_band14_egh_output = showcast_dir + "//Output//"

products.append("g16_band14_egh")

# ------------------------------------------------------------------------------------------------------
# RGB's created on the station - El Salvador
# ------------------------------------------------------------------------------------------------------
g16_24hrgb_slv = True  # GOES-19 24h Microphysics RGB - USER SECTOR

g16_24hrgb_slv_process = 5
g16_24hrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_24hrgb_slv_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_24hrgb_slv_max_files = 5
g16_24hrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_24hrgb_slv_resolution = 2
g16_24hrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_24hrgb_slv_config = "_SLV24H"
g16_24hrgb_slv_script = showcast_dir + "//Scripts//process_g16_24hrgb_sec.py"
g16_24hrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_24hrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_armrgb_slv = True  # GOES-19 Airmass RGB - USER SECTOR

g16_armrgb_slv_process = 5
g16_armrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_armrgb_slv_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_armrgb_slv_max_files = 5
g16_armrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_armrgb_slv_resolution = 2
g16_armrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_armrgb_slv_config = "_SLVARM"
g16_armrgb_slv_script = showcast_dir + "//Scripts//process_g16_armrgb_sec.py"
g16_armrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_armrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_ashrgb_slv = True  # GOES-19 Ash RGB - USER SECTOR

g16_ashrgb_slv_process = 5
g16_ashrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_ashrgb_slv_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_ashrgb_slv_max_files = 5
g16_ashrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_ashrgb_slv_resolution = 2
g16_ashrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_ashrgb_slv_config = "_SLVASH"
g16_ashrgb_slv_script = showcast_dir + "//Scripts//process_g16_ashrgb_sec.py"
g16_ashrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_ashrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_clprgb_slv = True  # GOES-19 Cloud Phase RGB - USER SECTOR

g16_clprgb_slv_process = 5
g16_clprgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band05//"
g16_clprgb_slv_identifier = "*L2-CMIPF-M*C05_G19*.nc"
g16_clprgb_slv_max_files = 5
g16_clprgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_clprgb_slv_resolution = 2
g16_clprgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_clprgb_slv_config = "_SLVCLP"
g16_clprgb_slv_script = showcast_dir + "//Scripts//process_g16_clprgb_sec.py"
g16_clprgb_slv_output = showcast_dir + "//Output//"

products.append("g16_clprgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dccrgb_slv = True  # GOES-19 Day Cloud Convection RGB - USER SECTOR

g16_dccrgb_slv_process = 5
g16_dccrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_dccrgb_slv_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_dccrgb_slv_max_files = 5
g16_dccrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dccrgb_slv_resolution = 2
g16_dccrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dccrgb_slv_config = "_SLVDCC"
g16_dccrgb_slv_script = showcast_dir + "//Scripts//process_g16_dccrgb_sec.py"
g16_dccrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dccrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dcprgb_slv = True  # GOES-19 Day Cloud Phase RGB - USER SECTOR

g16_dcprgb_slv_process = 5
g16_dcprgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_dcprgb_slv_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_dcprgb_slv_max_files = 5
g16_dcprgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dcprgb_slv_resolution = 2
g16_dcprgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dcprgb_slv_config = "_SLVDCP"
g16_dcprgb_slv_script = showcast_dir + "//Scripts//process_g16_dcprgb_sec.py"
g16_dcprgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dcprgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_conrgb_slv = True  # GOES-19 Convection RGB - USER SECTOR

g16_conrgb_slv_process = 5
g16_conrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_conrgb_slv_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_conrgb_slv_max_files = 5
g16_conrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_conrgb_slv_resolution = 2
g16_conrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_conrgb_slv_config = "_SLVCON"
g16_conrgb_slv_script = showcast_dir + "//Scripts//process_g16_conrgb_sec.py"
g16_conrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_conrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dlcrgb_slv = False  # GOES-19 Day Land Cloud RGB - USER SECTOR

g16_dlcrgb_slv_process = 5
g16_dlcrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band05//"
g16_dlcrgb_slv_identifier = "*L2-CMIPF-M*C05_G19*.nc"
g16_dlcrgb_slv_max_files = 5
g16_dlcrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dlcrgb_slv_resolution = 2
g16_dlcrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dlcrgb_slv_config = "_SLVDLC"
g16_dlcrgb_slv_script = showcast_dir + "//Scripts//process_g16_dlcrgb_sec.py"
g16_dlcrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dlcrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dlfrgb_slv = False  # GOES-19 Day Land Cloud Fire RGB - USER SECTOR

g16_dlfrgb_slv_process = 5
g16_dlfrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_dlfrgb_slv_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_dlfrgb_slv_max_files = 5
g16_dlfrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dlfrgb_slv_resolution = 2
g16_dlfrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dlfrgb_slv_config = "_SLVDLF"
g16_dlfrgb_slv_script = showcast_dir + "//Scripts//process_g16_dlfrgb_sec.py"
g16_dlfrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dlfrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dmprgb_slv = True  # GOES-19 Day Microphysics RGB - USER SECTOR

g16_dmprgb_slv_process = 5
g16_dmprgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_dmprgb_slv_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_dmprgb_slv_max_files = 5
g16_dmprgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dmprgb_slv_resolution = 2
g16_dmprgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dmprgb_slv_config = "_SLVDMP"
g16_dmprgb_slv_script = showcast_dir + "//Scripts//process_g16_dmprgb_sec.py"
g16_dmprgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dmprgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dsfrgb_slv = True  # GOES-19 Day Snow Fog RGB - USER SECTOR

g16_dsfrgb_slv_process = 5
g16_dsfrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band03//"
g16_dsfrgb_slv_identifier = "*L2-CMIPF-M*C03_G19*.nc"
g16_dsfrgb_slv_max_files = 5
g16_dsfrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dsfrgb_slv_resolution = 2
g16_dsfrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dsfrgb_slv_config = "_SLVDSF"
g16_dsfrgb_slv_script = showcast_dir + "//Scripts//process_g16_dsfrgb_sec.py"
g16_dsfrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dsfrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dwvrgb_slv = True  # GOES-19 Differential Water Vapor RGB - USER SECTOR

g16_dwvrgb_slv_process = 5
g16_dwvrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_dwvrgb_slv_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_dwvrgb_slv_max_files = 5
g16_dwvrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dwvrgb_slv_resolution = 2
g16_dwvrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dwvrgb_slv_config = "_SLVDWV"
g16_dwvrgb_slv_script = showcast_dir + "//Scripts//process_g16_dwvrgb_sec.py"
g16_dwvrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dwvrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_dstrgb_slv = True  # GOES-19 Dust RGB - USER SECTOR

g16_dstrgb_slv_process = 5
g16_dstrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_dstrgb_slv_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_dstrgb_slv_max_files = 5
g16_dstrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_dstrgb_slv_resolution = 2
g16_dstrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_dstrgb_slv_config = "_SLVDST"
g16_dstrgb_slv_script = showcast_dir + "//Scripts//process_g16_dstrgb_sec.py"
g16_dstrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_dstrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_fcorgb_slv = False  # GOES-19 False Color RGB - USER SECTOR

g16_fcorgb_slv_process = 5
g16_fcorgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_fcorgb_slv_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_fcorgb_slv_max_files = 5
g16_fcorgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_fcorgb_slv_resolution = 1
g16_fcorgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_fcorgb_slv_config = "_SLVFCO"
g16_fcorgb_slv_script = showcast_dir + "//Scripts//process_g16_fcorgb_sec.py"
g16_fcorgb_slv_output = showcast_dir + "//Output//"

products.append("g16_fcorgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_ftprgb_slv = True  # GOES-19 Fire Temperature RGB - USER SECTOR

g16_ftprgb_slv_process = 5
g16_ftprgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_ftprgb_slv_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_ftprgb_slv_max_files = 5
g16_ftprgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_ftprgb_slv_resolution = 2
g16_ftprgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_ftprgb_slv_config = "_SLVFTP"
g16_ftprgb_slv_script = showcast_dir + "//Scripts//process_g16_ftprgb_sec.py"
g16_ftprgb_slv_output = showcast_dir + "//Output//"

products.append("g16_ftprgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_ntcrgb_slv = False  # GOES-19 Natural True Color RGB - USER SECTOR

g16_ntcrgb_slv_process = 5
g16_ntcrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_ntcrgb_slv_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_ntcrgb_slv_max_files = 5
g16_ntcrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_ntcrgb_slv_resolution = 1
g16_ntcrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_ntcrgb_slv_config = "_SLVNTC"
g16_ntcrgb_slv_script = showcast_dir + "//Scripts//process_g16_ntcrgb_sec.py"
g16_ntcrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_ntcrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_nmprgb_slv = True  # GOES-19 Day Cloud Phase RGB - USER SECTOR

g16_nmprgb_slv_process = 5
g16_nmprgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_nmprgb_slv_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_nmprgb_slv_max_files = 5
g16_nmprgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_nmprgb_slv_resolution = 2
g16_nmprgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_nmprgb_slv_config = "_SLVNMP"
g16_nmprgb_slv_script = showcast_dir + "//Scripts//process_g16_nmprgb_sec.py"
g16_nmprgb_slv_output = showcast_dir + "//Output//"

products.append("g16_nmprgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_swvrgb_slv = True  # GOES-19 Simple Water Vapor RGB - USER SECTOR

g16_swvrgb_slv_process = 5
g16_swvrgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_swvrgb_slv_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_swvrgb_slv_max_files = 5
g16_swvrgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_swvrgb_slv_resolution = 2
g16_swvrgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_swvrgb_slv_config = "_SLVSWV"
g16_swvrgb_slv_script = showcast_dir + "//Scripts//process_g16_swvrgb_sec.py"
g16_swvrgb_slv_output = showcast_dir + "//Output//"

products.append("g16_swvrgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_so2rgb_slv = True  # GOES-19 SO2 RGB - USER SECTOR

g16_so2rgb_slv_process = 5
g16_so2rgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_so2rgb_slv_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_so2rgb_slv_max_files = 5
g16_so2rgb_slv_resolution = 2
g16_so2rgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_so2rgb_slv_config = "_SLVSO2"
g16_so2rgb_slv_script = showcast_dir + "//Scripts//process_g16_so2rgb_sec.py"
g16_so2rgb_slv_output = showcast_dir + "//Output//"

products.append("g16_so2rgb_slv")
# ------------------------------------------------------------------------------------------------------
g16_trurgb_slv = True  # GOES-19 True Color RGB - USER SECTOR

g16_trurgb_slv_process = 5
g16_trurgb_slv_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_trurgb_slv_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_trurgb_slv_max_files = 5
g16_trurgb_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_trurgb_slv_resolution = 1
g16_trurgb_slv_interval = "00,10,20,30,40,50"  # Processing interval
g16_trurgb_slv_config = "_SLVTRU"
g16_trurgb_slv_script = showcast_dir + "//Scripts//process_g16_trurgb_sec.py"
g16_trurgb_slv_output = showcast_dir + "//Output//"

products.append("g16_trurgb_slv")
# ------------------------------------------------------------------------------------------------------
# RGB's created on the station - Central America
# ------------------------------------------------------------------------------------------------------
g16_24hrgb_cam = True  # GOES-19 24h Microphysics RGB - USER SECTOR

g16_24hrgb_cam_process = 6
g16_24hrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_24hrgb_cam_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_24hrgb_cam_max_files = 5
g16_24hrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_24hrgb_cam_resolution = 2
g16_24hrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_24hrgb_cam_config = "_CAM24H"
g16_24hrgb_cam_script = showcast_dir + "//Scripts//process_g16_24hrgb_sec.py"
g16_24hrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_24hrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_armrgb_cam = True  # GOES-19 Airmass RGB - USER SECTOR

g16_armrgb_cam_process = 6
g16_armrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_armrgb_cam_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_armrgb_cam_max_files = 5
g16_armrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_armrgb_cam_resolution = 2
g16_armrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_armrgb_cam_config = "_CAMARM"
g16_armrgb_cam_script = showcast_dir + "//Scripts//process_g16_armrgb_sec.py"
g16_armrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_armrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_ashrgb_cam = True  # GOES-19 Ash RGB - USER SECTOR

g16_ashrgb_cam_process = 6
g16_ashrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_ashrgb_cam_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_ashrgb_cam_max_files = 5
g16_ashrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_ashrgb_cam_resolution = 2
g16_ashrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_ashrgb_cam_config = "_CAMASH"
g16_ashrgb_cam_script = showcast_dir + "//Scripts//process_g16_ashrgb_sec.py"
g16_ashrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_ashrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_clprgb_cam = True  # GOES-19 Cloud Phase RGB - USER SECTOR

g16_clprgb_cam_process = 6
g16_clprgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band05//"
g16_clprgb_cam_identifier = "*L2-CMIPF-M*C05_G19*.nc"
g16_clprgb_cam_max_files = 5
g16_clprgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_clprgb_cam_resolution = 2
g16_clprgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_clprgb_cam_config = "_CAMCLP"
g16_clprgb_cam_script = showcast_dir + "//Scripts//process_g16_clprgb_sec.py"
g16_clprgb_cam_output = showcast_dir + "//Output//"

products.append("g16_clprgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dccrgb_cam = True  # GOES-19 Day Cloud Convection RGB - USER SECTOR

g16_dccrgb_cam_process = 6
g16_dccrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_dccrgb_cam_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_dccrgb_cam_max_files = 5
g16_dccrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dccrgb_cam_resolution = 2
g16_dccrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dccrgb_cam_config = "_CAMDCC"
g16_dccrgb_cam_script = showcast_dir + "//Scripts//process_g16_dccrgb_sec.py"
g16_dccrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dccrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dcprgb_cam = True  # GOES-19 Day Cloud Phase RGB - USER SECTOR

g16_dcprgb_cam_process = 6
g16_dcprgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_dcprgb_cam_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_dcprgb_cam_max_files = 5
g16_dcprgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dcprgb_cam_resolution = 2
g16_dcprgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dcprgb_cam_config = "_CAMDCP"
g16_dcprgb_cam_script = showcast_dir + "//Scripts//process_g16_dcprgb_sec.py"
g16_dcprgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dcprgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_conrgb_cam = True  # GOES-19 Convection RGB - USER SECTOR

g16_conrgb_cam_process = 6
g16_conrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band08//"
g16_conrgb_cam_identifier = "*L2-CMIPF-M*C08_G19*.nc"
g16_conrgb_cam_max_files = 5
g16_conrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_conrgb_cam_resolution = 2
g16_conrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_conrgb_cam_config = "_CAMCON"
g16_conrgb_cam_script = showcast_dir + "//Scripts//process_g16_conrgb_sec.py"
g16_conrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_conrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dlcrgb_cam = False  # GOES-19 Day Land Cloud RGB - USER SECTOR

g16_dlcrgb_cam_process = 6
g16_dlcrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band05//"
g16_dlcrgb_cam_identifier = "*L2-CMIPF-M*C05_G19*.nc"
g16_dlcrgb_cam_max_files = 5
g16_dlcrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dlcrgb_cam_resolution = 2
g16_dlcrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dlcrgb_cam_config = "_CAMDLC"
g16_dlcrgb_cam_script = showcast_dir + "//Scripts//process_g16_dlcrgb_sec.py"
g16_dlcrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dlcrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dlfrgb_cam = False  # GOES-19 Day Land Cloud Fire RGB - USER SECTOR

g16_dlfrgb_cam_process = 6
g16_dlfrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_dlfrgb_cam_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_dlfrgb_cam_max_files = 5
g16_dlfrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dlfrgb_cam_resolution = 2
g16_dlfrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dlfrgb_cam_config = "_CAMDLF"
g16_dlfrgb_cam_script = showcast_dir + "//Scripts//process_g16_dlfrgb_sec.py"
g16_dlfrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dlfrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dmprgb_cam = True  # GOES-19 Day Microphysics RGB - USER SECTOR

g16_dmprgb_cam_process = 6
g16_dmprgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_dmprgb_cam_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_dmprgb_cam_max_files = 5
g16_dmprgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dmprgb_cam_resolution = 2
g16_dmprgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dmprgb_cam_config = "_CAMDMP"
g16_dmprgb_cam_script = showcast_dir + "//Scripts//process_g16_dmprgb_sec.py"
g16_dmprgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dmprgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dsfrgb_cam = True  # GOES-19 Day Snow Fog RGB - USER SECTOR

g16_dsfrgb_cam_process = 6
g16_dsfrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band03//"
g16_dsfrgb_cam_identifier = "*L2-CMIPF-M*C03_G19*.nc"
g16_dsfrgb_cam_max_files = 5
g16_dsfrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dsfrgb_cam_resolution = 2
g16_dsfrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dsfrgb_cam_config = "_CAMDSF"
g16_dsfrgb_cam_script = showcast_dir + "//Scripts//process_g16_dsfrgb_sec.py"
g16_dsfrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dsfrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dwvrgb_cam = True  # GOES-19 Differential Water Vapor RGB - USER SECTOR

g16_dwvrgb_cam_process = 6
g16_dwvrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_dwvrgb_cam_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_dwvrgb_cam_max_files = 5
g16_dwvrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dwvrgb_cam_resolution = 2
g16_dwvrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dwvrgb_cam_config = "_CAMDWV"
g16_dwvrgb_cam_script = showcast_dir + "//Scripts//process_g16_dwvrgb_sec.py"
g16_dwvrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dwvrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_dstrgb_cam = True  # GOES-19 Dust RGB - USER SECTOR

g16_dstrgb_cam_process = 6
g16_dstrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_dstrgb_cam_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_dstrgb_cam_max_files = 5
g16_dstrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dstrgb_cam_resolution = 2
g16_dstrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_dstrgb_cam_config = "_CAMDST"
g16_dstrgb_cam_script = showcast_dir + "//Scripts//process_g16_dstrgb_sec.py"
g16_dstrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_dstrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_fcorgb_cam = False  # GOES-19 False Color RGB - USER SECTOR

g16_fcorgb_cam_process = 6
g16_fcorgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_fcorgb_cam_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_fcorgb_cam_max_files = 5
g16_fcorgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_fcorgb_cam_resolution = 1
g16_fcorgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_fcorgb_cam_config = "_CAMFSC"
g16_fcorgb_cam_script = showcast_dir + "//Scripts//process_g16_fcorgb_sec.py"
g16_fcorgb_cam_output = showcast_dir + "//Output//"

products.append("g16_fcorgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_ftprgb_cam = True  # GOES-19 Fire Temperature RGB - USER SECTOR

g16_ftprgb_cam_process = 6
g16_ftprgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band07//"
g16_ftprgb_cam_identifier = "*L2-CMIPF-M*C07_G19*.nc"
g16_ftprgb_cam_max_files = 5
g16_ftprgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_ftprgb_cam_resolution = 2
g16_ftprgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_ftprgb_cam_config = "_CAMFTP"
g16_ftprgb_cam_script = showcast_dir + "//Scripts//process_g16_ftprgb_sec.py"
g16_ftprgb_cam_output = showcast_dir + "//Output//"

products.append("g16_ftprgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_ntcrgb_cam = False  # GOES-19 Natural True Color RGB - USER SECTOR

g16_ntcrgb_cam_process = 6
g16_ntcrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_ntcrgb_cam_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_ntcrgb_cam_max_files = 5
g16_ntcrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_ntcrgb_cam_resolution = 1
g16_ntcrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_ntcrgb_cam_config = "_CAMNTC"
g16_ntcrgb_cam_script = showcast_dir + "//Scripts//process_g16_ntcrgb_sec.py"
g16_ntcrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_ntcrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_nmprgb_cam = True  # GOES-19 Night microphysics RGB - USER SECTOR

g16_nmprgb_cam_process = 6
g16_nmprgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band15//"
g16_nmprgb_cam_identifier = "*L2-CMIPF-M*C15_G19*.nc"
g16_nmprgb_cam_max_files = 5
g16_nmprgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_nmprgb_cam_resolution = 2
g16_nmprgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_nmprgb_cam_config = "_CAMNMP"
g16_nmprgb_cam_script = showcast_dir + "//Scripts//process_g16_nmprgb_sec.py"
g16_nmprgb_cam_output = showcast_dir + "//Output//"

products.append("g16_nmprgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_swvrgb_cam = True  # GOES-19 Simple Water Vapor RGB - USER SECTOR

g16_swvrgb_cam_process = 6
g16_swvrgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band10//"
g16_swvrgb_cam_identifier = "*L2-CMIPF-M*C10_G19*.nc"
g16_swvrgb_cam_max_files = 5
g16_swvrgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_swvrgb_cam_resolution = 2
g16_swvrgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_swvrgb_cam_config = "_CAMSWV"
g16_swvrgb_cam_script = showcast_dir + "//Scripts//process_g16_swvrgb_sec.py"
g16_swvrgb_cam_output = showcast_dir + "//Output//"

products.append("g16_swvrgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_so2rgb_cam = True  # GOES-19 SO2 RGB - USER SECTOR

g16_so2rgb_cam_process = 6
g16_so2rgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band09//"
g16_so2rgb_cam_identifier = "*L2-CMIPF-M*C09_G19*.nc"
g16_so2rgb_cam_max_files = 5
g16_so2rgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_so2rgb_cam_resolution = 2
g16_so2rgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_so2rgb_cam_config = "_CAMSO2"
g16_so2rgb_cam_script = showcast_dir + "//Scripts//process_g16_so2rgb_sec.py"
g16_so2rgb_cam_output = showcast_dir + "//Output//"

products.append("g16_so2rgb_cam")
# ------------------------------------------------------------------------------------------------------
g16_trurgb_cam = True  # GOES-19 True Color RGB - USER SECTOR

g16_trurgb_cam_process = 6
g16_trurgb_cam_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_trurgb_cam_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_trurgb_cam_max_files = 5
g16_trurgb_cam_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_trurgb_cam_resolution = 1
g16_trurgb_cam_interval = "00,10,20,30,40,50"  # Processing interval
g16_trurgb_cam_config = "_CAMTRU"
g16_trurgb_cam_script = showcast_dir + "//Scripts//process_g16_trurgb_sec.py"
g16_trurgb_cam_output = showcast_dir + "//Output//"

products.append("g16_trurgb_cam")
# ------------------------------------------------------------------------------------------------------
# NATIONAL HURRICANE CENTER - (Experimental)

# ------------------------------------------------------------------------------------------------------
g16_band02_nhc = True  # GOES-19 L2 CMI - Band 02 - Central America + NHC

g16_band02_nhc_process = 7
g16_band02_nhc_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_band02_nhc_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_band02_nhc_max_files = 25
g16_band02_nhc_extent = [
    -113.5,
    -1.47,
    -50.25,
    36.83,
]
g16_band02_nhc_resolution = 1
g16_band02_nhc_config = "_NHC"
g16_band02_nhc_script = showcast_dir + "//Scripts//process_g1X_bands_nhc.py"
g16_band02_nhc_output = showcast_dir + "//Output//"

products.append("g16_band02_nhc")
# ------------------------------------------------------------------------------------------------------
g16_band13_nhc = True  # GOES-19 L2 CMI - Band 13 - Central America + NHC

g16_band13_nhc_process = 8
g16_band13_nhc_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_band13_nhc_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_band13_nhc_max_files = 25
g16_band13_nhc_extent = [
    -113.5,
    -1.47,
    -50.25,
    36.83,
]
g16_band13_nhc_resolution = 2
g16_band13_nhc_config = "_NHC"
g16_band13_nhc_script = showcast_dir + "//Scripts//process_g1X_bands_nhc.py"
g16_band13_nhc_output = showcast_dir + "//Output//"

products.append("g16_band13_nhc")
# ------------------------------------------------------------------------------------------------------
g16_trurgb_nhc = True  # GOES-19 True Color RGB - Central America + NHC

g16_trurgb_nhc_process = 9
g16_trurgb_nhc_directory = ingest_dir + "GOES-R-CMI-Imagery//Band01//"
g16_trurgb_nhc_identifier = "*L2-CMIPF-M*C01_G19*.nc"
g16_trurgb_nhc_max_files = 25
g16_trurgb_nhc_extent = [
    -113.5,
    -1.47,
    -50.25,
    36.83,
]
g16_trurgb_nhc_resolution = 1
g16_trurgb_nhc_interval = "00,10,20,30,40,50"  # Processing interval
g16_trurgb_nhc_config = "_NHCTRU"
g16_trurgb_nhc_script = showcast_dir + "//Scripts//process_g16_trurgb_nhc.py"
g16_trurgb_nhc_output = showcast_dir + "//Output//"

products.append("g16_trurgb_nhc")
# ------------------------------------------------------------------------------------------------------
g16_rrqpef_nhc = True  # GOES-19 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - Central America + NHC

g16_rrqpef_nhc_process = 10
g16_rrqpef_nhc_directory = ingest_dir + "GOES-R-Level-2-Products//RRQPEF//"
g16_rrqpef_nhc_identifier = "*RRQPEF*.nc"
g16_rrqpef_nhc_max_files = 25
g16_rrqpef_nhc_extent = [
    -113.5,
    -1.47,
    -50.25,
    36.83,
]
g16_rrqpef_nhc_resolution = 2
g16_rrqpef_nhc_config = "_NHCRRQ"
g16_rrqpef_nhc_script = showcast_dir + "//Scripts//process_g16_baseline_nhc.py"
g16_rrqpef_nhc_output = showcast_dir + "//Output//"

products.append("g16_rrqpef_nhc")
# ------------------------------------------------------------------------------------------------------
g16_glmden_nhc = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (Density) + GOES-19 Band 13 - Central America + NHC

g16_glmden_nhc_process = 11
g16_glmden_nhc_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glmden_nhc_identifier = "OR_GLM*.nc"
g16_glmden_nhc_max_files = 200
g16_glmden_nhc_extent = [
    -113.5,
    -1.47,
    -50.25,
    36.83,
]
g16_glmden_nhc_resolution = 2
g16_glmden_nhc_config = "_NHC"
g16_glmden_nhc_script = showcast_dir + "//Scripts//process_g16_glm_den_nhc.py"
g16_glmden_nhc_output = showcast_dir + "//Output//"

products.append("g16_glmden_nhc")
# ------------------------------------------------------------------------------------------------------
# GOES-19 BASELINE PRODUCTS (FROM GEONETCAST-AMERICAS AND / OR CLOUD)
# ------------------------------------------------------------------------------------------------------
g16_rrqpef_sum = (
    False  # GOES-19 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - USER SECTOR
)

g16_rrqpef_sum_process = 12
g16_rrqpef_sum_directory = ingest_dir + "GOES-R-Level-2-Products//RRQPEF//"
g16_rrqpef_sum_identifier = "*RRQPEF*.nc"
g16_rrqpef_sum_max_files = 5
g16_rrqpef_sum_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_rrqpef_sum_resolution = 2
g16_rrqpef_sum_config = "_SLV"
g16_rrqpef_sum_script = showcast_dir + "//Scripts//process_g16_baseline_sum.py"
g16_rrqpef_sum_output = showcast_dir + "//Output//"

products.append("g16_rrqpef_sum")
# ------------------------------------------------------------------------------------------------------
g16_rrqpef_slv = (
    True  # GOES-19 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - USER SECTOR
)

g16_rrqpef_slv_process = 12
g16_rrqpef_slv_directory = ingest_dir + "GOES-R-Level-2-Products//RRQPEF//"
g16_rrqpef_slv_identifier = "*RRQPEF*.nc"
g16_rrqpef_slv_max_files = 25
g16_rrqpef_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_rrqpef_slv_resolution = 2
g16_rrqpef_slv_config = "_SLV"
g16_rrqpef_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_rrqpef_slv_output = showcast_dir + "//Output//"

products.append("g16_rrqpef_slv")
# ------------------------------------------------------------------------------------------------------
g16_rrqpef_sv2 = (
    True  # GOES-19 L2 RRQPEF - Rainfall Rate - Quanti Pred. Estimate - USER SECTOR
)

g16_rrqpef_sv2_process = 12
g16_rrqpef_sv2_directory = ingest_dir + "GOES-R-Level-2-Products//RRQPEF//"
g16_rrqpef_sv2_identifier = "*RRQPEF*.nc"
g16_rrqpef_sv2_max_files = 25
g16_rrqpef_sv2_extent = [
    -90.3,
    13,
    -87.5,
    14.575,
]
g16_rrqpef_sv2_resolution = 2
g16_rrqpef_sv2_config = "_SV2"
g16_rrqpef_sv2_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_rrqpef_sv2_output = showcast_dir + "//Output//"

products.append("g16_rrqpef_sv2")
# ------------------------------------------------------------------------------------------------------
g16_cldhgt_slv = True  # GOES-19 L2 ACHAF - Cloud Top Height - USER SECTOR

g16_cldhgt_slv_process = 12
g16_cldhgt_slv_directory = ingest_dir + "GOES-R-Level-2-Products//ACHAF//"
g16_cldhgt_slv_identifier = "*ACHAF*.nc"
g16_cldhgt_slv_max_files = 5
g16_cldhgt_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_cldhgt_slv_resolution = 10  # Max Res.: 10 km
g16_cldhgt_slv_config = "_SLV"
g16_cldhgt_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_cldhgt_slv_output = showcast_dir + "//Output//"

products.append("g16_cldhgt_slv")
# ------------------------------------------------------------------------------------------------------
g16_cldtmp_slv = True  # GOES-19 L2 ACHTF - Cloud Top Temperature - USER SECTOR

g16_cldtmp_slv_process = 12
g16_cldtmp_slv_directory = ingest_dir + "GOES-R-Level-2-Products//ACHTF//"
g16_cldtmp_slv_identifier = "*ACHTF*.nc"
g16_cldtmp_slv_max_files = 5
g16_cldtmp_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_cldtmp_slv_resolution = 2
g16_cldtmp_slv_config = "_SLV"
g16_cldtmp_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_cldtmp_slv_output = showcast_dir + "//Output//"

products.append("g16_cldtmp_slv")
# ------------------------------------------------------------------------------------------------------
g16_aeropt_slv = True  # GOES-19 L2 AODF - Aerosol Optical Depth - USER SECTOR

g16_aeropt_slv_process = 12
g16_aeropt_slv_directory = ingest_dir + "GOES-R-Level-2-Products//AODF//"
g16_aeropt_slv_identifier = "*AODF*.nc"
g16_aeropt_slv_max_files = 5
g16_aeropt_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_aeropt_slv_resolution = 2
g16_aeropt_slv_config = "_SLV"
g16_aeropt_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_aeropt_slv_output = showcast_dir + "//Output//"

products.append("g16_aeropt_slv")
# ------------------------------------------------------------------------------------------------------
g16_dmwf14_slv = (
    True  # GOES-19 L2 DMWF-C14 - Derived Motion Winds Band 14 - USER SECTOR
)

g16_dmwf14_slv_process = 12
g16_dmwf14_slv_directory = ingest_dir + "GOES-R-Level-2-Products//DMWF-C14//"
g16_dmwf14_slv_identifier = "*DMWF*.nc"
g16_dmwf14_slv_max_files = 5
g16_dmwf14_slv_extent = [-120, 0.0, -10.0, 45.0]
g16_dmwf14_slv_resolution = 2
g16_dmwf14_slv_config = "_ATL"
g16_dmwf14_slv_script = showcast_dir + "//Scripts//process_g16_dmw_clouds_sec.py"
g16_dmwf14_slv_output = showcast_dir + "//Output//"

products.append("g16_dmwf14_slv")
# ------------------------------------------------------------------------------------------------------
g16_rsradi_slv = True  # GOES-19 L2 RSRF - Reflected Shortwave Radiation - USER SECTOR

g16_rsradi_slv_process = 12
g16_rsradi_slv_directory = ingest_dir + "GOES-R-Level-2-Products//RSRF//"
g16_rsradi_slv_identifier = "*RSRF*.nc"
g16_rsradi_slv_max_files = 25
g16_rsradi_slv_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_rsradi_slv_resolution = 2
g16_rsradi_slv_config = "_CAM"
g16_rsradi_slv_script = showcast_dir + "//Scripts//process_g16_rad_sec.py"
g16_rsradi_slv_output = showcast_dir + "//Output//"

products.append("g16_rsradi_slv")
# ------------------------------------------------------------------------------------------------------
g16_dsradi_slv = True  # GOES-19 L2 DSRF - Downward Shortwave Radiation - USER SECTOR

g16_dsradi_slv_process = 12
g16_dsradi_slv_directory = ingest_dir + "GOES-R-Level-2-Products//DSRF//"
g16_dsradi_slv_identifier = "*DSRF*.nc"
g16_dsradi_slv_max_files = 25
g16_dsradi_slv_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_dsradi_slv_resolution = 2
g16_dsradi_slv_config = "_CAM"
g16_dsradi_slv_script = showcast_dir + "//Scripts//process_g16_rad_sec.py"
g16_dsradi_slv_output = showcast_dir + "//Output//"

products.append("g16_dsradi_slv")
# ------------------------------------------------------------------------------------------------------
g16_sstskn_slv = True  # GOES-19 L2 SSTF - Sea Surface (Skin) Temperature - USER SECTOR

g16_sstskn_slv_process = 12
g16_sstskn_slv_directory = ingest_dir + "GOES-R-Level-2-Products//SSTF//"
g16_sstskn_slv_identifier = "*SSTF*.nc"
g16_sstskn_slv_max_files = 5
g16_sstskn_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_sstskn_slv_resolution = 2
g16_sstskn_slv_config = "_SLV"
g16_sstskn_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_sstskn_slv_output = showcast_dir + "//Output//"

products.append("g16_sstskn_slv")
# ------------------------------------------------------------------------------------------------------
g16_lstskn_slv = True  # GOES-19 L2 LSTF - Land Surface (Skin) Temperature - USER SECTOR

g16_lstskn_slv_process = 12
g16_lstskn_slv_directory = ingest_dir + "GOES-R-Level-2-Products//LSTF//"
g16_lstskn_slv_identifier = "*LST2KMF*.nc"
g16_lstskn_slv_max_files = 5
g16_lstskn_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_lstskn_slv_resolution = 2  # Max Res.: 10 km
g16_lstskn_slv_config = "_SLV"
g16_lstskn_slv_script = showcast_dir + "//Scripts//process_g16_baseline_sec.py"
g16_lstskn_slv_output = showcast_dir + "//Output//"

products.append("g16_lstskn_slv")
# ------------------------------------------------------------------------------------------------------
# GOES-19 - BANDS COMPOSITES / MULTISPECTRAL IMAGERY
# ------------------------------------------------------------------------------------------------------
g16_fcolor_sec = True  # GOES-19 False Color - Band 02 and Band 13 - USER SECTOR

g16_fcolor_sec_process = 13
g16_fcolor_sec_directory = ingest_dir + "GOES-R-CMI-Imagery//Band02//"
g16_fcolor_sec_identifier = "*L2-CMIPF-M*C02_G19*.nc"
g16_fcolor_sec_max_files = 5
g16_fcolor_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_fcolor_sec_resolution = 2
g16_fcolor_sec_config = "_FCS"
g16_fcolor_sec_script = showcast_dir + "//Scripts//process_g1X_false_color_sec.py"
g16_fcolor_sec_output = showcast_dir + "//Output//"

products.append("g16_fcolor_sec")
# #------------------------------------------------------------------------------------------------------
# g16_ircl13_sec            = False # GOES-19 IR Clouds - Band 13 with Blue Marble - USER SECTOR

# g16_ircl13_sec_process    = 7
# g16_ircl13_sec_directory  = ingest_dir + 'GOES-R-CMI-Imagery//Band13//'
# g16_ircl13_sec_identifier = '*L2-CMIPF-M*C13_G19*.nc'
# g16_ircl13_sec_max_files  = 3
# g16_ircl13_sec_extent     = [-97.9, 6.0, -73.0, 20.0]
# g16_ircl13_sec_resolution = 2
# g16_ircl13_sec_config     = '_IRS'
# g16_ircl13_sec_script     = showcast_dir + '//Scripts//process_g1X_ir_clouds_sec.py'
# g16_ircl13_sec_output     = showcast_dir + '//Output//'

# products.append('g16_ircl13_sec')
# #------------------------------------------------------------------------------------------------------
# g16_irce13_sec            = False # GOES-19 IR Clouds Enhanced - Band 13 [enhanced] with Blue Marble - USER SECTOR

# g16_irce13_sec_process    = 7
# g16_irce13_sec_directory  = ingest_dir + 'GOES-R-CMI-Imagery//Band13//'
# g16_irce13_sec_identifier = '*L2-CMIPF-M*C13_G19*.nc'
# g16_irce13_sec_max_files  = 3
# g16_irce13_sec_extent     = [-97.9, 6.0, -73.0, 20.0]
# g16_irce13_sec_resolution = 2
# g16_irce13_sec_config     = '_IES'
# g16_irce13_sec_script     = showcast_dir + '//Scripts//process_g1X_ir_clouds_enhance_sec.py'
# g16_irce13_sec_output     = showcast_dir + '//Output//'

# products.append('g16_irce13_sec')
# ------------------------------------------------------------------------------------------------------
# g16_swdiff_slv            = True # GOES-19 Split Window Difference - USER SECTOR

# g16_swdiff_slv_process    = 7
# g16_swdiff_slv_directory  = ingest_dir + 'GOES-R-CMI-Imagery//Band12//'
# g16_swdiff_slv_identifier = '*L2-CMIPF-M*C12_G19*.nc'
# g16_swdiff_slv_max_files  = 3
# g16_swdiff_slv_extent     = [-91.14, 12.5, -86.25, 15.25]
# g16_swdiff_slv_resolution = 2
# g16_swdiff_slv_config     = '_SLVSWD'
# g16_swdiff_slv_script     = showcast_dir + '//Scripts//process_g1X_swd_sec.py'
# g16_swdiff_slv_output     = showcast_dir + '//Output//'

# products.append('g16_swdiff_slv')
# ------------------------------------------------------------------------------------------------------
# g16_swdiff_cam            = True # GOES-19 Split Window Difference - USER SECTOR

# g16_swdiff_cam_process    = 7
# g16_swdiff_cam_directory  = ingest_dir + 'GOES-R-CMI-Imagery//Band12//'
# g16_swdiff_cam_identifier = '*L2-CMIPF-M*C12_G19*.nc'
# g16_swdiff_cam_max_files  = 3
# g16_swdiff_cam_extent     = [-97.9, 6.0, -73.0, 20.0]
# g16_swdiff_cam_resolution = 2
# g16_swdiff_cam_config     = '_CAMSWD'
# g16_swdiff_cam_script     = showcast_dir + '//Scripts//process_g1X_swd_sec.py'
# g16_swdiff_cam_output     = showcast_dir + '//Output//'

# products.append('g16_swdiff_cam')
# ------------------------------------------------------------------------------------------------------
g16_salpro_sec = True  # GOES-19 Saharan Air Layer Tracking Product - USER SECTOR

g16_salpro_sec_process = 13
g16_salpro_sec_directory = ingest_dir + "GOES-R-CMI-Imagery//Band13//"
g16_salpro_sec_identifier = "*L2-CMIPF-M*C13_G19*.nc"
g16_salpro_sec_max_files = 5
g16_salpro_sec_extent = [-120, 0.0, -10.0, 45.0]
g16_salpro_sec_resolution = 2
g16_salpro_sec_config = "_ATLSAL"
g16_salpro_sec_script = showcast_dir + "//Scripts//process_g1X_sal_sec.py"
g16_salpro_sec_output = showcast_dir + "//Output//"

products.append("g16_salpro_sec")
# ------------------------------------------------------------------------------------------------------
# GOES-19 GLM (GEOSTATIONARY LIGHTNING MAPPER) - SUGGESTION: PUT IN A DEDICATED PROCESS
# ------------------------------------------------------------------------------------------------------
g16_glm20s_slv = (
    True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (20s) - USER SECTOR
)

g16_glm20s_slv_process = 14
g16_glm20s_slv_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glm20s_slv_identifier = "OR_GLM*.nc"
g16_glm20s_slv_max_files = 15
g16_glm20s_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_glm20s_slv_resolution = 2
g16_glm20s_slv_config = "_SLV20S"
g16_glm20s_slv_script = showcast_dir + "//Scripts//process_g16_glm_20s_sec.py"
g16_glm20s_slv_output = showcast_dir + "//Output//"

products.append("g16_glm20s_slv")
# ------------------------------------------------------------------------------------------------------
g16_glir20_slv = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (20s) + GOES-19 Band 13 - USER SECTOR

g16_glir20_slv_process = 15
g16_glir20_slv_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glir20_slv_identifier = "OR_GLM*.nc"
g16_glir20_slv_max_files = 60
g16_glir20_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_glir20_slv_resolution = 2
g16_glir20_slv_config = "_SLVIGL"
g16_glir20_slv_script = showcast_dir + "//Scripts//process_g16_glm_ir_20s_sec.py"
g16_glir20_slv_output = showcast_dir + "//Output//"

products.append("g16_glir20_slv")
# ------------------------------------------------------------------------------------------------------
g16_glmtra_slv = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (Tracking) + GOES-19 Band 13 - USER SECTOR

g16_glmtra_slv_process = 16
g16_glmtra_slv_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glmtra_slv_identifier = "OR_GLM*.nc"
g16_glmtra_slv_max_files = 60
g16_glmtra_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_glmtra_slv_resolution = 2
g16_glmtra_slv_config = "_SLVTRA"
g16_glmtra_slv_script = showcast_dir + "//Scripts//process_g16_glm_tra_sec.py"
g16_glmtra_slv_output = showcast_dir + "//Output//"

products.append("g16_glmtra_slv")
# ------------------------------------------------------------------------------------------------------
g16_glmden_slv = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (Density) + GOES-19 Band 13 - USER SECTOR

g16_glmden_slv_process = 17
g16_glmden_slv_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glmden_slv_identifier = "OR_GLM*.nc"
g16_glmden_slv_max_files = 60
g16_glmden_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
g16_glmden_slv_resolution = 2
g16_glmden_slv_config = "_SLVDEN"
g16_glmden_slv_script = showcast_dir + "//Scripts//process_g16_glm_den_sec.py"
g16_glmden_slv_output = showcast_dir + "//Output//"

products.append("g16_glmden_slv")
# ------------------------------------------------------------------------------------------------------
g16_glmirc_sec = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (5 min density) - USER SECTOR

g16_glmirc_sec_process = 18
g16_glmirc_sec_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_glmirc_sec_identifier = "GLM_*.nc"
g16_glmirc_sec_max_files = 12
g16_glmirc_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]
g16_glmirc_sec_resolution = 2
g16_glmirc_sec_config = "_CAM5MD"
g16_glmirc_sec_script = showcast_dir + "//Scripts//process_g16_glm_clouds_sec.py"
g16_glmirc_sec_output = showcast_dir + "//Output//"

products.append("g16_glmirc_sec")
# ------------------------------------------------------------------------------------------------------
g16_gl5min_slv = True  # GOES-19 L2 GLM - Geostationary Lightning Mapper (5min) SLV

g16_gl5min_slv_process = 19
g16_gl5min_slv_directory = ingest_dir + "GOES-R-GLM-Products//"
g16_gl5min_slv_identifier = "OR_GLM*.nc"
g16_gl5min_slv_max_files = 1500
g16_gl5min_slv_extent = [
    -90.8,
    12.4,
    -87.0,
    15.2,
]  # [-91.14, 12.5, -86.25, 15.25]
g16_gl5min_slv_resolution = 2
g16_gl5min_slv_config = "_G5MSLV"
g16_gl5min_slv_script = showcast_dir + "//Scripts//process_g16_glm_5min_slv.py"
g16_gl5min_slv_output = showcast_dir + "//Output//"

products.append("g16_gl5min_slv")
# ------------------------------------------------------------------------------------------------------
# HOURLY GLOBAL BLENDED PRODUCTS - El Salvador
# ------------------------------------------------------------------------------------------------------
mul_btpwpr_slv = True  # Hourly Global Blended Total Precipitable Water

mul_btpwpr_slv_process = 20
mul_btpwpr_slv_directory = ingest_dir + "JPSS//PRODUCTS//BTPW//"
mul_btpwpr_slv_identifier = "BHP-TPW*"
mul_btpwpr_slv_max_files = 5
mul_btpwpr_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
mul_btpwpr_slv_resolution = 2  # Max Res.: 16 km
mul_btpwpr_slv_config = "_SLV"
mul_btpwpr_slv_script = showcast_dir + "//Scripts//process_jps_btpw_v2.py"
mul_btpwpr_slv_output = showcast_dir + "//Output//"

products.append("mul_btpwpr_slv")
# ------------------------------------------------------------------------------------------------------
mul_bpctpr_slv = True  # Hourly Global Blended Total Precipitable Water Anomaly

mul_bpctpr_slv_process = 20
mul_bpctpr_slv_directory = ingest_dir + "JPSS//PRODUCTS//BTPW//"
mul_bpctpr_slv_identifier = "BHP-PCT*"
mul_bpctpr_slv_max_files = 5
mul_bpctpr_slv_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]
mul_bpctpr_slv_resolution = 2  # Max Res.: 16 km
mul_bpctpr_slv_config = "_SLV"
mul_bpctpr_slv_script = showcast_dir + "//Scripts//process_jps_btpw_v2.py"
mul_bpctpr_slv_output = showcast_dir + "//Output//"

products.append("mul_bpctpr_slv")
# ------------------------------------------------------------------------------------------------------
# HOURLY GLOBAL BLENDED PRODUCTS - Central America
# ------------------------------------------------------------------------------------------------------
mul_btpwpr_cam = True  # Hourly Global Blended Total Precipitable Water

mul_btpwpr_cam_process = 20
mul_btpwpr_cam_directory = ingest_dir + "JPSS//PRODUCTS//BTPW//"
mul_btpwpr_cam_identifier = "BHP-TPW*"
mul_btpwpr_cam_max_files = 5
mul_btpwpr_cam_extent = [-120, 0.0, -57.777, 35]
mul_btpwpr_cam_resolution = 8  # Max Res.: 16 km
mul_btpwpr_cam_config = "_CAM"
mul_btpwpr_cam_script = showcast_dir + "//Scripts//process_jps_btpw_v2.py"
mul_btpwpr_cam_output = showcast_dir + "//Output//"

products.append("mul_btpwpr_cam")
# ------------------------------------------------------------------------------------------------------
mul_bpctpr_cam = True  # Hourly Global Blended Total Precipitable Water Anomaly

mul_bpctpr_cam_process = 20
mul_bpctpr_cam_directory = ingest_dir + "JPSS//PRODUCTS//BTPW//"
mul_bpctpr_cam_identifier = "BHP-PCT*"
mul_bpctpr_cam_max_files = 5
mul_bpctpr_cam_extent = [-120, 0.0, -57.777, 35]
mul_bpctpr_cam_resolution = 8  # Max Res.: 16 km
mul_bpctpr_cam_config = "_CAM"
mul_bpctpr_cam_script = showcast_dir + "//Scripts//process_jps_btpw_v2.py"
mul_bpctpr_cam_output = showcast_dir + "//Output//"

products.append("mul_bpctpr_cam")
# ------------------------------------------------------------------------------------------------------

#######################################################################################################
# NUCAPS SOUNDINGS - SUGGESTION: PUT IN A DEDICATED PROCESS
#######################################################################################################

# ------------------------------------------------------------------------------------------------------
n20_nucaps_sec = True  # NUCAPS SOUNDING

n20_nucaps_sec_process = 21
n20_nucaps_sec_directory = ingest_dir + "JPSS//PRODUCTS//NUCAPS//"
n20_nucaps_sec_identifier = "NUCAPS-EDR*"
n20_nucaps_sec_max_files = 1000
n20_nucaps_sec_extent = [
    -91.14,
    12.5,
    -86.25,
    15.25,
]  # Recommended using a max of 5 x 5 degree
n20_nucaps_sec_resolution = 1
n20_nucaps_sec_config = "_SLVNCP"
n20_nucaps_sec_script = showcast_dir + "//Scripts//process_nucaps.py"
n20_nucaps_sec_output = showcast_dir + "//Output//"

products.append("n20_nucaps_sec")
# ------------------------------------------------------------------------------------------------------
# MULTIMISSION FIRE / HOT SPOTS (INPE SHAPEFILES)
# ------------------------------------------------------------------------------------------------------
mul_firein_sec = True  # MULTIMISSION FIRE / HOTSPOTS - INPE

mul_firein_sec_process = 22
mul_firein_sec_directory = ingest_dir + "INPE//"
mul_firein_sec_identifier = "INPE_MVF_*.gz"
mul_firein_sec_max_files = 5
mul_firein_sec_resolution = 0  # Max Res.: N/A
mul_firein_sec_config = ""
mul_firein_sec_script = showcast_dir + "//Scripts//process_mul_fires.py"
mul_firein_sec_output = showcast_dir + "//Output//"

products.append("mul_firein_sec")
# ------------------------------------------------------------------------------------------------------
# CHARTS
# ------------------------------------------------------------------------------------------------------
idk_crbqpf_sec = (
    True  # QUANTITATIVE PRECIP. FORECASTS FOR DAYS 1-6 (CENTRAL AMERICA AND CARIBBEAN)
)

idk_crbqpf_sec_process = 23
idk_crbqpf_sec_directory = ingest_dir + "RANET//"
idk_crbqpf_sec_identifier = "crb3.gif"
idk_crbqpf_sec_max_files = 1
idk_crbqpf_sec_resolution = 0  # Max Res.: N/A
idk_crbqpf_sec_config = ""
idk_crbqpf_sec_script = showcast_dir + "//Scripts//process_idk_idkqpf_sec.py"
idk_crbqpf_sec_output = showcast_dir + "//Output//"

products.append("idk_crbqpf_sec")
# ------------------------------------------------------------------------------------------------------
ics_atrodn_sec = True  # ISCS-ANLZ-CLIMATE - NORTH ATLANTIC AREA

ics_atrodn_sec_process = 23
ics_atrodn_sec_directory = ingest_dir + "ISCS-ANLZ-CLIMATE//"
ics_atrodn_sec_identifier = "*T_AXNT*"
ics_atrodn_sec_max_files = 1
ics_atrodn_sec_resolution = 0  # Max Res.: N/A
ics_atrodn_sec_config = ""
ics_atrodn_sec_script = showcast_dir + "//Scripts//process_isc_atrodn_sec.py"
ics_atrodn_sec_output = showcast_dir + "//Output//"

products.append("ics_atrodn_sec")
# ------------------------------------------------------------------------------------------------------
ics_atrode_sec = True  # ISCS-ANLZ-CLIMATE - EASTERN PACIFIC AREA

ics_atrode_sec_process = 23
ics_atrode_sec_directory = ingest_dir + "ISCS-ANLZ-CLIMATE//"
ics_atrode_sec_identifier = "*T_AXPZ*"
ics_atrode_sec_max_files = 1
ics_atrode_sec_resolution = 0  # Max Res.: N/A
ics_atrode_sec_config = ""
ics_atrode_sec_script = showcast_dir + "//Scripts//process_isc_atrode_sec.py"
ics_atrode_sec_output = showcast_dir + "//Output//"

products.append("ics_atrode_sec")
# ------------------------------------------------------------------------------------------------------
ics_wtsuna_sec = True  # ISCS-WARN - TSUNAMI

ics_wtsuna_sec_process = 23
ics_wtsuna_sec_directory = ingest_dir + "ISCS-WARN//"
ics_wtsuna_sec_identifier = "*T_WE*"
ics_wtsuna_sec_max_files = 1
ics_wtsuna_sec_resolution = 0  # Max Res.: N/A
ics_wtsuna_sec_config = ""
ics_wtsuna_sec_script = showcast_dir + "//Scripts//process_isc_wtsuna_sec.py"
ics_wtsuna_sec_output = showcast_dir + "//Output//"

products.append("ics_wtsuna_sec")
# ------------------------------------------------------------------------------------------------------
ics_wvolca_sec = True  # ISCS-WARN - VOLCANIC ASH

ics_wvolca_sec_process = 23
ics_wvolca_sec_directory = ingest_dir + "ISCS-WARN//"
ics_wvolca_sec_identifier = "*T_WVHO*"
ics_wvolca_sec_max_files = 1
ics_wvolca_sec_resolution = 0  # Max Res.: N/A
ics_wvolca_sec_config = ""
ics_wvolca_sec_script = showcast_dir + "//Scripts//process_isc_wvolca_sec.py"
ics_wvolca_sec_output = showcast_dir + "//Output//"

products.append("ics_wvolca_sec")
# ------------------------------------------------------------------------------------------------------
# ALWP - ADVECTED LAYERED PRECIPITABLE WATER
# ------------------------------------------------------------------------------------------------------
jps_alpw01_sec = True  # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (Sfc - 850 mb)

jps_alpw01_sec_process = 24
jps_alpw01_sec_directory = ingest_dir + "CIRA//"
jps_alpw01_sec_identifier = "*ADVECT_COMPOSITE*"
jps_alpw01_sec_max_files = 6
jps_alpw01_sec_extent = [
    -120,
    0.0,
    -10.0,
    45.0,
]  # Max:[-180.0,-71.0,180.0,71.0]
jps_alpw01_sec_resolution = 8  # Max Res.: N/A
jps_alpw01_sec_config = "_ATL850"
jps_alpw01_sec_script = showcast_dir + "//Scripts//process_jps_alpwat_single_sec.py"
jps_alpw01_sec_output = showcast_dir + "//Output//"

products.append("jps_alpw01_sec")
# ------------------------------------------------------------------------------------------------------
jps_alpw02_sec = True  # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (850 - 700 mb)

jps_alpw02_sec_process = 24
jps_alpw02_sec_directory = ingest_dir + "CIRA//"
jps_alpw02_sec_identifier = "*ADVECT_COMPOSITE*"
jps_alpw02_sec_max_files = 6
jps_alpw02_sec_extent = [
    -120,
    0.0,
    -10.0,
    45.0,
]  # Max:[-180.0,-71.0,180.0,71.0]
jps_alpw02_sec_resolution = 8  # Max Res.: N/A
jps_alpw02_sec_config = "_ATL700"
jps_alpw02_sec_script = showcast_dir + "//Scripts//process_jps_alpwat_single_sec.py"
jps_alpw02_sec_output = showcast_dir + "//Output//"

products.append("jps_alpw02_sec")
# ------------------------------------------------------------------------------------------------------
jps_alpw03_sec = True  # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (700 - 500 mb)

jps_alpw03_sec_process = 24
jps_alpw03_sec_directory = ingest_dir + "CIRA//"
jps_alpw03_sec_identifier = "*ADVECT_COMPOSITE*"
jps_alpw03_sec_max_files = 6
jps_alpw03_sec_extent = [
    -120,
    0.0,
    -10.0,
    45.0,
]  # Max:[-180.0,-71.0,180.0,71.0]
jps_alpw03_sec_resolution = 8  # Max Res.: N/A
jps_alpw03_sec_config = "_ATL500"
jps_alpw03_sec_script = showcast_dir + "//Scripts//process_jps_alpwat_single_sec.py"
jps_alpw03_sec_output = showcast_dir + "//Output//"

products.append("jps_alpw03_sec")
# ------------------------------------------------------------------------------------------------------
jps_alpw04_sec = True  # ADVECTED LAYER PRECIPITABLE WATER PRODUCT (500 - 300 mb)

jps_alpw04_sec_process = 24
jps_alpw04_sec_directory = ingest_dir + "CIRA//"
jps_alpw04_sec_identifier = "*ADVECT_COMPOSITE*"
jps_alpw04_sec_max_files = 5
jps_alpw04_sec_extent = [
    -120,
    0.0,
    -10.0,
    45.0,
]  # Max:[-180.0,-71.0,180.0,71.0]
jps_alpw04_sec_resolution = 8  # Max Res.: N/A
jps_alpw04_sec_config = "_ATL300"
jps_alpw04_sec_script = showcast_dir + "//Scripts//process_jps_alpwat_single_sec.py"
jps_alpw04_sec_output = showcast_dir + "//Output//"

products.append("jps_alpw04_sec")
# ------------------------------------------------------------------------------------------------------
# SST - NOAA CORAL REEF WATCH DAILY 5km - Anomaly and Trend
# ------------------------------------------------------------------------------------------------------
mul_sstcor_slv = True  # SST - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstcor_slv_process = 20
mul_sstcor_slv_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstcor_slv_identifier = "coraltemp*"
mul_sstcor_slv_max_files = 25
mul_sstcor_slv_extent = [
    -91.6,
    11.5,
    -86.3,
    14.48,
]
mul_sstcor_slv_resolution = 5  # Max Res.: 5 km
mul_sstcor_slv_config = "_SLV"
mul_sstcor_slv_script = showcast_dir + "//Scripts//process_sst_coralre_sec.py"
mul_sstcor_slv_output = showcast_dir + "//Output//"

products.append("mul_sstcor_slv")
# ------------------------------------------------------------------------------------------------------
mul_sstcor_pac = True  # SST - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstcor_pac_process = 25
mul_sstcor_pac_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstcor_pac_identifier = "coraltemp*"
mul_sstcor_pac_max_files = 25
mul_sstcor_pac_extent = [-180, -30, -60, 30]
mul_sstcor_pac_resolution = 5  # Max Res.: 5 km
mul_sstcor_pac_config = "_PAC"
mul_sstcor_pac_script = showcast_dir + "//Scripts//process_sst_coralre_sec.py"
mul_sstcor_pac_output = showcast_dir + "//Output//"

products.append("mul_sstcor_pac")
# ------------------------------------------------------------------------------------------------------
mul_sstcor_atn = True  # SST - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstcor_atn_process = 25
mul_sstcor_atn_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstcor_atn_identifier = "coraltemp*"
mul_sstcor_atn_max_files = 25
mul_sstcor_atn_extent = [-100, -5.0, -15, 30]
mul_sstcor_atn_resolution = 5  # Max Res.: 5 km
mul_sstcor_atn_config = "_ATN"
mul_sstcor_atn_script = showcast_dir + "//Scripts//process_sst_coralre_sec.py"
mul_sstcor_atn_output = showcast_dir + "//Output//"

products.append("mul_sstcor_atn")
# ------------------------------------------------------------------------------------------------------
mul_sstano_slv = True  # SST ANOMALY - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstano_slv_process = 25
mul_sstano_slv_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstano_slv_identifier = "ct5km_ssta*"
mul_sstano_slv_max_files = 25
mul_sstano_slv_extent = [
    -91.6,
    11.5,
    -86.3,
    14.48,
]
mul_sstano_slv_resolution = 5  # Max Res.: 5 km
mul_sstano_slv_config = "_SLV"
mul_sstano_slv_script = showcast_dir + "//Scripts//process_sst_anomaly_sec.py"
mul_sstano_slv_output = showcast_dir + "//Output//"

products.append("mul_sstano_slv")
# ------------------------------------------------------------------------------------------------------
mul_sstano_pac = True  # SST ANOMALY - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstano_pac_process = 25
mul_sstano_pac_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstano_pac_identifier = "ct5km_ssta*"
mul_sstano_pac_max_files = 25
mul_sstano_pac_extent = [-180, -30, -60, 30]
mul_sstano_pac_resolution = 5  # Max Res.: 5 km
mul_sstano_pac_config = "_PAC"
mul_sstano_pac_script = showcast_dir + "//Scripts//process_sst_anomaly_sec.py"
mul_sstano_pac_output = showcast_dir + "//Output//"

products.append("mul_sstano_pac")
# ------------------------------------------------------------------------------------------------------
mul_sstano_atn = True  # SST ANOMALY - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_sstano_atn_process = 25
mul_sstano_atn_directory = ingest_dir + "NOAA-NESDIS//"
mul_sstano_atn_identifier = "ct5km_ssta*"
mul_sstano_atn_max_files = 25
mul_sstano_atn_extent = [-100, -5.0, -15, 30]
mul_sstano_atn_resolution = 5  # Max Res.: 5 km
mul_sstano_atn_config = "_ATN"
mul_sstano_atn_script = showcast_dir + "//Scripts//process_sst_anomaly_sec.py"
mul_sstano_atn_output = showcast_dir + "//Output//"

products.append("mul_sstano_atn")
# ------------------------------------------------------------------------------------------------------

mul_ssttre_slv = True  # 7-DAY SST TREND - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_ssttre_slv_process = 25
mul_ssttre_slv_directory = ingest_dir + "NOAA-NESDIS//"
mul_ssttre_slv_identifier = "ct5km_sst-trend-7d*"
mul_ssttre_slv_max_files = 25
mul_ssttre_slv_extent = [
    -91.6,
    11.5,
    -86.3,
    14.48,
]
mul_ssttre_slv_resolution = 5  # Max Res.: 5 km
mul_ssttre_slv_config = "_SLV"
mul_ssttre_slv_script = showcast_dir + "//Scripts//process_sst_7dtrend_sec.py"
mul_ssttre_slv_output = showcast_dir + "//Output//"

products.append("mul_ssttre_slv")
# ------------------------------------------------------------------------------------------------------
mul_ssttre_pac = True  # 7-DAY SST TREND - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_ssttre_pac_process = 25
mul_ssttre_pac_directory = ingest_dir + "NOAA-NESDIS//"
mul_ssttre_pac_identifier = "ct5km_sst-trend-7d*"
mul_ssttre_pac_max_files = 25
mul_ssttre_pac_extent = [-180, -30, -60, 30]
mul_ssttre_pac_resolution = 5  # Max Res.: 5 km
mul_ssttre_pac_config = "_PAC"
mul_ssttre_pac_script = showcast_dir + "//Scripts//process_sst_7dtrend_sec.py"
mul_ssttre_pac_output = showcast_dir + "//Output//"

products.append("mul_ssttre_pac")
# ------------------------------------------------------------------------------------------------------
mul_ssttre_atn = True  # 7-DAY SST TREND - NOAA CORAL REEF WATCH DAILY 5km - El Salvador

mul_ssttre_atn_process = 25
mul_ssttre_atn_directory = ingest_dir + "NOAA-NESDIS//"
mul_ssttre_atn_identifier = "ct5km_sst-trend-7d*"
mul_ssttre_atn_max_files = 25
mul_ssttre_atn_extent = [-100, -5.0, -15, 30]
mul_ssttre_atn_resolution = 5  # Max Res.: 5 km
mul_ssttre_atn_config = "_ATN"
mul_ssttre_atn_script = showcast_dir + "//Scripts//process_sst_7dtrend_sec.py"
mul_ssttre_atn_output = showcast_dir + "//Output//"

products.append("mul_ssttre_atn")
# ------------------------------------------------------------------------------------------------------
# NOAA-20 - CHLOROPHYLL-A CONCENTRATION
# ------------------------------------------------------------------------------------------------------
jps_ocrgvy_sec = True  # NOAA-20 - CHLOROPHYLL-A CONCENTRATION - REGION VY

jps_ocrgvy_sec_process = 25
jps_ocrgvy_sec_directory = ingest_dir + "JPSS//PRODUCTS//OC//"
jps_ocrgvy_sec_identifier = "VR1VCW_*VY*.nc"
jps_ocrgvy_sec_max_files = 25
jps_ocrgvy_sec_extent = [
    -91.6,
    11.5,
    -86.3,
    14.48,
]  # Max:[-120.0, 0.0, -60.0, 44.0]
jps_ocrgvy_sec_resolution = 1  # Max Res.: 0.750 km
jps_ocrgvy_sec_config = "_SLV"
jps_ocrgvy_sec_script = showcast_dir + "//Scripts//process_jps_oceanc_sec.py"
jps_ocrgvy_sec_output = showcast_dir + "//Output//"

products.append("jps_ocrgvy_sec")
# ------------------------------------------------------------------------------------------------------
# JPSS - VIIRS VEGETATION PRODUCTS
# ------------------------------------------------------------------------------------------------------
jps_gblgvf_sec = True  # JPSS - GREEN VEGETATION FRACTION - GLOBAL - 4km

jps_gblgvf_sec_process = 25
jps_gblgvf_sec_directory = ingest_dir + "JPSS//PRODUCTS//VEGETATION//"
jps_gblgvf_sec_identifier = "GVF-WKL-GLB*.nc"
jps_gblgvf_sec_max_files = 1
jps_gblgvf_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]  # Max:[-180, -80, 180, 80]
jps_gblgvf_sec_resolution = 4  # Max Res.: 4 km
jps_gblgvf_sec_interval = ""  # Processing interval
jps_gblgvf_sec_config = "_CAMGVF"
jps_gblgvf_sec_script = showcast_dir + "//Scripts//process_jps_gblgvf_sec.py"
jps_gblgvf_sec_output = showcast_dir + "//Output//"

products.append("jps_gblgvf_sec")
# ------------------------------------------------------------------------------------------------------
jps_ndvita_sec = True  # JPSS - NORMALIZED DIFFERENCE VEGETATION INDEX AT TOP OF ATMOSPHERE (TOA) - GLOBAL - 4km

jps_ndvita_sec_process = 25
jps_ndvita_sec_directory = ingest_dir + "JPSS//PRODUCTS//VEGETATION//"
jps_ndvita_sec_identifier = "VI-WKL-GLB*.nc"
jps_ndvita_sec_max_files = 1
jps_ndvita_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]  # Max:[-180, -80, 180, 80]
jps_ndvita_sec_resolution = 4  # Max Res.: 4 km
jps_ndvita_sec_interval = ""  # Processing interval
jps_ndvita_sec_config = "_CAMNDA"
jps_ndvita_sec_script = showcast_dir + "//Scripts//process_jps_vegidx_sec.py"
jps_ndvita_sec_output = showcast_dir + "//Output//"

products.append("jps_ndvita_sec")
# ------------------------------------------------------------------------------------------------------
jps_ndvitc_sec = True  # JPSS - NORMALIZED DIFFERENCE VEGETATION INDEX AT TOP OF CANOPY (TOC) - GLOBAL - 4km

jps_ndvitc_sec_process = 25
jps_ndvitc_sec_directory = ingest_dir + "JPSS//PRODUCTS//VEGETATION//"
jps_ndvitc_sec_identifier = "VI-WKL-GLB*.nc"
jps_ndvitc_sec_max_files = 1
jps_ndvitc_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]  # Max:[-180, -80, 180, 80]
jps_ndvitc_sec_resolution = 4  # Max Res.: 4 km
jps_ndvitc_sec_interval = ""  # Processing interval
jps_ndvitc_sec_config = "_CAMNDC"
jps_ndvitc_sec_script = showcast_dir + "//Scripts//process_jps_vegidx_sec.py"
jps_ndvitc_sec_output = showcast_dir + "//Output//"

products.append("jps_ndvitc_sec")
# ------------------------------------------------------------------------------------------------------
jps_evitoc_sec = (
    True  # JPSS - ENHANCED VEGETATION INDEX AT TOP OF CANOPY (TOC) - GLOBAL - 4km
)

jps_evitoc_sec_process = 25
jps_evitoc_sec_directory = ingest_dir + "JPSS//PRODUCTS//VEGETATION//"
jps_evitoc_sec_identifier = "VI-WKL-GLB*.nc"
jps_evitoc_sec_max_files = 1
jps_evitoc_sec_extent = [
    -97.9,
    6.0,
    -73.0,
    20.0,
]  # Max:[-180, -80, 180, 80]
jps_evitoc_sec_resolution = 4  # Max Res.: 4 km
jps_evitoc_sec_interval = ""  # Processing interval
jps_evitoc_sec_config = "_CAMEVC"
jps_evitoc_sec_script = showcast_dir + "//Scripts//process_jps_vegidx_sec.py"
jps_evitoc_sec_output = showcast_dir + "//Output//"

products.append("jps_evitoc_sec")
# ------------------------------------------------------------------------------------------------------

#######################################################################################################
# FILE PROCESSING AND LOG FUNCTION
#######################################################################################################


def procProduct(
    prod_dir,
    identifier,
    config,
    script,
    min_lon,
    min_lat,
    max_lon,
    max_lat,
    resolution,
    output,
    vis_dir,
):

    # Create the list that will store the file names
    gnc_files = []

    # Add to the list the files in the dir that matches the identifier
    for filename in sorted(glob.glob(prod_dir + identifier)):
        # If the identifier is for a file that doesn't change its name:
        if (
            (identifier == "gfs.sam.t00z.f120")
            or (identifier == "gfs.sam.t12z.f120")
            or (identifier == "gfs.t00z.pgrb2full.0p50.f384")
            or (identifier == "gfs.t06z.pgrb2full.0p50.f384")
            or (identifier == "gfs.t12z.pgrb2full.0p50.f384")
            or (identifier == "gfs.t18z.pgrb2full.0p50.f384")
            or (identifier == "d6.gif")
            or (identifier == "crb3.gif")
        ):
            import datetime  # Basic Date and Time types
            import pathlib  # Object-oriented filesystem paths

            # Get the file modification time
            mtime = datetime.datetime.fromtimestamp(
                pathlib.Path(filename).stat().st_mtime
            ).strftime("%Y%m%d%H%M%S")
            gnc_files.append(os.path.normpath(filename + config + "_c" + mtime))
        else:  # If the files have unique names
            gnc_files.append(os.path.normpath(filename + config))

        # print("\n")
        # print("PRODDIR: ", prod_dir+identifier)
        # print("PRODNAM: ", filename + config + '_' + mtime)
        # print("\n")

    # Keep on the list only the max number of files
    gnc_files = gnc_files[-max_files:]

    import datetime  # Basic Date and Time types

    # If the gnc log file doesn't exist yet, create one
    file = open(
        showcast_dir + "//Logs//gnc_log_" + str(datetime.datetime.now())[0:10] + ".txt",
        "a",
    )
    file.close()

    # Put all file names on the gnc log in a list
    log = []
    with open(
        showcast_dir + "//Logs//gnc_log_" + str(datetime.datetime.now())[0:10] + ".txt"
    ) as f:
        log = f.readlines()

    # Remove the line feeds
    log = [x.strip() for x in log]

    # Compare the gnc file list with the log
    # Loop through all the files
    for x in gnc_files:
        # If a file is not on the log, process it
        if x not in log:
            print("Processing product:\n", str(x))
            print("Script used:\n", script)
            global prod_count
            prod_count = prod_count + 1
            # print('Command used:\n', script + ' ' + x + ' ' + str(min_lon) + ' ' + str(min_lat) + ' ' + str(max_lon) + ' ' + str(max_lat) + ' ' + str(resolution))
            os.system(
                script
                + ' "'
                + str(x)
                + '" '
                + str(min_lon)
                + " "
                + str(min_lat)
                + " "
                + str(max_lon)
                + " "
                + str(max_lat)
                + " "
                + str(resolution)
                + " "
                + output
                + " "
                + vis_dir
                + " "
                + str(config)
            )
            print("\n")


# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

print("\n")
print("############## SHOWCAST MONITOR STARTED ##############")
print("Started at:", datetime.datetime.now())
print("\n")

# Create a counter to identify how many products have been processed in the run
prod_count = 0

# Identifier for channel composites init
config = ""

# Extent init
extent = [0.0, 0.0, 0.0, 0.0]

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

#######################################################################################################
# PROCESSING EACH SELECTED PRODUCT
#######################################################################################################

for product in products:  # Loop through products
    process = globals()[product + "_process"]
    directory = globals()[product + "_directory"]
    identifier = globals()[product + "_identifier"]
    max_files = globals()[product + "_max_files"]
    if (product + "_extent") in globals():
        extent = globals()[product + "_extent"]
    resolution = globals()[product + "_resolution"]
    config = globals()[product + "_config"]
    output = globals()[product + "_output"]
    script = python_env + "python " + globals()[product + "_script"]

    # Call the processing routine, if the product is set to True and if the product process is equal to the current SHOWCast process
    if (globals()[product] == True) and (
        globals()[product + "_process"] == showcast_process
    ):
        procProduct(
            directory,
            identifier,
            config,
            script,
            extent[0],
            extent[1],
            extent[2],
            extent[3],
            resolution,
            output,
            vis_dir,
        )

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------

print("\n")
print("##############  SHOWCAST MONITOR ENDED  ##############")
print("Ended at:", datetime.datetime.now())
print("Number of products processed:", prod_count)
print("Total processing time:", t.time() - start, "seconds")
print("\n")

# ------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
