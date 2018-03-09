class ColorCalculations(object):

    def calculate_color_difference(self, rgb_list_1, rgb_list_2):
        red_difference = max(rgb_list_1[0], rgb_list_2[0]) - min(rgb_list_1[0], rgb_list_2[0])
        green_difference = max(rgb_list_1[1], rgb_list_2[1]) - min(rgb_list_1[1], rgb_list_2[1])
        blue_difference = max(rgb_list_1[2], rgb_list_2[2]) - min(rgb_list_1[2], rgb_list_2[2])

        color_difference = red_difference + green_difference + blue_difference
        difference_message = 'Color difference is {}. '.format(color_difference)

        if color_difference >= 500:
            message = difference_message + 'Color difference is sufficient.'
        else:
            message = difference_message + 'Color difference must be at least 500 to pass.'

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
            message = difference_message + 'Color brightness is sufficient.'
        else:
            message = difference_message + 'Color brightness difference must be at least 125 to pass.'

        return message
