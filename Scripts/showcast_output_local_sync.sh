#!/bin/bash
while true; do
  inotifywait -r -e modify,create,delete /home/geonetcast/SHOWCast/Output/ISC/
  rsync -avz --delete /home/geonetcast/SHOWCast/Output/ISC/ /var/www/html/Output/ISC/
  sleep 10s
done
