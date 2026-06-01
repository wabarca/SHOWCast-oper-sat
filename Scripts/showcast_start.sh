#!/bin/bash
# Wait for the GUI to be ready
while [[ ! $(pgrep gnome-shell) ]]; do sleep 1; done
cd /home/geonetcast/SHOWCast
./showcast_start_linux.sh
