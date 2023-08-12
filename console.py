#!/usr/bin/python3
import cmd
"""The entry point of the command interpreter."""


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using CTRL+D (EOF)"""
        print()  # Print a new line before exiting
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
