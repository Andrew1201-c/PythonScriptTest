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


if len(sys.argv) < 4:
    print("Usage: writeautogen <filename> <section> <output.h>")
    sys.exit(1)


filename = sys.argv[1]
section = sys.argv[2]
output = sys.argv[3]


if not os.path.exists(filename):
    print("The file does not exist: " + filename)
    sys.exit(1)


config = configparser.ConfigParser()
config.optionxform = str

config.read(filename, encoding="utf-8")


# Custom section
if section not in config:
    print("Section does not exist: " + section)
    sys.exit(1)


guard = f"_AUTOGEN_H_{time}"


with open(output, "w", encoding="utf-8", newline="\n") as f:

    f.write("/** @file\n")
    f.write(" *\n")
    f.write(" * Auto Generated Header File.\n")
    f.write(" *\n")
    f.write(" * Copyright (c) 2026 Andrew\n")
    f.write(" * SPDX-License-Identifier: BSD-2-Clause-Patent\n")
    f.write(" */\n\n")

    f.write(f"#ifndef {guard}\n")
    f.write(f"#define {guard}\n\n")

    f.write("/* Auto Generated Header File, for C to include. */\n\n")


    for key, value in config[section].items():

        key = key.strip()

        if not key:
            continue


        parts = value.split("|")

        actual_value = parts[0].strip()

        kind = None
        datatype = None
        expression = False


        for part in parts[1:]:

            field = part.strip()

            if not field:
                continue


            if field.lower() == "macro":
                kind = "macro"


            elif field.lower() == "expression":
                expression = True


            else:
                # Convert datatype directly to uppercase.
                datatype = field.upper()


        if kind == "macro":

            if expression:
                f.write(
                    f"#define {key} ({actual_value})\n"
                )

            else:
                f.write(
                    f"#define {key} {actual_value}\n"
                )


        else:
            print(
                f"Warning: Unknown kind for {key}: {kind}"
            )


    f.write(f"\n#endif /* {guard} */\n")


print("Generated: " + output)