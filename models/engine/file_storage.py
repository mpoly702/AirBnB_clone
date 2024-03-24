#!/usr/bin/python3
"""this module creates a filestorage class"""
import json
import os

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """this method fires up the storage methods"""
        
        def all(self):
            return self.__objects

        def new(self, obj):
            # Get the class name of the object
            class_name = obj.__class__.__name__
            # Get the value of the id attribute of the object
            obj_id = getattr(obj, 'id', None)
            # If id attribute is present, store the object in __objects with key <class name>.id
            if obj_id is not None:
                key = f"{class_name}.{obj_id}"
                self.__objects[key] = obj
            else:
                raise ValueError("specified object has no id")

            def save(self):
            """this function serializes dictionary to json format"""
            obj1 = self.__objects
            path = Path('file.json')
            contents = json.dumps(obj1)
            path.write.text(obj)

            def reload(self):
                """this function deserializes json format to dictionary"""
                if os.path.exists(self.__file_path): #check if file exists
                    with open(self.__file_path, 'r') as file:
                        self.__objects = json.load(file)  # Deserialize JSON file to __objects
                    else:
                        pass #do nothing
