import unittest

from app.utilities.utilities import map_char_to_int


class UtilitiesTests(unittest.TestCase):

    def test_length_string_of_chars_less_than_length_list_of_ints_returns_message(self):
        result = map_char_to_int('a', 'abc', range(5))
        self.assertEqual('Not enough characters to map to an integer.', result)

    def test_length_string_of_chars_greater_than_length_list_of_ints_returns_message(self):
        result = map_char_to_int('a', 'abcdef', range(5))
        self.assertEqual('Too many characters to map to an integer.', result)

    def test_char_not_in_string_of_chars_returns_message(self):
        result = map_char_to_int('z', 'abcde', range(5))
        self.assertEqual('Character not in string of characters.', result)

    def test_char_in_string_of_chars_returns_int(self):
        result = map_char_to_int('a', 'abc', range(3))
        self.assertEqual(type(result), int)

    def test_char_in_string_of_chars(self):
        result = map_char_to_int('a', 'abc', range(3))
        self.assertEqual(0, result)
