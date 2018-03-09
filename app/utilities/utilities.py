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
