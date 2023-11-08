#!/bin/bash

if [ $(which pyinstaller | grep -o pyinstaller > /dev/null &&  echo 0 || echo 1) -eq 1 ]; then
	echo "pyinstaller is not installed. Installing..."
	python3 -m pip install pyinstaller
fi

if [ "$1" = '-r' ]; then
    if [ -z "$2" ]; then
        echo "Please provide the name of the build to remove after -r."
        exit 1
    fi
    echo "Removing previous build of $2..."
    rm -f "./$2"
    rm -f "./$2.spec"
    echo "Done."

	script_name="$2"
	run="$3"
	shift 1	
else
    if [ -z "$1" ]; then
        echo "Please provide the name of the build to create."
        exit 1
    fi

	script_name="$1"
	run="$2"
fi

echo "Building $script_name..."
pyinstaller --onefile "$script_name.py"
echo "Done."

echo "Setting permissions..."
chmod a+x "./$script_name"
echo "Done."

echo ""
if [ "$run" = 'run' ]; then
	./cmm -h
fi
