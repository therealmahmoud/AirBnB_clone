#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_NewInstanceInObjects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_NoArgumentsInPut(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_IdStr(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_updated_at_DateTime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_created_at_DateTime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_TwoModelsDifferent_created_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.created_at, basemodel2.created_at)

    def test_TwoUniqueIds(self):
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)

    def test_InPutNoneKwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_ArgumentsUnused(self):
        basemodel = BaseModel(None)
        self.assertNotIn(None, basemodel.__dict__.values())

    def test_TwoModelsDifferent_updated_at(self):
        basemodel1 = BaseModel()
        sleep(0.05)
        basemodel2 = BaseModel()
        self.assertLess(basemodel1.updated_at, basemodel2.updated_at)

    def test_InPutKwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        basemodel = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, dt)
        self.assertEqual(basemodel.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

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

    def test_SaveUpdates(self):
        basemodel = BaseModel()
        basemodel.save()
        bmid = "BaseModel." + basemodel.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_SaveArguments(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.save(None)

    def test_OneSave(self):
        basemodel = BaseModel()
        sleep(0.05)
        first_updated_at = basemodel.updated_at
        basemodel.save()
        self.assertLess(first_updated_at, basemodel.updated_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_ToDictDateTimeAttributesStrs(self):
        basemodel = BaseModel()
        bm_dict = basemodel.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_ToDictType(self):
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_to_dictContainsAttributes(self):
        basemodel = BaseModel()
        basemodel.name = "Holberton"
        basemodel.my_number = 98
        self.assertIn("name", basemodel.to_dict())
        self.assertIn("my_number", basemodel.to_dict())

    def test_ToDictArguments(self):
        basemodel = BaseModel()
        with self.assertRaises(TypeError):
            basemodel.to_dict(None)

    def test_ToDictDunderDict(self):
        basemodel = BaseModel()
        self.assertNotEqual(basemodel.to_dict(), basemodel.__dict__)


if __name__ == "__main__":
    unittest.main()
