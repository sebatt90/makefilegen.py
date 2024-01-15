#!/bin/python
### SETTINGS ###

INCLUDE_DIR = "."
LIBRARY_DIR = "."
EXEC_NAME = "exec"
BUILD_PATH = "./build"
MAIN_CXX = "main"
COMPILER = "g++"

# Libraries to link
# e.g. -lpthreads -lglfw
LINK_LIBRARIES = ""

###
import os
import sys

makefile_src = ""
objs = ""

for subdir, dirs, files in os.walk('./'):
    for file in files:
        fdata = file.split(".")

        if len(fdata) == 1:
            continue
        
        if fdata[1] == "cpp" or fdata[1] == "c":
            makefile_src += f"{fdata[0]}.o: {fdata[0]}.{fdata[1]}\n\t{COMPILER} -c {fdata[0]}.cpp\n\n"
            objs += (f"{fdata[0]}.o ")


# make clean
makefile_src += f"clean:\n\trm -rf {BUILD_PATH}\n\trm *.o"

# exec part
tmp = makefile_src
makefile_src = f"{EXEC_NAME}: {objs}\n\tmkdir -p {BUILD_PATH}\n\t\
{COMPILER} -o {BUILD_PATH}/{EXEC_NAME}\
 -L{LIBRARY_DIR}\
 -I{INCLUDE_DIR}\
 {objs}\n\n"

makefile_src += tmp

# Write to makefile
Makefile = open("Makefile", "w")

n = Makefile.write(makefile_src)

if n == len(makefile_src):
    print("Success! Makefile generated.")
else:
    print("Failure! Makefile was not generated.")

Makefile.close()