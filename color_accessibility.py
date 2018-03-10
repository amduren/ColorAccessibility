from app.color_accessibility_calculations import ColorCalculations
from app.convert_to_hex import ConvertToHex
from app.convert_to_hsl import ConvertToHsl
from app.utilities.prompts import ask_for_color

color = ColorCalculations()
hex_color = ConvertToHex()
hsl_color = ConvertToHsl()

rgb_1 = ask_for_color(1)
rgb_2 = ask_for_color(2)

hex_1 = hex_color.convert_rgb_to_hex(rgb_1)
hex_2 = hex_color.convert_rgb_to_hex(rgb_2)

hsl_1 = hsl_color.convert_rgb_to_hsl(rgb_1)
hsl_2 = hsl_color.convert_rgb_to_hsl(rgb_2)

print('First color as RGB: rgb({}, {}, {})'.format(rgb_1[0], rgb_1[1], rgb_1[2]))
print('First color as Hex: {}'.format(hex_1))
print('First color as HSL: hsl({}, {}, {})'.format(hsl_1[0], hsl_1[1], hsl_1[2]))
print()
print('Second color as RGB: rgb({}, {}, {})'.format(rgb_2[0], rgb_2[1], rgb_2[2]))
print('Second color as Hex: {}'.format(hex_2))
print('Second color as HSL: hsl({}, {}, {})'.format(hsl_2[0], hsl_2[1], hsl_2[2]))
print()
print(color.calculate_color_difference(rgb_1, rgb_2))
print(color.calculate_color_brightness_difference(rgb_1, rgb_2))
print()
