#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a template .c file in the folder \
                                              (Title, section headers, etc) it is called in.")

parser.add_argument("filename", help="The name of the file that you want to generate omitting .c")

args = parser.parse_args()

filename = args.filename

lines = []

# lines.append("    \n")
lines.append("/******************************************************************************/\n")
lines.append("/*!\n")
lines.append(" * @file  %s.c\n" %filename)
lines.append(" * @brief\n")
lines.append(" * \n")
lines.append(" * @author Cathal Harte <cathal.harte@protonmail.com>\n")
lines.append(" *\n")
lines.append(" */\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Includes\n")
lines.append("******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Definitions and types\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Internal function prototypes\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Data\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Functions\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")

# Create and fill the file.
file = open("%s.c" % filename, "w")
for line in lines:
    file.write( line )
file.close()



