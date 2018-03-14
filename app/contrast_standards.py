class ContrastStandards(object):

    def is_wcag_aa_compliant(self, contrast):
        if contrast >= 4.50:
            return 'Contrast passes the WCAG 2.0 AA standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AA standard; must be at least 4.50.'

    def is_wcag_aa_at_least_18_compliant(self, contrast):
        if contrast >= 3.00:
            return 'Contrast passes the WCAG 2.0 AA 18pt+ standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AA 18pt+ standard; must be at least 3.00.'

    def is_wcag_aaa_compliant(self, contrast):
        if contrast >= 7.00:
            return 'Contrast passes the WCAG 2.0 AAA standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AAA standard; must be at least 7.00.'

    def is_wcag_aaa_at_least_18_compliant(self, contrast):
        if contrast >= 4.50:
            return 'Contrast passes the WCAG 2.0 AAA 18pt+ standard.'
        else:
            return 'Contrast FAILS the WCAG 2.0 AAA 18pt+ standard; must be at least 4.50.'
