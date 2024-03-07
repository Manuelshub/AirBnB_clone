#!/usr/bin/python3
"""
This module contains entry point of a command interpreter
"""
import cmd



class HBNBCommand(cmd.Cmd):
    """
    A class that is the entry point of a command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to quit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
