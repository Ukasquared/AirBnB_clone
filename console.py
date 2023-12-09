#!/usr/bin/env python3
""" importing the cmd module"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Basic implementation of the console
    """
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of file used to quit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit(1)

    def emptyline(self):
        """This wont allow the last excecuted command to repeat 
        when the ENTER key is pressed"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()