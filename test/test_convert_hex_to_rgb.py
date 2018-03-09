import unittest

from app.convert_to_rgb import ConvertToRgb


class HexToRgbTests(unittest.TestCase):

    def test_hex_string_with_hash_returns_rgb_list_length_3(self):
        color = ConvertToRgb()
        result = color.convert_hex_to_rgb('#50068F')
        self.assertEqual(len(result), 3)

    def test_hex_string_without_hash_returns_rgb_list_length_3(self):
        color = ConvertToRgb()
        result = color.convert_hex_to_rgb('50068F')
        self.assertEqual(len(result), 3)

    def test_hex_string_with_hash_returns_rgb_list_with_all_int_values(self):
        color = ConvertToRgb()
        result = color.convert_hex_to_rgb('#50068F')
        self.assertEqual(type(result[0]), int)
        self.assertEqual(type(result[1]), int)
        self.assertEqual(type(result[2]), int)
