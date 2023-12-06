#!/usr/bin/env python3
""" importing the cmd module"""
import cmd
from modes import nonint_mode

class DConsole(cmd.Cmd):
    """create create your data model.
    manage (create, update, destroy, etc) objects via a console / command interpreter.
    store and persist objects to a file (JSON file)."""
    
    def do_hello(self, message):
        print("hello," + message)
    
    def do_EOF(self, eof):
        return True

if __name__ == "__main__":
    nonint_mode(DConsole, cmd.Cmd.cmdloop, cmd.Cmd.onecmd)