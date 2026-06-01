#!/bin/bash
while true; do
  inotifywait -r -e modify,create,delete /home/geonetcast/SHOWCast/HTML/
  rsync -avz --delete /home/geonetcast/SHOWCast/HTML/ /var/www/html/HTML/
  sleep 10s
done
