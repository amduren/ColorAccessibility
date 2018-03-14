import unittest

from app.convert_to_rgb import ConvertToRgb


class HexToRgbTests(unittest.TestCase):
    def setUp(self):
        self.color = ConvertToRgb()

    def test_hex_string_with_hash_returns_rgb_list_length_3(self):
        result = self.color.convert_hex_to_rgb('#50068F')
        self.assertEqual(len(result), 3)

    def test_hex_string_without_hash_returns_rgb_list_length_3(self):
        result = self.color.convert_hex_to_rgb('50068F')
        self.assertEqual(len(result), 3)

    def test_hex_string_with_hash_returns_rgb_list_with_all_int_values(self):
        result = self.color.convert_hex_to_rgb('#50068F')
        self.assertEqual(type(result[0]), int)
        self.assertEqual(type(result[1]), int)
        self.assertEqual(type(result[2]), int)

    def test_hex_string_without_hash_returns_rgb_list_with_all_int_values(self):
        result = self.color.convert_hex_to_rgb('50068F')
        self.assertEqual(type(result[0]), int)
        self.assertEqual(type(result[1]), int)
        self.assertEqual(type(result[2]), int)

    def test_hex_black(self):
        result = self.color.convert_hex_to_rgb('000000')
        self.assertEqual(result, [0, 0, 0])

    def test_hex_white(self):
        result = self.color.convert_hex_to_rgb('#FFFFFF')
        self.assertEqual(result, [255, 255, 255])

    def test_hex_red(self):
        result = self.color.convert_hex_to_rgb('FF0000')
        self.assertEqual(result, [255, 0, 0])

    def test_hex_green(self):
        result = self.color.convert_hex_to_rgb('#00ff00')
        self.assertEqual(result, [0, 255, 0])

    def test_hex_blue(self):
        result = self.color.convert_hex_to_rgb('0000ff')
        self.assertEqual(result, [0, 0, 255])

    def test_hex_pink(self):
        result = self.color.convert_hex_to_rgb('#f15d9A')
        self.assertEqual(result, [241, 93, 154])
