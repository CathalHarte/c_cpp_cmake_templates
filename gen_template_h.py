#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="This creates a template .h file in the folder \
                                              (Title, section headers, etc) it is called in. \
                                              If the filename ends in _fake, extra structures \
                                              useful for writing a \"fake\" header will be added")

parser.add_argument("filename", help="The name of the file that you want to generate omitting .c")

args = parser.parse_args()

filename = args.filename

lines = []

# lines.append("    \n")
lines.append("/******************************************************************************/\n")
lines.append("/*!\n")
lines.append(" * @file  %s.h\n" %filename)
lines.append(" * @brief \n")
lines.append(" * \n")
lines.append(" * @author Cathal Harte <cathal.harte@protonmail.com\n")
lines.append(" */\n")
lines.append("#ifndef _%s_H\n" %filename.upper())
lines.append("#define _%s_H\n" %filename.upper())
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Includes\n")
lines.append("******************************************************************************/\n")
lines.append("\n")
if "_fake" in filename:
    lines.append("#include \"%s.h\"\n" % filename.replace("_fake",""))
    lines.append("\n")
    lines.append("// Include the faking framework\n")
    lines.append("#include <fff.h>\n")
    lines.append("\n")
lines.append("#ifdef __cplusplus\n")
lines.append("extern \"C\"\n")
lines.append("{\n")
lines.append("#endif\n")
lines.append("\n")
lines.append("/*! @defgroup %s %s.\n" % ( filename, filename.capitalize()))
lines.append(" *\n")
lines.append(" * @addtogroup %s\n" % filename)
lines.append(" * @{\n")
lines.append(" * @brief \n")
lines.append(" */\n")
lines.append("/*******************************************************************************\n")
lines.append("* Definitions and types\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Data\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
lines.append("/*******************************************************************************\n")
lines.append("* Function prototypes\n")
lines.append("*******************************************************************************/\n")
lines.append("\n")
if "_fake" in filename:
    lines.append("FAKE_VOID_FUNC( )\n") 
    lines.append("FAKE_VALUE_FUNC( ) \n")
    lines.append("\n")
    lines.append("/*! Do something to all the %s fakes.\n" % filename.replace("_fake","").upper())
    lines.append(" *\n")
    lines.append(" * e.g. %s_ALL_FAKES( RESET_FAKE );\n" % filename.replace("_fake","").upper())
    lines.append(" */\n")
    lines.append("#define %s_ALL_FAKES(action)   \\\n"  % filename.replace("_fake","").upper())
    lines.append("    action( )\n")
lines.append("\n")
lines.append("/*! @}\n")
lines.append(" */\n")
lines.append("\n")
lines.append("#ifdef __cplusplus\n")
lines.append("}\n")
lines.append("#endif\n")
lines.append("\n")
lines.append("#endif  // _%s_H\n" %filename.upper())

# Create and fill the file.
file = open(filename + ".h", "w")
for line in lines:
    file.write( line )
file.close()



