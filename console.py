#!/usr/bin/python3
"""
======================================================
Module with the entry point of the command interpreter
======================================================
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""

    intro = 'Welcome the Airbnb console, type help for help or quit for close'
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """method for close and exit from the console"""

        print("Chao PapAA")
        # quit()
        return True

    def do_EOF(self, arg):
        """method for exit from the console"""
        print("\nya no hay mas que leer")
        exit()

    def emptyline(self):
        """empty line"""

        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
