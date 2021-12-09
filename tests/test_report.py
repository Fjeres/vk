import os
from report import Collector, CSV_format, JSON_format, TSV_format
import unittest
from user_model import User




class TestReport(unittest.TestCase):

    def test_CSV_format(self):
        user = User()
        path = 'test_folder'
        user.name = 'Test'
        user.last_name = 'Test'
        user.country = {'id': 1, 'title': "Rus"}
        user.city = {'id': 1, 'title': "Tomsk"}
        user.birthday = '9.5.1991'
        user.sex = 1
        user_list = [user]
        fields = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex', ]
        collector = Collector(CSV_format(data=user_list, fields=fields, id=1, path=path))
        collector.make_report()
        self.assertEqual(os.path.exists('test_folder/1.csv'), True)
        os.remove("test_folder/1.csv")

    def test_JSON_format(self):
        user = User()
        path = 'test_folder'
        user.name = 'Test'
        user.last_name = 'Test'
        user.country = {'id': 1, 'title': "Rus"}
        user.city = {'id': 1, 'title': "Tomsk"}
        user.birthday = '9.5.1991'
        user.sex = 1
        user_list = [user]
        fields = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex', ]
        collector = Collector(JSON_format(data=user_list, fields=fields, id=1, path=path))
        collector.make_report()
        self.assertEqual(os.path.exists('test_folder/1.json'), True)
        os.remove("test_folder/1.json")

    def test_TSV_format(self):
        user = User()
        path = 'test_folder'
        user.name = 'Test'
        user.last_name = 'Test'
        user.country = {'id': 1, 'title': "Rus"}
        user.city = {'id': 1, 'title': "Tomsk"}
        user.birthday = '9.5.1991'
        user.sex = 1
        user_list = [user]
        fields = ['first_name', 'last_name', 'country', 'city', 'bdate', 'sex', ]
        collector = Collector(TSV_format(data=user_list, fields=fields, id=1, path=path))
        collector.make_report()
        self.assertEqual(os.path.exists('test_folder/1.tsv'), True)
        os.remove("test_folder/1.tsv")