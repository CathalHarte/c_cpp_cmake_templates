#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a template _test.cpp file in the folder \
                                              (Title, section headers, etc) it is called in.")

parser.add_argument("filename", help="The name of the file that you want to generate omitting _test.c (the name of the target module)")

args = parser.parse_args()

filename = args.filename

lines = []

lines.append("/**\n")
lines.append("* \\file %s_test.cpp\n" % filename)
lines.append("*\n")
lines.append("* \\brief ... unit test\n")
lines.append("*\n")
lines.append("* \\author Cathal Harte  <cathal.harte@protonmail.com>\n")
lines.append("*/\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Includes\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("#if defined( _MSC_VER )\n")
lines.append("    #define _SILENCE_TR1_NAMESPACE_DEPRECATION_WARNING \n")
lines.append("#endif\n")
lines.append("\n")
lines.append("#include <gtest/gtest.h>\n")
lines.append("#include <%s.h>\n" % filename)
lines.append("\n")


lines.append("namespace\n")
lines.append("{\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Definitions and types\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("#if defined( _MSC_VER )\n")
lines.append("    #pragma warning(disable:4996)        // strcpy, sprintf security warnings\n")
lines.append("#endif\n")
lines.append("\n")
lines.append("DEFINE_FFF_GLOBALS;                    //!< Required for FFF\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Local Function prototypes\n")
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
lines.append("/* This will be deleted or overwritten soon */\n")
lines.append("TEST( testGroup1, scrap_test_1 )\n")
lines.append("{\n")
lines.append("\n")
lines.append("\n")
lines.append("}\n")
lines.append("\n")
lines.append("} // namespace\n")
lines.append("\n")

# Create and fill the file.
file = open(filename + "_test.cpp", "w")
for line in lines:
    file.write( line )
file.close()
