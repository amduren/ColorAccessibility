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
