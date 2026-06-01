#! /bin/bash
# 
# Reads year to backup $1 and directory to copy $2
echo Backup of year $1 from directories in $2
for folder in $(ls $2)
do 
    mkdir -p $HOME/Backup/Output/$1/${PWD##*/}/$folder/
    mv ./$folder/*_2021* $HOME/Backup/Output/$1/${PWD##*/}/$folder/
done
