def map_char_to_int(char, string_of_chars, list_of_ints):
    if len(string_of_chars) < len(list_of_ints):
        return 'Not enough characters to map to an integer.'
    if len(string_of_chars) > len(list_of_ints):
        return 'Too many characters to map to an integer.'

    if char not in string_of_chars:
        return 'Character not in string of characters.'

    for letter in range(len(string_of_chars)):
        if char.lower() == string_of_chars[letter]:
            int_from_char = list_of_ints[letter]

    return int_from_char


def map_int_to_char(integer, list_of_ints, string_of_chars):
    if len(list_of_ints) < len(string_of_chars):
        return 'Not enough integers to map to a character.'
    if len(list_of_ints) > len(string_of_chars):
        return 'Too many integers to map to a character.'

    if integer not in list_of_ints:
        return integer

    for number in range(len(list_of_ints)):
        if integer == list_of_ints[number]:
            char_from_int = string_of_chars[number]

    return char_from_int
