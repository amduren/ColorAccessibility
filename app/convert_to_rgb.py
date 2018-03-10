from app.utilities import utilities


class ConvertToRgb(object):

    def convert_hsl_to_rgb(self, hue, saturation, luminance):
        if hue < 0 or hue > 360:
            return 'Hue must be between 0 and 360.'
        if saturation < 0 or saturation > 1:
            return 'Saturation must be between 0 and 1.'
        if luminance < 0 or luminance > 1:
            return 'Luminance must be between 0 and 1.'

        if saturation == 0:
            rgb_luminance = luminance * 255
            rgb = [rgb_luminance, rgb_luminance, rgb_luminance]
            return rgb

        if luminance < 0.50:
            constant_1 = luminance * (1.0 + saturation)
            # 0.4375
        elif luminance >= 0.50:
            constant_1 = luminance + saturation - luminance * saturation

        constant_2 = 2 * luminance - constant_1
        hue_of_360 = hue / 360
        red = hue_of_360 + 0.333
        green = hue_of_360
        blue = hue_of_360 - 0.333
        rgb = [red, green, blue]

        for color in range(len(rgb)):
            # Get color value to be between 0 and 1
            if rgb[color] < 0:
                rgb[color] += 1
            elif rgb[color] > 1:
                rgb[color] -= 1
            # Convert color to value to multiply by 255
            if 6 * rgb[color] < 1:
                rgb[color] = constant_2 + (constant_1 - constant_2) * 6 * rgb[color]
            elif 2 * rgb[color] < 1:
                rgb[color] = constant_1
            elif 3 * rgb[color] < 2:
                rgb[color] = constant_2 + (constant_1 - constant_2) * (0.666 - rgb[color]) * 6
            else:
                rgb[color] = constant_2
            # Set color to integer value of 0 - 255
            rgb[color] *= 255
            rgb[color] = round(rgb[color])

        return rgb

    def convert_hex_to_rgb(self, hex_string):
        letters = 'abcdef'
        numbers = range(10, 16)

        if hex_string[0] == '#':
            hex_string = hex_string[1:]

        red = hex_string[0:2]
        green = hex_string[2:4]
        blue = hex_string[4:6]
        rgb = [red, green, blue]

        for color in range(len(rgb)):
            if rgb[color][0].lower() not in letters and rgb[color][1].lower() not in letters:
                first = int(rgb[color][0])
                second = int(rgb[color][1])
                rgb[color] = first * 16 + second
            elif rgb[color][0].lower() in letters and rgb[color][1].lower() in letters:
                first = utilities.map_char_to_int(rgb[color][0].lower(), letters, numbers)
                second = utilities.map_char_to_int(rgb[color][1].lower(), letters, numbers)
                rgb[color] = first * 16 + second
            elif rgb[color][0].lower() in letters and rgb[color][1].lower() not in letters:
                first = utilities.map_char_to_int(rgb[color][0].lower(), letters, numbers)
                second = int(rgb[color][1])
                rgb[color] = first * 16 + second
            elif rgb[color][0].lower() not in letters and rgb[color][1].lower() in letters:
                first = int(rgb[color][0])
                second = utilities.map_char_to_int(rgb[color][1].lower(), letters, numbers)
                rgb[color] = first * 16 + second

        return rgb
