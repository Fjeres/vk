from user_model import User

import unittest


class TestUserModel(unittest.TestCase):

    def test_GetAndSet(self):
        user = User()
        user.name = 'Test'
        user.last_name = 'Test'
        user.country = {'id': 1, 'title': "Rus"}
        user.city = {'id': 1, 'title': "Tomsk"}
        user.birthday = '9.5.1991'
        user.sex = 1

        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.last_name, 'Test')
        self.assertEqual(user.country, 'Rus')
        self.assertEqual(user.city, 'Tomsk')
        self.assertEqual(user.birthday, '1991-05-09')
        self.assertEqual(user.sex, 'Ж')
        user.sex = 2
        self.assertEqual(user.sex, 'М')

    def test_data_normalization(self):
        user = User()
        user_dict = {
            'first_name': "Test",
            'last_name': "Test",
            'bdate': '9.5.1991',
            'sex': 1,
            'country': {'id': 1, 'title': "Rus"},
            'city': {'id': 1, 'title': "Tomsk"},
        }
        user.data_normalization(user_dict)

        self.assertEqual(user.name, 'Test')
        self.assertEqual(user.last_name, 'Test')
        self.assertEqual(user.country, 'Rus')
        self.assertEqual(user.city, 'Tomsk')
        self.assertEqual(user.birthday, '1991-05-09')
        self.assertEqual(user.sex, 'Ж')

    def test_sorting(self, ):
        user_list = []
        name_list = ['Dima', 'Max', 'Anton', 'Petr']
        sort_name_list = ["Anton", 'Dima', 'Max', 'Petr']
        for i in range(4):
            user = User()
            user.name = name_list[i]
            user.last_name = 'Test'
            user.country = {'id': 1, 'title': "Rus"}
            user.city = {'id': 1, 'title': "Tomsk"}
            user.birthday = '9.5.1991'
            user.sex = 1
            user_list.append(user)

        user_list = user_list[0].sorting(user_list)

        for i in range(4):
            self.assertEqual(user_list[i].name, sort_name_list[i])


