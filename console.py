#!/usr/bin/env python3
""" importing the cmd module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """create create your data model.
    manage (create, update, destroy, etc) objects via a console / command interpreter.
    store and persist objects to a file (JSON file)."""
    prompt = "(hbnb) "
    def do_quit(self, command):
        exit(1)

    def emptyline(self):
        pass
    
    def do_EOF(self, eof):
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
