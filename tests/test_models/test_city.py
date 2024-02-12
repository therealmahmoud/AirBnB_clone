#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_new_inst(self):
        self.assertIn(City(), models.storage.all().values())

    def test_nO_aArgss(self):
        self.assertEqual(City, type(City()))

    def test_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_two_cities_ids(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    def test_upDATed_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(cy))
        self.assertNotIn("state_id", cy.__dict__)

    def test_name_attribute(self):
        cy = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(cy))
        self.assertNotIn("name", cy.__dict__)

    def test_intion_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_args_unused(self):
        cy = City(None)
        self.assertNotIn(None, cy.__dict__.values())


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the City class."""

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

    def test_sAveArg(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.save(None)

    def test_save_upfile(self):
        cy = City()
        cy.save()
        cyid = "City." + cy.id
        with open("file.json", "r") as f:
            self.assertIn(cyid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_dict_typee(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_to_dict_c_keys(self):
        cy = City()
        self.assertIn("id", cy.to_dict())
        self.assertIn("created_at", cy.to_dict())
        self.assertIn("updated_at", cy.to_dict())
        self.assertIn("__class__", cy.to_dict())

    def test_to_dict_attR(self):
        cy = City()
        cy.middle_name = "Holberton"
        cy.my_number = 98
        self.assertEqual("Holberton", cy.middle_name)
        self.assertIn("my_number", cy.to_dict())

    def test_toDict_output(self):
        dt = datetime.today()
        cy = City()
        cy.id = "123456"
        cy.created_at = cy.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(cy.to_dict(), tdict)

    def test_to_dict_argsS(self):
        cy = City()
        with self.assertRaises(TypeError):
            cy.to_dict(None)

    def test_contrast_to_dictDUNDdict(self):
        cy = City()
        self.assertNotEqual(cy.to_dict(), cy.__dict__)


if __name__ == "__main__":
    unittest.main()
