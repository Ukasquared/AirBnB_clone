#!/usr/bin/python3
""" importing the cmd module"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Basic implementation of the console
    """
    prompt = '(hbnb) '
    class_names = {"BaseModel": BaseModel,
                   "User": User,
                   "Place": Place,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Review": Review
    }

    def do_EOF(self, line):
        """End of file used to quit the program"""
        print()
        return True

    def do_create(self, old_model):
        """ creates an instance"""
        if not old_model:
            print("** class name missing **")
            return
        if old_model in self.class_names.keys():
            new_model = self.class_names[old_model]()
            new_model.save()
            print(new_model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, model):
        """show instance according to id"""
        args = model.split()
        if not model or not args[0]:
            print("** class name missing **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        found = False
        if args[0] in self.class_names:
            objs = storage.all()
            # obj is a key value pair
            for obj_keys, obj_values in objs.items():
                if (args[0] + '.' + args[1]) == obj_keys:
                    print(obj_values)
                    found = True
                if found is True:
                    break
            if found is False:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, model):
        """delete instance according to id"""
        deleted = False
        args = model.split()
        if not model:
            print("** class name missing **")
            return
        if len(args) != 2:
            print("** instance id missing **")
            return
        if args[0] in self.class_names:
            objs = storage.all()
            for key in objs.keys():
                if (args[0] + '.' + args[1]) == key:
                    del objs[key]
                    deleted = True
                if deleted is True:
                    break
            if deleted is True:
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, model):
        """show all instance according to class name or not"""
        obj_list = []
        exist = False
        if model:
            args = model.split()
        if not model:
            # print all the instances reloaded into storage.__objects
            for key in storage.all().keys():
                obj_list.append(str(storage.all()[key]))
            print(obj_list)
        elif args[0] and args[0] in self.class_names.keys():
            for key in storage.all().keys():
                model_name = key.split('.')
                if args[0] == model_name[0]:
                    exist = True
                    obj_list.append(str(storage.all()[key]))
            if exist is True:
                print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, model):
        """updates an instance"""
        exist = False
        if not model:
            print("** class name missing **")
            return
        all_arg = shlex.split(model)
        args = len(all_arg)
        if args < 2:
            print("** instance id missing **")
            return
        if args < 3:
            print("** attribute name missing **")
            return
        if args < 4:
            print("** value missing **")
            return
        my_key = all_arg[0] + '.' + all_arg[1]
        if all_arg[0] in self.class_names.keys():
            for key in storage.all().keys():
                if my_key == key:
                    setattr(storage.all()[key], all_arg[2], all_arg[3])
                    storage.all()[key].save()
                    exist = True
                if exist is True:
                    break
            if exist is False:
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """This wont allow the last excecuted command to repeat
        when the ENTER key is pressed"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
