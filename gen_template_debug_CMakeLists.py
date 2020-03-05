#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a CMakeLists.txt file for compiling a generic \
                                              unit test project.")

parser.add_argument("modulename", help="The name of the module that you want to generate a CMakeLists.txt for")

args = parser.parse_args()

modulename = args.modulename

lines = []

lines.append("cmake_minimum_required(VERSION 3.12.0)\n") # Push past the LTS ubuntu version for the benefits of a newer default
lines.append("project( %s )\n" % modulename)
lines.append("\n")
lines.append("# The target\n")
lines.append("add_executable( %s %s.c )\n" % (modulename, modulename))

# Create and fill the file.
file = open("CMakeLists.txt", "w")
for line in lines:
    file.write( line )
file.close()
