from app.color_accessibility_calculations import ColorCalculations
from app.contrast_standards import ContrastStandards
from app.convert_to_hex import ConvertToHex
from app.convert_to_hsl import ConvertToHsl
from app.utilities.prompts import ask_for_color

from app.color_recommendations import ColorRecommendations

color = ColorCalculations()
hex_color = ConvertToHex()
hsl_color = ConvertToHsl()
contrast_obj = ContrastStandards()

rgb_1 = ask_for_color(1)
rgb_2 = ask_for_color(2)

hex_1 = hex_color.convert_rgb_to_hex(rgb_1)
hex_2 = hex_color.convert_rgb_to_hex(rgb_2)

hsl_1 = hsl_color.convert_rgb_to_hsl(rgb_1)
hsl_2 = hsl_color.convert_rgb_to_hsl(rgb_2)

relative_luminance_1 = color.calculate_relative_luminance(rgb_1)
relative_luminance_2 = color.calculate_relative_luminance(rgb_2)

contrast = color.calculate_contrast_ratio(relative_luminance_1, relative_luminance_2)

print('First color as…\n\tRGB: rgb({}, {}, {})\n\tHex: {}\n\tHSL: hsl({}, {}, {})\n'.format(rgb_1[0], rgb_1[1],
                                                                                            rgb_1[2], hex_1, hsl_1[0],
                                                                                            hsl_1[1], hsl_1[2]))
print('Second color as…\n\tRGB: rgb({}, {}, {})\n\tHex: {}\n\tHSL: hsl({}, {}, {})\n'.format(rgb_2[0], rgb_2[1],
                                                                                             rgb_2[2], hex_2, hsl_2[0],
                                                                                             hsl_2[1], hsl_2[2]))
print(color.calculate_color_difference(rgb_1, rgb_2))
print(color.calculate_color_brightness_difference(rgb_1, rgb_2))
print('\nThe contrast between the two colors is {}.'.format(contrast))
print(contrast_obj.is_wcag_aa_at_least_18_compliant(contrast))
print(contrast_obj.is_wcag_aa_compliant(contrast))
print(contrast_obj.is_wcag_aaa_at_least_18_compliant(contrast))
print(contrast_obj.is_wcag_aaa_compliant(contrast) + '\n')

color_recs = ColorRecommendations()
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_1, relative_luminance_1, 3.00))
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_2, relative_luminance_2, 3.00) + '\n')
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_1, relative_luminance_1, 4.50))
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_2, relative_luminance_2, 4.50) + '\n')
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_1, relative_luminance_1, 7.00))
print(color_recs.calculate_colors_that_pass_given_contrast_ratio(rgb_2, relative_luminance_2, 7.00))
