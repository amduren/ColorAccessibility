from app.convert_to_rgb import ConvertToRgb


def ask_for_color(number):
    rgb = []
    color = ConvertToRgb()

    if number == 1:
        number_string = 'first'
    elif number == 2:
        number_string = 'second'
    else:
        return 'Can only compare two colors at a time. Please enter 1 or 2'

    color_format = input('What format would you like to enter your {} color in as (RGB, Hex, HSL)? '
                         .format(number_string))
    if color_format.lower() == 'rgb':
        rgb.append(int(input('\tWhat is the color\'s R value (0 - 255)? ')))
        rgb.append(int(input('\tWhat is the color\'s G value (0 - 255)? ')))
        rgb.append(int(input('\tWhat is the color\'s B value (0 - 255)? ')))
    elif color_format.lower() == 'hex' or color_format.lower() == 'hexidecimal':
        rgb = color.convert_hex_to_rgb(input('\tWhat is the color\'s hex value? '))
    elif color_format.lower() == 'hsl':
        hue = float(input('\tWhat is the color\'s hue value (0 - 360)? '))
        saturation = float(input('\tWhat is the color\'s saturation value (0 - 1)? '))
        luminance = float(input('\tWhat is the color\'s luminance value (0 - 1)? '))
        rgb = color.convert_hsl_to_rgb(hue, saturation, luminance)

    print()

    return rgb
