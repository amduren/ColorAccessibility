import unittest

from app.color_recommendations import ColorRecommendations


class ColorRecommendationTests(unittest.TestCase):
    def setUp(self):
        self.recommendations = ColorRecommendations()

    def test_color_recommendations_for_300_contrast_lighter_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([0, 0, 255], 0.0722, 3.00)
        expected_message = 'Required relative luminance for sufficient contrast of darker colors must be between 0' \
                           ' and 1 with color: rgb(0, 0, 255).\nAlso colors with values of 153 - 255 for each of RGB' \
                           ' in rgb(red, green, blue) will pass the WCAG 2.0 AA 18pt+ standard with color: ' \
                           'rgb(0, 0, 255).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_300_contrast_darker_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([255, 255, 255], 1.00, 3.00)
        expected_message = 'Colors with values of 0 - 148 for each of RGB in rgb(red, green, blue) will pass the ' \
                           'WCAG 2.0 AA 18pt+ standard with color: rgb(255, 255, 255).\nRequired relative luminance' \
                           ' for sufficient contrast of lighter colors must be between 0 and 1 with color: ' \
                           'rgb(255, 255, 255).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_300_contrast_lighter_and_darker(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([255, 0, 0], 0.2126, 3.00)
        expected_message = 'Colors with values of 0 - 54 for each of RGB in rgb(red, green, blue) will pass the ' \
                           'WCAG 2.0 AA 18pt+ standard with color: rgb(255, 0, 0).\nAlso colors with values of 223 - ' \
                           '255 for each of RGB in rgb(red, green, blue) will pass the WCAG 2.0 AA 18pt+ standard' \
                           ' with color: rgb(255, 0, 0).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_450_contrast_lighter_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([0, 0, 0], 0.00, 4.50)
        expected_message = 'Required relative luminance for sufficient contrast of darker colors must be between 0' \
                           ' and 1 with color: rgb(0, 0, 0).\nAlso colors with values of 117 - 255 for each of RGB' \
                           ' in rgb(red, green, blue) will pass the WCAG 2.0 AA standard with color: rgb(0, 0, 0).' \
                           '\nAlso colors with values of 117 - 255 for each of RGB in rgb(red, green, blue) will ' \
                           'pass the WCAG 2.0 AAA 18pt+ standard with color: rgb(0, 0, 0).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_450_contrast_darker_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([255, 255, 255], 1.00, 4.50)
        expected_message = 'Colors with values of 0 - 118 for each of RGB in rgb(red, green, blue) will pass the ' \
                           'WCAG 2.0 AA standard with color: rgb(255, 255, 255).\nColors with values of 0 - 118 for' \
                           ' each of RGB in rgb(red, green, blue) will pass the WCAG 2.0 AAA 18pt+ standard with' \
                           ' color: rgb(255, 255, 255).\nRequired relative luminance for sufficient contrast of ' \
                           'lighter colors must be between 0 and 1 with color: rgb(255, 255, 255).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_450_contrast_lighter_and_darker(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([188, 0, 255], 0.18, 4.50)
        expected_message = 'Colors with values of 0 - 3 for each of RGB in rgb(red, green, blue) will pass the ' \
                           'WCAG 2.0 AA standard with color: rgb(188, 0, 255).\nColors with values of 0 - 3 for' \
                           ' each of RGB in rgb(red, green, blue) will pass the WCAG 2.0 AAA 18pt+ standard with' \
                           ' color: rgb(188, 0, 255).\nAlso colors with values of 254 - 255 for each of RGB in' \
                           ' rgb(red, green, blue) will pass the WCAG 2.0 AA standard with color: rgb(188, 0, 255).' \
                           '\nAlso colors with values of 254 - 255 for each of RGB in rgb(red, green, blue) will' \
                           ' pass the WCAG 2.0 AAA 18pt+ standard with color: rgb(188, 0, 255).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_700_contrast_lighter_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([0, 0, 0], 0.00, 7.00)
        expected_message = 'Required relative luminance for sufficient contrast of darker colors must be between 0' \
                           ' and 1 with color: rgb(0, 0, 0).\nAlso colors with values of 149 - 255 for each of RGB' \
                           ' in rgb(red, green, blue) will pass the WCAG 2.0 AAA standard with color: rgb(0, 0, 0).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_700_contrast_darker_only(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([255, 255, 255], 1.00, 7.00)
        expected_message = 'Colors with values of 0 - 89 for each of RGB in rgb(red, green, blue) will pass the ' \
                           'WCAG 2.0 AAA standard with color: rgb(255, 255, 255).\nRequired relative luminance' \
                           ' for sufficient contrast of lighter colors must be between 0 and 1 with color: ' \
                           'rgb(255, 255, 255).'
        self.assertEqual(result, expected_message)

    def test_color_recommendations_for_700_contrast_none(self):
        result = self.recommendations.calculate_colors_that_pass_given_contrast_ratio([255, 0, 0], 0.2126, 7.00)
        expected_message = 'Required relative luminance for sufficient contrast of darker colors must be between 0' \
                           ' and 1 with color: rgb(255, 0, 0).\nRequired relative luminance for sufficient contrast ' \
                           'of lighter colors must be between 0 and 1 with color: rgb(255, 0, 0).'
        self.assertEqual(result, expected_message)
