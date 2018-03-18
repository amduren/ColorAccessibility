from math import floor, ceil


class ColorRecommendations:

    @staticmethod
    def calculate_colors_that_pass_given_contrast_ratio(rgb_list, relative_luminance, contrast_ratio):
        message = ''

        if contrast_ratio == 3.00:
            standard = ['AA 18pt+']
        elif contrast_ratio == 7.00:
            standard = ['AAA']
        else:
            standard = ['AA', 'AAA 18pt+']

        # Calculate required luminance for a "darker" color of sufficient contrast
        # contrast_ratio <= (relative_luminance + 0.05) / (req_darker_luminance + 0.05)
        # req_darker_luminance <= ((relative_luminance + 0.05) / contrast_ratio) - 0.05
        req_darker_luminance = ((relative_luminance + 0.05) / contrast_ratio) - 0.05

        # 0 <= temp_darker_luminance <= req_darker_luminance
        if 0 <= req_darker_luminance <= 1:
            temp_darker_luminance = req_darker_luminance

            # for 0 <= darker_gray_color <= 10.164:
            #    0.0003035269835 * darker_gray_color <= req_darker_luminance
            #    darker_gray_color <= req_darker_luminance / 0.0003035269835
            darker_gray_color = temp_darker_luminance / 0.0003035269835

            if darker_gray_color > 10.164:
                # for 10.164 <= darker_gray_color <= 255:
                #    (((darker_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= req_darker_luminance
                #    darker_gray_color <= (((req_darker_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                darker_gray_color = (((req_darker_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255

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
        # contrast_ratio <= (req_lighter_luminance + 0.05) / (relative_luminance + 0.05)
        # req_lighter_luminance >= (contrast_ratio * (relative_luminance + 0.05)) - 0.05
        req_lighter_luminance = (contrast_ratio * (relative_luminance + 0.05)) - 0.05

        # req_lighter_luminance <= temp_lighter_luminance <= 1
        if 0 <= req_lighter_luminance <= 1:
            temp_lighter_luminance = req_lighter_luminance

            # for 0 <= lighter_gray_color <= 10.164:
            #     0.0003035269835 * lighter_gray_color >= req_lighter_luminance
            #     lighter_gray_color >= req_lighter_luminance / 0.0003035269835
            lighter_gray_color = temp_lighter_luminance / 0.0003035269835

            if lighter_gray_color > 10.164:
                # for 10.164 <= lighter_gray_color <= 255:
                #     (((lighter_gray_color / 255) + 0.055) / 1.055) ** 2.4 <= req_lighter_luminance
                #     lighter_gray_color >= (((req_lighter_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255
                lighter_gray_color = (((req_lighter_luminance ** (1 / 2.4)) * 1.055) - 0.055) * 255

                if lighter_gray_color > 255:
                    lighter_gray_color = None

            message += 'Also colors with values of {} - 255 for each of RGB in rgb(red, green, blue) will' \
                .format(ceil(lighter_gray_color))
            message += ' pass the WCAG 2.0 {} standard with color: rgb({}, {}, {}).'.format(standard[0], rgb_list[0],
                                                                                            rgb_list[1], rgb_list[2])
            if contrast_ratio == 4.50:
                message += '\nAlso colors with values of {} - 255 for each of RGB in rgb(red, green, blue) will ' \
                    .format(ceil(lighter_gray_color))
                message += 'pass the WCAG 2.0 {} standard with color: rgb({}, {}, {}).'.format(standard[1], rgb_list[0],
                                                                                               rgb_list[1], rgb_list[2])
        else:
            message += 'Required relative luminance for sufficient contrast of lighter colors must be between 0 and 1 '
            message += 'with color: rgb({}, {}, {}).'.format(rgb_list[0], rgb_list[1], rgb_list[2])

        return message
