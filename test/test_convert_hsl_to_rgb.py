import unittest

from app.convert_to_rgb import ConvertToRgb


class HslToRgbTests(unittest.TestCase):
    def setUp(self):
        self.color = ConvertToRgb()

    def test_hue_value_less_than_0_returns_message(self):
        result = self.color.convert_hsl_to_rgb(-50, 0.50, 0.25)
        self.assertEqual(result, 'Hue must be between 0 and 360.')

    def test_hue_value_greater_than_360_returns_message(self):
        result = self.color.convert_hsl_to_rgb(450, 0.50, 0.25)
        self.assertEqual(result, 'Hue must be between 0 and 360.')

    def test_saturation_value_less_than_0_returns_message(self):
        result = self.color.convert_hsl_to_rgb(180, -0.50, 0.25)
        self.assertEqual(result, 'Saturation must be between 0 and 1.')

    def test_saturation_value_greater_than_1_returns_message(self):
        result = self.color.convert_hsl_to_rgb(180, 1.50, 0.25)
        self.assertEqual(result, 'Saturation must be between 0 and 1.')
        
    def test_luminance_value_less_than_0_returns_message(self):
        result = self.color.convert_hsl_to_rgb(180, 0.50, -0.25)
        self.assertEqual(result, 'Luminance must be between 0 and 1.')

    def test_luminance_value_greater_than_1_returns_message(self):
        result = self.color.convert_hsl_to_rgb(180, 0.50, 1.25)
        self.assertEqual(result, 'Luminance must be between 0 and 1.')

    def test_saturation_value_of_0_returns_rgb_list_with_all_values_equal(self):
        result = self.color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(result[0], result[1])
        self.assertEqual(result[1], result[2])

    def test_saturation_value_of_0_returns_rgb_list_with_all_values_equal_255x_luminance(self):
        result = self.color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(result[0], 102)    # 0.40 * 255 = 102
        self.assertEqual(result[1], 102)    # 0.40 * 255 = 102
        self.assertEqual(result[2], 102)    # 0.40 * 255 = 102

    def test_rgb_list_has_length_3(self):
        result = self.color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(len(result), 3)

    def test_hsl_black(self):
        result = self.color.convert_hsl_to_rgb(0, 0.0, 0.0)
        self.assertEqual(result, [0, 0, 0])

    def test_hsl_white(self):
        result = self.color.convert_hsl_to_rgb(0, 0.0, 1.0)
        self.assertEqual(result, [255, 255, 255])

    def test_hsl_red(self):
        result = self.color.convert_hsl_to_rgb(0, 1.0, 0.5)
        self.assertEqual(result, [255, 0, 0])

    def test_hsl_green(self):
        result = self.color.convert_hsl_to_rgb(120, 1.0, 0.5)
        self.assertEqual(result, [0, 255, 0])

    def test_hsl_blue(self):
        result = self.color.convert_hsl_to_rgb(240, 1.0, 0.5)
        self.assertEqual(result, [0, 0, 255])

    def test_hsl_pink(self):
        result = self.color.convert_hsl_to_rgb(335, 0.84, 0.65)
        self.assertEqual(result, [241, 91, 152])
