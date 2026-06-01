#!/bin/bash
while true; do
  inotifywait -r -e modify,create,delete /var/www/html/Output/ISC/
  rsync -avzh --delete /var/www/html/Output/ISC/ wabarca@192.168.4.20:/var/www/html/SHOWCast/Output/ISC/
  sleep 10s
done
