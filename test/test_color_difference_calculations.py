import unittest

from app.color_accessibility_calculations import ColorCalculations


class ColorDifferenceTests(unittest.TestCase):
    def setUp(self):
        self.difference = ColorCalculations()

    # Color difference tests
    def test_color_difference_less_than_500_returns_message(self):
        result = self.difference.calculate_color_difference([0, 0, 0], [0, 0, 0])
        self.assertEqual('Color difference is 0. Color difference MUST BE AT LEAST 500 to pass the standard.', result)

    def test_color_difference_greater_than_500_returns_message(self):
        result = self.difference.calculate_color_difference([255, 255, 0], [0, 0, 255])
        self.assertEqual('Color difference is 765. Color difference PASSES the standard.', result)

    def test_color_difference_is_500_returns_message(self):
        result = self.difference.calculate_color_difference([245, 0, 0], [0, 0, 255])
        self.assertEqual('Color difference is 500. Color difference PASSES the standard.', result)

    # Color brightness difference tests
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

    # Relative luminance tests
    def test_relative_luminance_returns_float(self):
        result = self.difference.calculate_relative_luminance([0, 0, 0])
        self.assertEqual(type(result), float)

    def test_relative_luminance_black_returns_0(self):
        result = self.difference.calculate_relative_luminance([0, 0, 0])
        self.assertEqual(result, 0.00)

    def test_relative_luminance_white_returns_1(self):
        result = self.difference.calculate_relative_luminance([255, 255, 255])
        self.assertEqual(result, 1.00)

    def test_relative_luminance_red_returns_0_2126(self):
        result = self.difference.calculate_relative_luminance([255, 0, 0])
        self.assertEqual(result, 0.2126)

    def test_relative_luminance_green_returns_0_7152(self):
        result = self.difference.calculate_relative_luminance([0, 255, 0])
        self.assertEqual(result, 0.7152)

    def test_relative_luminance_blue_returns_0_0722(self):
        result = self.difference.calculate_relative_luminance([0, 0, 255])
        self.assertEqual(result, 0.0722)

    def test_relative_luminance_pink_returns_0_2886(self):
        result = self.difference.calculate_relative_luminance([241, 93, 154])
        self.assertEqual(round(result, 4), 0.2886)

    # Contrast ratio tests
    def test_contrast_ratio_returns_float(self):
        result = self.difference.calculate_contrast_ratio(0.00, 1.00)
        self.assertEqual(type(result), float)

    def test_contrast_ratio_returns_float_with_two_places(self):
        result = self.difference.calculate_contrast_ratio(0.33, 1.00)
        result = str(result).split('.')[-1]
        self.assertEqual(len(result), 2)

    def test_contrast_ratio_black_and_white(self):
        result = self.difference.calculate_contrast_ratio(0.00, 1.00)
        self.assertEqual(result, 21.00)

    def test_contrast_ratio_black_and_red(self):
        result = self.difference.calculate_contrast_ratio(0.00, 0.2126)
        self.assertEqual(result, 5.25)

    def test_contrast_ratio_black_and_green(self):
        result = self.difference.calculate_contrast_ratio(0.00, 0.7152)
        self.assertEqual(result, 15.30)

    def test_contrast_ratio_black_and_blue(self):
        result = self.difference.calculate_contrast_ratio(0.00, 0.0722)
        self.assertEqual(result, 2.44)

    def test_contrast_ratio_black_and_pink(self):
        result = self.difference.calculate_contrast_ratio(0.00, 0.2886)
        self.assertEqual(result, 6.77)

    def test_contrast_ratio_red_and_white(self):
        result = self.difference.calculate_contrast_ratio(0.2126, 1.00)
        self.assertEqual(result, 4.00)

    def test_contrast_ratio_green_and_white(self):
        result = self.difference.calculate_contrast_ratio(0.7152, 1.00)
        self.assertEqual(result, 1.37)

    def test_contrast_ratio_blue_and_white(self):
        result = self.difference.calculate_contrast_ratio(0.0722, 1.00)
        self.assertEqual(result, 8.59)

    def test_contrast_ratio_pink_and_white(self):
        result = self.difference.calculate_contrast_ratio(0.2886, 1.00)
        self.assertEqual(result, 3.10)
