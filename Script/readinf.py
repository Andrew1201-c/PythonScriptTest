## @file
#
#  Parsing the *.inf file
#
#  Copyright (c) 2026 Andrew
#  SPDX-License-Identifier: BSD-2-Clause-Patent
##

import configparser
import sys
import os
import operator as op

if len(sys.argv) < 3:
    print("Usage: readinf <filename> <section> <key>")
    sys.exit(1)

filename = sys.argv[1]
section = sys.argv[2]
key = sys.argv[3]

if not os.path.exists(filename):
    print("The file is not exist: " + filename)
    sys.exit(1)

value = None

config = configparser.ConfigParser()
config.read(filename)

if section not in config:
    print("Section does not exist:", section)
    sys.exit(1)

if key in config[section]:
    value = config[section][key]
    print(config[section][key])
else:
    sys.exit(1)

if value is None:
    print("Cannot find key: " + key)