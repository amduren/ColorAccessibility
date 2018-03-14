class ContrastStandards:

    @staticmethod
    def is_wcag_aa_compliant(contrast):
        if contrast >= 4.50:
            return 'Contrast PASSES the WCAG 2.0 AA standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AA standard; must be at least 4.50.'

    @staticmethod
    def is_wcag_aa_at_least_18_compliant(contrast):
        if contrast >= 3.00:
            return 'Contrast PASSES the WCAG 2.0 AA 18pt+ standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AA 18pt+ standard; must be at least 3.00.'

    @staticmethod
    def is_wcag_aaa_compliant(contrast):
        if contrast >= 7.00:
            return 'Contrast PASSES the WCAG 2.0 AAA standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AAA standard; must be at least 7.00.'

    @staticmethod
    def is_wcag_aaa_at_least_18_compliant(contrast):
        if contrast >= 4.50:
            return 'Contrast PASSES the WCAG 2.0 AAA 18pt+ standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AAA 18pt+ standard; must be at least 4.50.'
