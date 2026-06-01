#!/bin/bash
# Select the number of SHOWCast parallel processes
declare -i num_process=25
export DISPLAY=:0
echo --------------
echo "SHOWCast Start"
echo --------------
echo
echo "SHOWCast will be executed."
echo

# Check if the showcast env is already created
if [ -d "/home/geonetcast/miniconda3/envs/showcast" ]; then

	echo "Calling showcast_start.py"
	for i in $( seq 1 $num_process)
	do
		xfce4-terminal -T $i -e 'bash -c "/home/geonetcast/miniconda3/envs/showcast/bin/python /home/geonetcast/SHOWCast/Scripts/showcast_start.py '$i'; exec bash"' &
	done
	echo "Calling cloud_download_config.py"
	echo /home/geonetcast/miniconda3/envs/showcast/bin/python /home/geonetcast/SHOWCast/Cloud/Scripts/pda_aws_download_start.py
	declare -i cloud_process=$((num_process+1))
	xfce4-terminal -T $cloud_process -e 'bash -c "/home/geonetcast/miniconda3/envs/showcast/bin/python /home/geonetcast/SHOWCast/Cloud/Scripts/pda_aws_download_start.py; exec bash"' &
	#echo

else	# if not, show a message to the user
	echo The showcast env is not created. Please create it using the installer found at
	echo $(pwd)/Installer/showcast_install_linux.sh
	echo and start SHOWCast again.
fi

echo
read -p "Finished. Press any key to exit ..."