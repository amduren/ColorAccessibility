import unittest

from app.utilities.utilities import map_char_to_int, map_int_to_char


class UtilitiesTests(unittest.TestCase):

    def test_length_string_of_chars_less_than_length_list_of_ints_returns_message(self):
        result = map_char_to_int('a', 'abc', range(5))
        self.assertEqual(result, 'Not enough characters to map to an integer.')

    def test_length_string_of_chars_greater_than_length_list_of_ints_returns_message(self):
        result = map_char_to_int('a', 'abcdef', range(5))
        self.assertEqual(result, 'Too many characters to map to an integer.')

    def test_char_not_in_string_of_chars_returns_message(self):
        result = map_char_to_int('z', 'abcde', range(5))
        self.assertEqual(result, 'Character not in string of characters.')

    def test_char_in_string_of_chars_returns_int(self):
        result = map_char_to_int('a', 'abc', range(3))
        self.assertEqual(type(result), int)

    def test_char_in_string_of_chars(self):
        result = map_char_to_int('a', 'abc', range(3))
        self.assertEqual(result, 0)

    def test_length_list_of_ints_less_than_length_string_of_chars_returns_message(self):
        result = map_int_to_char(4, range(5), 'abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(result, 'Not enough integers to map to a character.')

    def test_length_list_of_ints_greater_than_length_string_of_chars_returns_message(self):
        result = map_int_to_char(1, range(5), 'abc')
        self.assertEqual(result, 'Too many integers to map to a character.')

    def test_int_not_in_list_of_ints_returns_message(self):
        result = map_int_to_char(9, range(10, 16), 'abcdef')
        self.assertEqual(result, 9)     # return integer

    def test_int_in_list_of_ints_returns_char(self):
        result = map_int_to_char(0, range(3), 'abc')
        self.assertEqual(type(result), str)     # character should be a string

    def test_int_in_list_of_ints(self):
        result = map_int_to_char(2, range(1, 4), 'abc')
        self.assertEqual(result, 'b')
