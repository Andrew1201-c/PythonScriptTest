## @file
#
#  Write to the AutoGen.h
#
#  Copyright (c) 2026 Andrew
#  SPDX-License-Identifier: BSD-2-Clause-Patent
##

import configparser
import sys
import os
from datetime import datetime

time = datetime.now().strftime("%Y%m%d")

if len(sys.argv) < 3:
    print("Usage: writeautogen <filename> <output.h>")
    sys.exit(1)

filename = sys.argv[1]
output = sys.argv[2]

if not os.path.exists(filename):
    print("The file does not exist: " + filename)
    sys.exit(1)

config = configparser.ConfigParser()
config.optionxform = str
config.read(filename)

if "Defines" not in config:
    print("Section does not exist: Defines")
    sys.exit(1)

with open(output, "w", encoding="utf-8") as f:

    f.write(f"#ifndef _AUTOGEN_H_{time}\n")
    f.write(f"#define _AUTOGEN_H_{time}\n\n")
    f.write(f"/* Auto Generated Header File, for C to include. */\n\n")

    for key, value in config["Defines"].items():

        key = key.strip()
        parts = value.split("|")

        actual_value = parts[0].strip()
        kind = parts[1].strip().lower() if len(parts) > 1 else None

        if kind == "macro":
            f.write(f"#define {key} {actual_value}\n")

    f.write(f"\n#endif _/* AUTOGEN_H_{time} */\n")

print("Generated: " + output)