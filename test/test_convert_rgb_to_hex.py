import unittest

from app.convert_to_hex import ConvertToHex


class RgbToHexTests(unittest.TestCase):
    def setUp(self):
        self.color = ConvertToHex()

    def test_rgb_list_returns_string_length_7(self):
        result = self.color.convert_rgb_to_hex([0, 15, 150])
        self.assertEqual(len(result), 7)

    def test_rgb_list_returns_string(self):
        result = self.color.convert_rgb_to_hex([255, 205, 155])
        self.assertEqual(type(result), str)

    def test_rgb_list_returns_string_with_first_char_as_hash(self):
        result = self.color.convert_rgb_to_hex([255, 205, 155])
        self.assertEqual(result[0], '#')

    def test_rgb_list_returns_string_with_all_non_first_char_as_0_to_9_or_a_to_f(self):
        result = self.color.convert_rgb_to_hex([255, 205, 155])
        for char in range(1, len(result)):
            self.assertTrue(result[char] in '0123456789ABCDEF')

    def test_rgb_black(self):
        result = self.color.convert_rgb_to_hex([0, 0, 0])
        self.assertEqual(result, '#000000')

    def test_rgb_white(self):
        result = self.color.convert_rgb_to_hex([255, 255, 255])
        self.assertEqual(result, '#FFFFFF')

    def test_rgb_red(self):
        result = self.color.convert_rgb_to_hex([255, 0, 0])
        self.assertEqual(result, '#FF0000')

    def test_rgb_green(self):
        result = self.color.convert_rgb_to_hex([0, 255, 0])
        self.assertEqual(result, '#00FF00')

    def test_rgb_blue(self):
        result = self.color.convert_rgb_to_hex([0, 0, 255])
        self.assertEqual(result, '#0000FF')

    def test_rgb_pink(self):
        result = self.color.convert_rgb_to_hex([241, 93, 154])
        self.assertEqual(result, '#F15D9A')
