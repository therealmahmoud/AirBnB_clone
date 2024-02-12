#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_idPublicStr(self):
        self.assertEqual(str, type(Amenity().id))

    def test_no_arguments_input(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_newInstance(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_updated_atDateTime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_isClassAttribute(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_TwoUniqueIds(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_TwoDifferent_updated_at(self):
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_InstantiationNoneKwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_ArgumentsUnused(self):
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_SaveUpdatesFile(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())

    def test_TwoSaves(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_OneSave(self):
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_SaveArguments(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_DictType(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_Dict_ContainsKeys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_ContainsAddedAttributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_arguments(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)

    def test_Contrast_to_dict_DunderDict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)


if __name__ == "__main__":
    unittest.main()
