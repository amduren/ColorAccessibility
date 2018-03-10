from app.utilities import utilities


class ConvertToHex(object):

    def convert_rgb_to_hex(self, rgb_list):
        list_of_ints = range(10, 16)
        string_of_characters = 'ABCDEF'

        hex_value = '#'

        for color in range(len(rgb_list)):
            first_value = int(rgb_list[color] / 16)
            second_value = rgb_list[color] % 16

            first_value = utilities.map_int_to_char(first_value, list_of_ints, string_of_characters)
            second_value = utilities.map_int_to_char(second_value, list_of_ints, string_of_characters)

            hex_value += str(first_value) + str(second_value)

        return hex_value
