#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a template .cpp file in the folder \
                                              (Title, section headers, etc) it is called in.")

parser.add_argument("filename", help="The name of the file that you want to generate omitting .cpp")

args = parser.parse_args()

filename = args.filename

lines = []

lines.append("/******************************************************************************/\n")
lines.append("/*!\n")
lines.append(" * @file  %s.cpp\n" %filename)
lines.append(" * @brief\n")
lines.append(" * \n")
lines.append(" * @author Cathal Harte <cathal.harte@protonmail.com>\n")
lines.append(" */\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Includes\n")
lines.append("******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Definitions\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Types\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Internal function prototypes\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Classes\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Functions\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")

# Create and fill the file.
file = open("%s.cpp" % filename, "w")
for line in lines:
    file.write( line )
file.close()



