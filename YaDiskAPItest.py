from YaDiskTestMain import create_folder

from unittest import TestCase

class TestYa_API(TestCase):
    def test_answer_server(self):
        expected = 201
        res = create_folder('Тест')
        self.assertEqual(res, expected, "Not equal")

    def test_repeat_create(self):
        expected = 409
        res = create_folder('Тест')
        self.assertEqual(res, expected, "Not equal")

    def test_answer_server2(self):
        expected = 200
        res = create_folder('Тест2')
        self.assertGreater(res, expected, "Not equal")