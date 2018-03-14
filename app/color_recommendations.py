from math import floor, ceil


class ColorRecommendations:

    @staticmethod
    def calculate_colors_that_pass_given_contrast_ratio(rgb_list, relative_luminance, contrast_ratio):
        message = ''

        if contrast_ratio == 3.00:
            standard = ['AA 18pt+']
        elif contrast_ratio == 7.00:
            standard = ['AAA 18pt+']
        else:
            standard = ['AA', 'AAA']

        # Calculate required luminance for a "darker" color of sufficient contrast
        #   contrast_ratio <= (relative_luminance + 0.05) / (req_darker_luminance + 0.05)
        #   req_darker_luminance + 0.05 <= (relative_luminance + 0.05) / contrast_ratio
        #   req_darker_luminance <= ((relative_luminance + 0.05) / contrast_ratio) - 0.05
        req_darker_luminance = ((relative_luminance + 0.05) / contrast_ratio) - 0.05
        # Example using rgb(255, 0, 0)
        # 7.00 <= (0.2126 + 0.05) / (y + 0.05)
        # y + 0.05 <= 0.2626 / 7.00
        # y + 0.05 <= 0.03751428571
        # y <= -0.01248571429
        #
        # 4.50 <= (0.2126 + 0.05) / (y + 0.05)
        # y + 0.05 <= 0.2626 / 4.50
        # y + 0.05 <= 0.05835556
        # y <= 0.00835556
        #
        # 3.00 <= (0.2126 + 0.05) / (y + 0.05)
        # y + 0.05 <= 0.2626 / 3.00
        # y + 0.05 <= 0.08753333
        # y <= 0.03753333

        # 0 <= temp_darker_luminance <= req_darker_luminance
        if 0 <= req_darker_luminance <= 1:
            temp_darker_luminance = req_darker_luminance
            # Example using rgb(255, 0, 0)
            # 7.00 : y <= -0.01248571429 FAILS
            #
            # 4.50 : y <= 0.00835556
            # 0 <= y <= 0.00835556
            #
            # 3.00 : y <= 0.03753333
            # 0 <= y <= 0.03753333

            # for 0 <= darker_gray_color <= 10.164:
            #    0.0003035269835 * darker_gray_color <= req_darker_luminance
            #    darker_gray_color <= req_darker_luminance / 0.0003035269835
            darker_gray_color = temp_darker_luminance / 0.0003035269835
            # Example using rgb(255, 0, 0)
            # 7.00 : y <= -0.01248571429 FAILS
            #
            # 4.50 : 0.0003035269835 * darker_gray_color <= 0.00835556
            # darker_gray_color <= 0.00835556 / 0.0003035269835
            # darker_gray_color <= 27.528 >> 10.164 because 10.164 < 27.528
            #
            # 3.00 : 0.0003035269835 * darker_gray_color <= 0.03753333
            # darker_gray_color <= 0.03753333 / 0.0003035269835
            # darker_gray_color <= 123.657 >> 10.164 because 10.164 < 123.657

            if darker_gray_color > 10.164:
                # darker_gray_color = 10.164

                # for 10.164 <= darker_gray_color <= 255:
                #    (((darker_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= req_darker_luminance
                #    ((darker_gray_color / 255) + 0.055) / 1.055 <= req_darker_luminance ** (1 / 2.4)
                #    (darker_gray_color / 255) + 0.055 <= (req_darker_luminance ** (1 / 2.4)) * 1.055
                #    darker_gray_color / 255 <= ((req_darker_luminance ** (1 / 2.4)) * 1.055) - 0.055
                #    darker_gray_color <= (((req_darker_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                darker_gray_color = (((req_darker_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                # Example using rgb(255, 0, 0)
                # 7.00 : y <= -0.01248571429 FAILS
                #
                # 4.50 : (((darker_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= 0.00835556
                # ((darker_gray_color / 255) + 0.055) / 1.055 <= 0.00835556 ** (1 / 2.4)
                # (darker_gray_color / 255) + 0.055 <= (0.00835556 ** (1 / 2.4)) * 1.055
                # darker_gray_color / 255 <= ((0.00835556 ** (1 / 2.4)) * 1.055) - 0.055
                # darker_gray_color <= (((0.00835556 ** (1 / 2.4)) * 1.055) - 0.055) * 255
                # darker_gray_color <= 22.614
                #
                # 3.00 : (((darker_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= 0.03753333
                # ((darker_gray_color / 255) + 0.055) / 1.055 <= 0.03753333 ** (1 / 2.4)
                # (darker_gray_color / 255) + 0.055 <= (0.03753333 ** (1 / 2.4)) * 1.055
                # darker_gray_color / 255 <= ((0.03753333 ** (1 / 2.4)) * 1.055) - 0.055
                # darker_gray_color <= (((0.03753333 ** (1 / 2.4)) * 1.055) - 0.055) * 255
                # darker_gray_color <= 54.492
                if darker_gray_color > 255:
                    darker_gray_color = 255

            message += 'Colors with values of 0 - {} for each of RGB in rgb(red, green, blue) will pass'.\
                format(floor(darker_gray_color))
            message += ' the WCAG 2.0 {} standard with color: rgb({}, {}, {}).\n'.format(standard[0], rgb_list[0],
                                                                                         rgb_list[1], rgb_list[2])
            if contrast_ratio == 4.50:
                message += 'Colors with values of 0 - {} for each of RGB in rgb(red, green, blue) will pass'. \
                    format(floor(darker_gray_color))
                message += ' the WCAG 2.0 {} standard with color: rgb({}, {}, {}).\n'.format(standard[1], rgb_list[0],
                                                                                             rgb_list[1], rgb_list[2])
        else:
            message += 'Required relative luminance for sufficient contrast of darker colors must be between 0 and 1 '
            message += 'with color: rgb({}, {}, {}).\n'.format(rgb_list[0], rgb_list[1], rgb_list[2])

        # Calculate required luminance for a "lighter" color of sufficient contrast
        #   contrast_ratio <= (req_lighter_luminance + 0.05) / (relative_luminance + 0.05)
        #   contrast_ratio * (relative_luminance + 0.05) <= req_lighter_luminance + 0.05
        #   req_lighter_luminance >= (contrast_ratio * (relative_luminance + 0.05)) - 0.05
        req_lighter_luminance = (contrast_ratio * (relative_luminance + 0.05)) - 0.05
        # Example using rgb(255, 0, 0)
        # 7.00 <= (y + 0.05) / (0.2126 + 0.05)
        # 7.00 * 0.2626 <= y + 0.05
        # y >= 7.00 * 0.2626 - 0.05
        # y >= 1.7882
        #
        # 4.50 <= (y + 0.05) / (0.2126 + 0.05)
        # 4.50 * 0.2626 <= y + 0.05
        # y >= 4.50 * 0.2626 - 0.05
        # y >= 1.1317
        #
        # 3.00 <= (y + 0.05) / (0.2126 + 0.05)
        # 3.00 * 0.2626 <= y + 0.05
        # y >= 3.00 * 0.2626 - 0.05
        # y >= 0.7378

        # req_lighter_luminance <= temp_lighter_luminance <= 1
        if 0 <= req_lighter_luminance <= 1:
            temp_lighter_luminance = req_lighter_luminance
            # Example using rgb(255, 0, 0)
            # 7.00 : y >= 1.7882 FAILS
            #
            # 4.50 : y >= 1.1317 FAILS
            #
            # 3.00 : y >= 0.7378
            # 0.7378 <= y <= 1

            # for 0 <= lighter_gray_color <= 10.164:
            #     0.0003035269835 * lighter_gray_color >= req_lighter_luminance
            #     lighter_gray_color >= req_lighter_luminance / 0.0003035269835
            lighter_gray_color = temp_lighter_luminance / 0.0003035269835
            # Example using rgb(255, 0, 0)
            # 7.00 : y >= 1.7882 FAILS
            #
            # 4.50 : y >= 1.1317 FAILS
            #
            # 3.00 : 0.0003035269835 * lighter_gray_color >= 0.7378
            # lighter_gray_color >= 0.7378 / 0.0003035269835
            # lighter_gray_color >= 2430.759 >> None because 10.164 < 2430.759

            if lighter_gray_color > 10.164:
                # lighter_gray_color = None

                # for 10.164 <= lighter_gray_color <= 255:
                #     (((lighter_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= req_lighter_luminance
                #     ((lighter_gray_color / 255) + 0.055) / 1.055 >= req_lighter_luminance ** (1 / 2.4)
                #     (lighter_gray_color / 255) + 0.055 >= (req_lighter_luminance ** (1 / 2.4)) * 1.055
                #     lighter_gray_color / 255 >= ((req_lighter_luminance ** (1 / 2.4)) * 1.055) - 0.055
                #     lighter_gray_color >= (((req_lighter_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                lighter_gray_color = (((req_lighter_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                # Example using rgb(255, 0, 0)
                # 7.00 : y >= 1.7882 FAILS
                #
                # 4.50 : y >= 1.1317 FAILS
                #
                # 3.00 : (((lighter_gray_color / 255) + 0.055) / 1.055) ** 2.4 >= 0.7378
                # ((lighter_gray_color / 255) + 0.055) / 1.055 >= 0.7378 ** (1 / 2.4)
                # (lighter_gray_color / 255) + 0.055 >= (0.7378 ** (1 / 2.4)) * 1.055
                # lighter_gray_color / 255 >= ((0.7378 ** (1 / 2.4)) * 1.055) - 0.055
                # lighter_gray_color >= (((0.7378 ** (1 / 2.4)) * 1.055) - 0.055) * 255
                # lighter_gray_color >= 222.985
                if lighter_gray_color > 255:
                    lighter_gray_color = None

            message += 'Also colors with values of {} - 255 for each of RGB in rgb(red, green, blue) will' \
                .format(ceil(lighter_gray_color))
            message += 'pass the WCAG 2.0 {} standard with color: rgb({}, {}, {}).'.format(standard[0], rgb_list[0],
                                                                                           rgb_list[1], rgb_list[2])
            if contrast_ratio == 4.50:
                message += '\nAlso colors with values of {} - 255 for each of RGB in rgb(red, green, blue) will' \
                    .format(ceil(lighter_gray_color))
                message += 'pass the WCAG 2.0 {} standard with color: rgb({}, {}, {}).'.format(standard[1], rgb_list[0],
                                                                                               rgb_list[1], rgb_list[2])
        else:
            message += 'Required relative luminance for sufficient contrast of lighter colors must be between 0 and 1 '
            message += 'with color: rgb({}, {}, {}).'.format(rgb_list[0], rgb_list[1], rgb_list[2])

        return message
