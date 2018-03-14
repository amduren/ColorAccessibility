class ColorCalculations:

    def calculate_color_difference(self, rgb_list_1, rgb_list_2):
        red_difference = max(rgb_list_1[0], rgb_list_2[0]) - min(rgb_list_1[0], rgb_list_2[0])
        green_difference = max(rgb_list_1[1], rgb_list_2[1]) - min(rgb_list_1[1], rgb_list_2[1])
        blue_difference = max(rgb_list_1[2], rgb_list_2[2]) - min(rgb_list_1[2], rgb_list_2[2])

        color_difference = red_difference + green_difference + blue_difference
        difference_message = 'Color difference is {}. '.format(color_difference)

        if color_difference >= 500:
            message = difference_message + 'Color difference PASSES the standard.'
        else:
            message = difference_message + 'Color difference MUST BE AT LEAST 500 to pass the standard.'

        return message

    def calculate_color_brightness_difference(self, rgb_list_1, rgb_list_2):
        red_1 = rgb_list_1[0] * 299
        green_1 = rgb_list_1[1] * 587
        blue_1 = rgb_list_1[2] * 114
        brightness_1 = (red_1 + green_1 + blue_1) / 1000

        red_2 = rgb_list_2[0] * 299
        green_2 = rgb_list_2[1] * 587
        blue_2 = rgb_list_2[2] * 114
        brightness_2 = (red_2 + green_2 + blue_2) / 1000

        brightness = round(max(brightness_1, brightness_2) - min(brightness_1, brightness_2), 2)
        difference_message = 'Color brightness difference is {}. '.format(brightness)

        if brightness >= 125:
            message = difference_message + 'Color brightness PASSES the standard.'
        else:
            message = difference_message + 'Color brightness difference MUST BE AT LEAST 125 to pass the standard.'

        return message

    def calculate_relative_luminance(self, rgb_list):
        luminance_list = []
        for color in range(len(rgb_list)):
            luminance_list.append(rgb_list[color] / 255)

            if luminance_list[color] <= 0.03928:
                luminance_list[color] /= 12.92
            else:
                luminance_list[color] = ((luminance_list[color] + 0.055) / 1.055) ** 2.4

        relative_luminance = 0.2126 * luminance_list[0] + 0.7152 * luminance_list[1] + 0.0722 * luminance_list[2]

        return relative_luminance

    def calculate_contrast_ratio(self, rel_luminance_1, rel_luminance_2):
        lighter = max(rel_luminance_1, rel_luminance_2)
        darker = min(rel_luminance_1, rel_luminance_2)

        contrast = round((lighter + 0.05) / (darker + 0.05), 2)

        return contrast
