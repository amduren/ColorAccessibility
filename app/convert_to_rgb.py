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
        elif luminance >= 0.50:
            constant_1 = luminance + saturation - luminance * saturation

        constant_2 = 2 * luminance - constant_1
        hue_of_360 = hue / 360
        red = hue_of_360 + 0.333
        green = hue_of_360
        blue = hue_of_360 - 0.333
        rgb = [red, blue, green]

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
