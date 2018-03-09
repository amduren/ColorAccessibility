import unittest

from app.convert_to_rgb import ConvertToRgb


class HslToRgbTests(unittest.TestCase):

    def test_hue_value_less_than_0_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(-50, 0.50, 0.25)
        self.assertEqual('Hue must be between 0 and 360.', result)

    def test_hue_value_greater_than_360_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(450, 0.50, 0.25)
        self.assertEqual('Hue must be between 0 and 360.', result)

    def test_saturation_value_less_than_0_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, -0.50, 0.25)
        self.assertEqual('Saturation must be between 0 and 1.', result)

    def test_saturation_value_greater_than_1_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 1.50, 0.25)
        self.assertEqual('Saturation must be between 0 and 1.', result)
        
    def test_luminance_value_less_than_0_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 0.50, -0.25)
        self.assertEqual('Luminance must be between 0 and 1.', result)

    def test_luminance_value_greater_than_1_returns_message(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 0.50, 1.25)
        self.assertEqual('Luminance must be between 0 and 1.', result)

    def test_saturation_value_of_0_returns_rgb_list_with_all_values_equal(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(result[0], result[1])
        self.assertEqual(result[1], result[2])

    def test_saturation_value_of_0_returns_rgb_list_with_all_values_equal_255x_luminance(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(result[0], 102)    # 0.40 * 255 = 102

    def test_rgb_list_has_length_3(self):
        color = ConvertToRgb()
        result = color.convert_hsl_to_rgb(180, 0.00, 0.40)
        self.assertEqual(len(result), 3)
