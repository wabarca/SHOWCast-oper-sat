#!/bin/bash
while true; do
  inotifywait -r -e modify,create,delete /var/www/html/HTML/
  rsync -avzh --delete /var/www/html/HTML/ wabarca@192.168.4.20:/var/www/html/SHOWCast/HTML/
  sleep 10s
done
