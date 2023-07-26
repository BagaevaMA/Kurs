from FuncFromCollectionDict import get_country
from FuncFromCollectionDict import get_unic_number
from FuncFromCollectionDict import get_count_queries

from unittest import TestCase

class TestGet_Country(TestCase):
    def test_with_russia(self):
        some_dict = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
        ]
        expected = [{'visit1': ['Москва', 'Россия']}]
        res = get_country(some_dict)
        self.assertEqual(res, expected, "Not equal")

    def test_len_russia(self):
        some_dict = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']}]

        expected = 1
        res = len(get_country(some_dict))
        self.assertGreater(res, expected, "Not equal")


    def test_ListEqual(self):
        some_dict = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
        ]
        expected = [{'visit1': ['Москва', 'Россия']}]
        res = get_country(some_dict)
        self.assertListEqual(res, expected)

class TestGet_unic_number(TestCase):

    def test_len_set(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}

        expected = 3
        res = len(get_unic_number(ids))
        self.assertGreater(res, expected, "Not equal")

    def test_with_set(self):

        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}

        expected = {98, 35, 15, 213, 54, 119}
        res = get_unic_number(ids)
        self.assertEqual(res, expected, "Not equal")


class TestGet_count_queries(TestCase):
    def test_sum_percent(self):
        queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
        expected = 100
        res = list(get_count_queries(queries).values())[0]+list(get_count_queries(queries).values())[1]
        self.assertEqual(res, expected, "Not equal")

    def test_dict_equal(self):
        queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
        expected = {3: 57.142857142857146, 2: 42.85714285714286}
        res = get_count_queries(queries)
        self.assertDictEqual(res, expected)
