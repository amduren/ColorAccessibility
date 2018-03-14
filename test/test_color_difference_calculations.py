import unittest

from app.color_accessibility_calculations import ColorCalculations


class ColorDifferenceTests(unittest.TestCase):
    def setUp(self):
        self.difference = ColorCalculations()

    def test_color_difference_less_than_500_returns_message(self):
        result = self.difference.calculate_color_difference([0, 0, 0], [0, 0, 0])
        self.assertEqual('Color difference is 0. Color difference MUST BE AT LEAST 500 to pass the standard.', result)

    def test_color_difference_greater_than_500_returns_message(self):
        result = self.difference.calculate_color_difference([255, 255, 0], [0, 0, 255])
        self.assertEqual('Color difference is 765. Color difference PASSES the standard.', result)

    def test_color_difference_is_500_returns_message(self):
        result = self.difference.calculate_color_difference([245, 0, 0], [0, 0, 255])
        self.assertEqual('Color difference is 500. Color difference PASSES the standard.', result)

    def test_color_brightness_difference_less_than_125_returns_message(self):
        result = self.difference.calculate_color_brightness_difference([0, 0, 0], [0, 0, 0])
        self.assertEqual('Color brightness difference is 0.0. Color brightness difference MUST BE AT LEAST 125 to '
                         + 'pass the standard.', result)

    def test_color_brightness_difference_greater_than_125_returns_message(self):
        result = self.difference.calculate_color_brightness_difference([255, 255, 0], [0, 0, 255])
        self.assertEqual('Color brightness difference is 196.86. Color brightness PASSES the standard.', result)

    def test_color_brightness_difference_is_125_returns_message(self):
        result = self.difference.calculate_color_brightness_difference([254, 133, 0], [0, 0, 254])
        self.assertEqual('Color brightness difference is 125.06. Color brightness PASSES the standard.', result)

    def test_relative_luminance_returns_float(self):
        result = self.difference.calculate_relative_luminance([0, 0, 0])
        self.assertEqual(type(result), float)

    def test_relative_luminance_returns_0(self):
        result = self.difference.calculate_relative_luminance([0, 0, 0])
        self.assertEqual(result, 0.00)

    def test_relative_luminance_returns_1(self):
        result = self.difference.calculate_relative_luminance([255, 255, 255])
        self.assertEqual(result, 1.00)

    def test_relative_luminance_returns_0_2126(self):
        result = self.difference.calculate_relative_luminance([255, 0, 0])
        self.assertEqual(result, 0.2126)

    def test_relative_luminance_returns_0_7152(self):
        result = self.difference.calculate_relative_luminance([0, 255, 0])
        self.assertEqual(result, 0.7152)

    def test_relative_luminance_returns_0_0722(self):
        result = self.difference.calculate_relative_luminance([0, 0, 255])
        self.assertEqual(result, 0.0722)

    def test_relative_luminance_returns_0_2886(self):
        result = self.difference.calculate_relative_luminance([241, 93, 154])
        self.assertEqual(round(result, 4), 0.2886)
