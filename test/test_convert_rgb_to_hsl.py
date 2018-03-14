import unittest

from app.convert_to_hsl import ConvertToHsl


class RgbToHslTests(unittest.TestCase):
    def setUp(self):
        self.color = ConvertToHsl()

    def test_rgb_list_returns_hsl_length_3(self):
        result = self.color.convert_rgb_to_hsl([0, 100, 200])
        self.assertEqual(len(result), 3)

    def test_rgb_list_returns_hsl_with_hue_int_value(self):
        result = self.color.convert_rgb_to_hsl([0, 100, 150])
        self.assertEqual(type(result[0]), int)

    def test_rgb_list_returns_hsl_with_saturation_float_value(self):
        result = self.color.convert_rgb_to_hsl([0, 100, 150])
        self.assertEqual(type(result[1]), float)

    def test_rgb_list_returns_hsl_with_luminance_float_value(self):
        result = self.color.convert_rgb_to_hsl([150, 100, 0])
        self.assertEqual(type(result[2]), float)

    def test_rgb_list_returns_hsl_with_saturation_float_value_with_2_places(self):
        result = self.color.convert_rgb_to_hsl([50, 100, 100])
        result = str(result[1]).split('.')[-1]
        self.assertEqual(len(result), 2)

    def test_rgb_list_returns_hsl_with_luminance_float_value_with_2_places(self):
        result = self.color.convert_rgb_to_hsl([50, 100, 100])
        result = str(result[2]).split('.')[-1]
        self.assertEqual(len(result), 2)

    def test_hsl_for_black(self):
        result = self.color.convert_rgb_to_hsl([0, 0, 0])
        self.assertEqual(result, [0, 0.0, 0.0])

    def test_hsl_for_white(self):
        result = self.color.convert_rgb_to_hsl([255, 255, 255])
        self.assertEqual(result, [0, 0.0, 1.0])

    def test_hsl_for_red(self):
        result = self.color.convert_rgb_to_hsl([255, 0, 0])
        self.assertEqual(result, [0, 1.0, 0.5])

    def test_hsl_for_green(self):
        result = self.color.convert_rgb_to_hsl([0, 255, 0])
        self.assertEqual(result, [120, 1.0, 0.5])

    def test_hsl_for_blue(self):
        result = self.color.convert_rgb_to_hsl([0, 0, 255])
        self.assertEqual(result, [240, 1.0, 0.5])

    def test_hsl_for_gold(self):
        result = self.color.convert_rgb_to_hsl([255, 215, 0])
        self.assertEqual(result, [51, 1.0, 0.5])
