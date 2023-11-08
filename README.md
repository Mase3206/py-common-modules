# py-common-modules
Modules I have made that I frequently use across multiple programs.


# Common Module Manager (cmm)

cmm is the custom module manager I made to install, remove, and update the modules in this repository. 

- `-u` updates all packages
- `-i package` installs the specified package. If already installed, it attempts to update it.
- `-r package` removes the specified package. If not installed, it exits.

When installing or removing a package, do not add the file extension. 


# build.sh

**Usage:** `./build.sh [-r] file [run]`

I made `build.sh` to quickly make binaries of `cmm` via PyInstaller. I haven't tested it in Windows, but in Unix-based OSes, it will build the passed program (extension ommitted) with the `--onefile` flag set by default. It will then move the binary from ./dist/ to ./ and mark it as executable.

If `build.sh` is run with the `-r` flag, it will rebuild the package by removing its remnants and building it again.

If `run` is added to the end of the command, it will test the binary it made by telling it to display its help page (`cmm -h`).


# reformat

`reformat` has a bunch of functions to reformat data. It is used in a number of my programs and was the main reason I made `cmm`.


# checkDependencies

`checkDependencies` does exactly that: it checks python modules needed by a program to function. If it doesn't find them, it will attempt to install them via `pip`.