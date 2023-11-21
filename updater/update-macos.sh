#!/bin/bash

# if a previous version of cmm exists, remove it
if [[ "/usr/local/bin/cmm" -e ]]; then
	rm /usr/bin/local/cmm
fi

# if /usr/local/var doesn't exist, make it
if [[ "/usr/local/var" -ne ]]; then
	mkdir /usr/local/var
fi

# if /usr/local/var/cmm doesn't exist, make it
if [[ "/usr/local/var/cmm" -ne ]]; then
	mkdir /usr/local/var/cmm
fi

# if version in /usr/local/var/cmm/version is less than latest release and user consents to update
mkdir /private/tmp/cmm-update
cd /private/tmp/cmm-update

wget 

chmod a+x cmm
cp cmm /usr/local/bin/cmm
cp cmm /