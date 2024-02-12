#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_inSt(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""


    def testFileStorage_objectsPrivatediCt(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_FileStorage_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initiaL(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_filePathPrivate_string(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_No_Args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

class TestFileStorage_methds(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_ALL_Arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_ALL(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_NEWW(self):
        Basemodell = BaseModel()
        us = User()
        st = State()
        pl = Place()
        CitY = City()
        AmenItyy = Amenity()
        REview = Review()
        models.storage.new(Basemodell)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(CitY)
        models.storage.new(AmenItyy)
        models.storage.new(REview)
        self.assertIn("BaseModel." + Basemodell.id, models.storage.all().keys())
        self.assertIn(Basemodell, models.storage.all().values())
        self.assertIn("User." + us.id, models.storage.all().keys())
        self.assertIn(us, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + pl.id, models.storage.all().keys())
        self.assertIn(pl, models.storage.all().values())
        self.assertIn("City." + CitY.id, models.storage.all().keys())
        self.assertIn(CitY, models.storage.all().values())
        self.assertIn("Amenity." + AmenItyy.id, models.storage.all().keys())
        self.assertIn(AmenItyy, models.storage.all().values())
        self.assertIn("Review." + REview.id, models.storage.all().keys())
        self.assertIn(REview, models.storage.all().values())

    def test_NEWarGs(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_RELOAd(self):
        Basemodell = BaseModel()
        us = User()
        st = State()
        pl = Place()
        CitY = City()
        AmenItyy = Amenity()
        REview = Review()
        models.storage.new(Basemodell)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(CitY)
        models.storage.new(AmenItyy)
        models.storage.new(REview)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + Basemodell.id, objs)
        self.assertIn("User." + us.id, objs)
        self.assertIn("State." + st.id, objs)
        self.assertIn("Place." + pl.id, objs)
        self.assertIn("City." + CitY.id, objs)
        self.assertIn("Amenity." + AmenItyy.id, objs)
        self.assertIn("Review." + REview.id, objs)

    def test_SAvee(self):
        Basemodell = BaseModel()
        us = User()
        st = State()
        pl = Place()
        CitY = City()
        AmenItyy = Amenity()
        REview = Review()
        models.storage.new(Basemodell)
        models.storage.new(us)
        models.storage.new(st)
        models.storage.new(pl)
        models.storage.new(CitY)
        models.storage.new(AmenItyy)
        models.storage.new(REview)
        models.storage.save()
        save_text = ""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + Basemodell.id, save_text)
            self.assertIn("User." + us.id, save_text)
            self.assertIn("State." + st.id, save_text)
            self.assertIn("Place." + pl.id, save_text)
            self.assertIn("City." + CitY.id, save_text)
            self.assertIn("Amenity." + AmenItyy.id, save_text)
            self.assertIn("Review." + REview.id, save_text)

    def test_REALOadArg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_sAveArg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)


if __name__ == "__main__":
    unittest.main()
