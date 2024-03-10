#!/usr/bin/python3
"""
This module contains entry point of a command interpreter
"""
import ast
import cmd
from datetime import datetime
from importlib import import_module
from models.engine.file_storage import FileStorage


class HBNBUtility:
    """
    A class that provides utility methods for working with module
    names and importing modules dynamically.
    """

    @staticmethod
    def attain_module(mod_name: str, root='models'):
        """
        This method helps us attain the module name.
        """
        try:
            module = import_module(root + '.' + mod_name)
            return module
        except(AttributeError, ModuleNotFoundError):
            return None

    @staticmethod
    def module_format(name: str):
        """
        This method helps us get the format of the module.
        """
        return 'base_model' if name == 'BaseModel' else str(name).lower()


class HBNBAmenity:
    """
    An Amenity class that helps manage entities.
    """
    storage = FileStorage()

    def __attain_module(self, arg):
        """
        This method helps us get a module using the methods from
        HBNBUtility
        """
        mod_name = HBNBUtility.module_format(arg)
        mod = HBNBUtility.attain_module(mod_name)
        return mod if mod else None

    def __get_instance(self, module, cls_name):
        """This method helps us get the instance id"""
        entity = None
        try:
            entity = getattr(module, cls_name)
        except AttributeError:
            print("** class doesn't exist **")
            return None
        inst = entity()
        inst.save()
        return inst.id

    def create(self, clas):
        """
        Create a new model
        """
        mod = self.__attain_module(clas)
        if mod is None:
            print("** class doesn't exist **")
            return None
        else:
            mod_id = self.__get_instance(mod, clas)
            return mod_id if mod_id else None

    def get_model_by_id(self, cls_name, mod_id):
        """
        Prints the string rep of an instance.
        """
        mod = self.__attain_module(cls_name)
        if mod:
            if hasattr(mod, cls_name):
                key = '.'.join([cls_name, mod_id])
                model = self.storage.all().get(key)
                if model is None:
                    print("** no instance found **")
                    return
                return model
            else:
                print("** class doesn't exist **")
                return None
        else:
            print("** class doesn't exist **")
            return None

    def __discard_instance(self, model, cls_id):
        """This method helps us delete an instance."""
        key = '.'.join([model, cls_id])
        if self.storage.all().get(key) is None:
            print("** no instance found **")
            return
        del self.storage.all()[key]
        self.storage.save()

    def discard_model_by_id(self, model, cls_id):
        """Remove an instance by it's ID
        Args:
            model (str): The instance's class name
            cls_id (str): The instance's ID
        """
        mod = self.__attain_module(model)
        if mod is not None and hasattr(mod, model):
            self.__discard_instance(model, cls_id)
            return
        else:
            print("** class doesn't exist **")
            return

    def get_all(self, cls_name):
        """
        Lists all models of a class
        Args:
            cls_name (str): The insstance's class name.
        """
        mod = self.__attain_module(cls_name)
        if mod:
            if not hasattr(mod, cls_name):
                print("** class doesn't exist **")
            else:
                model = self.storage.all()
                return [str(i) for i in model.values()
                        if i.__class__.__name__ == cls_name]
        else:
            print("** class doesn't exist **")

    def update_model_with_attr(self, cls_name, cls_id, attr, val):
        """Update a model's Data
        Args:
            cls_name (str): The instance's class name
            cls_id (str): The instance's ID
            attr (str): The attribute to be updated.
            val (str): The value for the attribute
        """
        mod = self.__attain_module(cls_name)
        if mod and hasattr(mod, cls_name):
            key = '.'.join([cls_name, cls_id])
            inst = self.storage.all().get(key)
            if inst:
                inst.__setattr__(attr, val)
                inst.updated_at = datetime.now()
                self.storage.all()[key] = inst
                self.storage.save()
                return inst
            else:
                print("** no instance found **")
                return None
        else:
            print("** class doesn't exist **")
            return None


class HBNBCommand(cmd.Cmd):
    """
    A class that is the entry point of a command interpreter
    """
    prompt = "(hbnb) "
    bnbAmenity = HBNBAmenity()

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """Initializes this class.
        Args:
            completekey: the readline name of a completion key,
            Defaults to Tab.
            stdin: specifies the input file object, Defaults to None
            stdout: specifies the output file object, Defaults to None
        """
        super().__init__(completekey, stdin, stdout)

    def do_EOF(self, arg):
        """EOF command(ctrl-D) to quit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, *arg):
        """Creates an instance of a class"""
        arg1 = (str(arg[0]).split(' '))
        if len(arg1) < 1 or arg[0] == "":
            print("** class name missing **")
            return
        ins_id = self.bnbAmenity.create(arg1[0])
        if ins_id:
            print(ins_id)
            return

    def do_show(self, *arg):
        """Prints the string rep of an instance."""
        args = (str(arg[0]).split(' '))
        model, cls_id = None, None
        try:
            model = args[0]
            cls_id = args[1]
        except (ValueError, IndexError):
            if len(model) == 0 or model == '':
                print("** class name missing **")
                return
            if cls_id is None or len(cls_id) == 0:
                print("** instance id missing **")
                return
        res = self.bnbAmenity.get_model_by_id(model, cls_id)
        if res:
            print(res)

    def do_destroy(self, *arg):
        """Deletes an instance based on class name and ID"""
        args = (str(arg[0]).split(' '))
        model, cls_id = None, None
        try:
            model = args[0]
            cls_id = args[1]
        except (IndexError, ValueError):
            if model == '' or len(model) == 0:
                print("** class name missing **")
                return
            if cls_id is None or len(cls_id) == 0:
                print("** instance id  missing **")
                return
        return self.bnbAmenity.discard_model_by_id(model, cls_id)

    def do_all(self, arg):
        """Prints all string rep of all instances"""
        if not arg:
            lst = self.bnbAmenity.storage.all().values()
            print([str(i) for i in lst])
            return
        args = (str(arg).split(' '))
        res = self.bnbAmenity.get_all(args[0])
        if res and len(res) > 0:
            print(res)

    def do_update(self, *arg):
        """Updates an instance"""
        args = (str(arg[0]).split(' '))
        cls_name, cls_id = None, None
        attr, val = None, None
        try:
            cls_name = args[0]
            cls_id = args[1]
            attr = args[2]
            val = ast.literal_eval(args[3])
        except (ValueError, IndexError):
            if cls_name is None or len(cls_name) == 0:
                print("** class name missing **")
                return
            if cls_id is None or len(cls_id) == 0:
                print("** instance id missing **")
                return
            if attr is None or len(attr) == 0:
                print("** attribute name missing **")
                return
            if val is None or len(val) == 0:
                print("** value missing **")
                return
        res = self.bnbAmenity.update_model_with_attr(cls_name,
                                                     cls_id, attr, val)
        if res is None:
            return

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
