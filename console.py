#!/usr/bin/python3
"""
======================================================
Module with the entry point of the command interpreter
======================================================
"""

import cmd, os
from models.base_model import BaseModel
from models import storage

classes = ["BaseModel"] # List of classes we might need

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

    def do_create(self, arg):

        if len(arg) < 1:
            print ("** class name missing **")
        elif not arg in classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save() # this saves it into the file.json
            print(new.id)

    def do_show(self, arg):

        data = arg.split()
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if not key in storage.all():
                print("** no instance found **")
            else:   
                print(storage.all()[key])

    def do_destroy(self, arg):

        data = arg.split()
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if not key in storage.all():
                print("** no instance found **")
            else:   
                storage.all().pop(key) # Deletes the key of the dict
                storage.save() # Saves the file,json

    def do_all(self, arg):

        data = arg.split()
        my_list = []
        if len(arg) < 1: # If only typed all
            # Print all the items of storage
            for key, value in storage.all().items():
                c_name, c_id = key.split(".")
                my_list.append("[{}] ({}) {}".format(c_name, c_id, value))
            print(my_list)
        else:
            if not data[0] in classes:
                print("** class doesn't exist **")
            else:
                #print all the keys with data[0]
                for key, value in storage.all().items():
                    c_name, c_id = key.split(".")
                    if c_name == data[0]:
                        my_list.append("[{}] ({}) {}".format(c_name, c_id, value))
            print(my_list)

    def do_update(self, arg):
        """ Updates and instance: update <class name> <id> <attribute name> '<attribute value>'"""

        data = arg.split()
        if len(data) < 1:
            print("** class name missing **")
        elif not data[0] in classes:
            print("** class doesn't exist **")
        elif len(data) < 2:
            print("** instance id missing **")
        else:
            key = data[0] + "." + data[1]
            if not key in storage.all():
                print("** no instance found **")
            else:   
                storage.all().pop(key) # Deletes the key of the dict
                storage.save() # Saves the file,json

    def do_clear(self, arg):
        """Clearses the screen"""

        os.system('clear')

    def emptyline(self):
        """empty line"""

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
