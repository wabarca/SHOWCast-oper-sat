#!/bin/bash
FILESYSTEM1=/home/geonetcast/GNC-A/
CAPACITY=70
CACHEDIR1=/home/geonetcast/GNC-A/incoming/

if [ $(df -P $FILESYSTEM1 | awk '{ gsub("%",""); capacity = $5 }; END { print capacity }') -gt $CAPACITY ]
then
    find "$CACHEDIR1" -type f -mtime +1 -exec rm -f {} \;
fi
