#!/usr/bin/python3
"""Class HBNBComand a program called console.py
"""

import re
from shlex import split
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Command line for the airbnb
    """
    __allw_cls = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }

    prompt = '(hbnb) '

    def default(self, arg):
        """
        Execute a default action when the entered command does not
        match any existing command method.
        """

        args = arg.split(".")
        if args[1] == "all()":
            self.do_all(args[0])
            return
        if args[1] == "count()":
            self.do_count(args[0])
            return
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_quit(self, line):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, line):
        """ Quit command to exit the program. """
        return True

    def do_create(self, class_name):
        """
        Create a new instance of a specified class.

        Usage: create <class_name>
        """

        if len(class_name) == 0:
            print("** class name missing **")
        elif class_name not in HBNBCommand.__allw_cls:
            print("** class doesn't exist **")
        else:
            instan = eval(class_name)()
            instan.save()
            print(instan.id)

    def do_show(self, args):
        """
        Display information of a specified instance.

        Usage: show <class_name> <instance_id>
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__allw_cls:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            for value in storage.all().values():
                if args[1] == value.id:
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete a specified instance.

        Usage: destroy <class_name> <instance_id>
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__allw_cls:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            for key, value in storage.all().items():
                if args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, args):
        """
        Display all instances of a specified class or all classes.

        Usage: all [<class_name>]
        """

        args = args.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__allw_cls:
            print("** class doesn't exist **")
        else:
            insList = []
            for value in storage.all().values():
                if len(args) > 0 and args[0] == value.__class__.__name__:
                    insList.append(value.__str__())
                elif len(args) == 0:
                    insList.append(value.__str__())
            print(insList)

    def do_count(self, args):
        """
        Count the number of instances of a specified class.
        """
        args = args.split()
        c_instance = 0
        for key, value in storage.all().items():
            if len(args) > 0 and args[0] == value.__class__.__name__:
                c_instance += 1
        print(c_instance)

    def do_update(self, args):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(args)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
