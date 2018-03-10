import unittest

from app.color_accessibility_calculations import ColorCalculations


class ColorDifferenceTests(unittest.TestCase):

    def test_color_difference_less_than_500_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_difference([0, 0, 0], [0, 0, 0])
        self.assertEqual('Color difference is 0. Color difference must be at least 500 to pass.', result)

    def test_color_difference_greater_than_500_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_difference([255, 255, 0], [0, 0, 255])
        self.assertEqual('Color difference is 765. Color difference is sufficient.', result)

    def test_color_difference_is_500_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_difference([245, 0, 0], [0, 0, 255])
        self.assertEqual('Color difference is 500. Color difference is sufficient.', result)

    def test_color_brightness_difference_less_than_125_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_brightness_difference([0, 0, 0], [0, 0, 0])
        self.assertEqual('Color brightness difference is 0.0. Color brightness difference must be at least 125 to '
                         + 'pass.', result)

    def test_color_brightness_difference_greater_than_125_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_brightness_difference([255, 255, 0], [0, 0, 255])
        self.assertEqual('Color brightness difference is 196.86. Color brightness is sufficient.', result)

    def test_color_brightness_difference_is_125_returns_message(self):
        difference = ColorCalculations()
        result = difference.calculate_color_brightness_difference([254, 133, 0], [0, 0, 254])
        self.assertEqual('Color brightness difference is 125.06. Color brightness is sufficient.', result)