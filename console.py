#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
from models.base_model import BaseModel
from models import storage
import datetime
import json


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True

    def do_quit(self, line):
        """Exits the program.
        """
        return True

    def emptyline(self):
        """Doesn't do anything on ENTER.
        """
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, 
	saves it (to the JSON file), and prints the id.
	"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)
    
    def do_show(self, line):
        """Prints the string representation 
	of an instance based on name and id.
	"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")
    
    def do_destroy(self, line):
        """Deletes an instance based on the class name and id 
	(save the change into the JSON file).
	"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in all_instances:
            del all_instances[key]
            storage.save()
        else:
            print("** no instance found **")
    
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name."""
        args = line.split()
        all_instances = storage.all()
        if len(args) == 0:
            instance_list = list(all_instances.values())
        else:
            class_name = args[0]
            if class_name not in ['BaseModel']:
                print("** class doesn't exist **")
                return
            instance_list = [instance for key, instance in all_instances.items() if key.startswith(class_name)]
        print([str(instance) for instance in instance_list])
    
    def do_update(self, line):
        """Updates an instance based on the class name and id 
	by adding or updating attribute 
	(save the change into the JSON file).
	"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        all_instances = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in all_instances:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3]
        
        instance = all_instances[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
