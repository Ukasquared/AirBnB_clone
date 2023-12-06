#!/usr/bin/env python3
"""check for the different mode"""
import sys
import os

def nonint_mode(name, cmdloop, onecmd):
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                name.use_rawinput = False
                name(stdin=file).cmdloop()
        else:
            name().onecmd("".join(sys.argv[1:]))
    else:
        name().cmdloop()