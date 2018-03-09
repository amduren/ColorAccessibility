from app.color_accessibility_calculations import ColorCalculations
from app.utilities.prompts import ask_for_color

color = ColorCalculations()

rgb_1 = ask_for_color(1)
rgb_2 = ask_for_color(2)

print(rgb_1)
print(rgb_2)
print()
print(color.calculate_color_difference(rgb_1, rgb_2))
print(color.calculate_color_brightness_difference(rgb_1, rgb_2))
print()
