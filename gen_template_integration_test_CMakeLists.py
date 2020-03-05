#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a CMakeLists.txt file for compiling a generic \
                                              integration_test project.")

parser.add_argument("modulename", help="The name of the module that you want to generate a CMakeLists.txt for")

args = parser.parse_args()

modulename = args.modulename

lines = []

lines.append("cmake_minimum_required(VERSION 3.16.0)\n")
lines.append("project( %s_integration_test ASM C )\n" % modulename)
lines.append("\n")
lines.append("set(REPO_ROOT \"../../..\")\n")
lines.append("\n")
lines.append("# Where to find include files.\n")
lines.append("include_directories( ..\n")
lines.append("                     ${REPO_ROOT}/hardware/cypress )\n")
lines.append("\n")
lines.append("\n")
lines.append("# Where to find other source files\n")
lines.append("add_subdirectory( .. %s )\n" % modulename)
lines.append("add_subdirectory( ${REPO_ROOT}/hardware/cypress cypress )\n")
lines.append("add_subdirectory( ${REPO_ROOT}/hardware/gen5_startup gen5_startup )\n")
lines.append("\n")
lines.append("# Linker script\n")
lines.append("# The location of the linker script is needed relative to the _build folder, hence the extra ../\n")
lines.append("set( LINKER_SCRIPT \"${REPO_ROOT}/../compiler/amcu_app.ld\" ) \n")
lines.append("set( CMAKE_EXE_LINKER_FLAGS \"${CMAKE_EXE_LINKER_FLAGS} -T ${LINKER_SCRIPT}\" )\n")
lines.append("\n")
lines.append("# The target\n")
lines.append("add_executable( %s_integration_test %s_integration_test.c )\n" % (modulename, modulename))
lines.append("\n")
lines.append("# Add library\n")
lines.append("target_link_libraries( %s_integration_test PRIVATE %s\n"  % (modulename, modulename))
lines.append("                                                        cypress\n")
lines.append("                                                        gen5_startup )\n")
lines.append("\n")

# Create and fill the file.
file = open("CMakeLists.txt", "w")
for line in lines:
    file.write( line )
file.close()
