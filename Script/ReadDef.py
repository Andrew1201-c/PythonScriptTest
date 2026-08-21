## @file
#
#  Parsing the *.defs file
#
#  Copyright (c) 2026 Andrew
#  SPDX-License-Identifier: BSD-2-Clause-Patent
##

import configparser
import sys
import os
import operator as op

if len(sys.argv) < 3:
    print("Usage: readdef <filename> <section> <key>")
    sys.exit(1)

filename = sys.argv[1]
section = sys.argv[2]
key = sys.argv[3]

if not os.path.exists(filename):
    print("The file is not exist: " + filename)
    sys.exit(1)

# Default Values
value = None
kind = None
expression = False

# Array of the valid dataypes
datatype = [ "VOID", "PVOID", 
            "INT", "UINT", "UINT64", 
            "UINT32", "UINT8", "PINT", 
            "PUINT", "PUINT64", 
            "PUINT32", "PUINT8",
            "BOOLEAN"
]

config = configparser.ConfigParser()
config.read(filename)

if section not in config:
    print("Section does not exist:", section)
    sys.exit(1)

if key in config[section]:
    value = config[section][key]
    parts = config[section][key].split("|")

    # Parsing
    if "|" not in value:
        value = value.strip()
        kind = None
        expression = False
        datatype = None

    if len(parts) > 1:
        field = parts[1].strip()

        if field.upper() in datatype:
            datatype = field.upper()
            kind = None
        else:
            kind = field

    else:
        print("Invalid Macro: ", kind)
        sys.exit(1)


    if len(parts) > 1:
        if len(parts) > 2:
            if parts[2].lower() == "expression":
                expression = True
                
        if len(parts) > 3:
            if parts[3].lower() == "expression":
                expression = True
        
        if len(parts) > 2:
            if parts[2] in datatype:
                datatype = parts[2]

            elif parts[2].lower() == "expression":
                expression = True
                datatype = None

            else:
                print("Invalid data type:", parts[2])
                sys.exit(1)

# Print the values
print("Value:", value)
print("Type:", kind)
print("Expression:", expression)
print("Data Type:", datatype)

print("Key: " + key.split("|")[0].strip())

if value is None:
    print("Cannot find key: " + key)
