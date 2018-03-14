class ConvertToHsl:

    def convert_rgb_to_hsl(self, rgb_list):
        hsl = []

        for color in range(len(rgb_list)):
            hsl.append(rgb_list[color] / 255)

        max_val = 0.0
        min_val = 1.0

        for color in range(len(hsl)):
            if hsl[color] > max_val:
                max_val = hsl[color]
            if hsl[color] < min_val:
                min_val = hsl[color]

        luminance = round((max_val + min_val) / 2, 3)

        if min_val == max_val:
            saturation = 0.0
        elif luminance < 0.50:
            saturation = round((max_val - min_val) / (max_val + min_val), 3)
        else:
            saturation = round((max_val - min_val) / (2.0 - max_val - min_val), 3)

        if rgb_list[0] == rgb_list[1] and rgb_list[1] == rgb_list[2]:
            hue = 0
        elif max(hsl) == hsl[0]:
            hue = round(((hsl[1] - hsl[2]) / (max_val - min_val)) * 60)
        elif max(hsl) == hsl[1]:
            hue = round((2.0 + (hsl[2] - hsl[0]) / (max_val - min_val)) * 60)
        elif max(hsl) == hsl[2]:
            hue = round((4.0 + (hsl[0] - hsl[1]) / (max_val - min_val)) * 60)

        hsl = [hue, round(saturation, 2), round(luminance, 2)]

        return hsl
