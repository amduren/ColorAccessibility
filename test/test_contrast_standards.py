import unittest

from app.contrast_standards import ContrastStandards


class ContrastStandardsTests(unittest.TestCase):
    def setUp(self):
        self.contrast = ContrastStandards()

    def test_wcag_aa_compliant_passes(self):
        result = self.contrast.is_wcag_aa_compliant(5.00)
        self.assertEqual(result, 'Contrast PASSES the WCAG 2.0 AA standard.')

    def test_wcag_aa_compliant_fails(self):
        result = self.contrast.is_wcag_aa_compliant(1.50)
        self.assertEqual(result, 'Contrast FAILS the WCAG 2.0 AA standard; must be at least 4.50.')

    def test_wcag_aa_at_least_18_compliant_passes(self):
        result = self.contrast.is_wcag_aa_at_least_18_compliant(3.00)
        self.assertEqual(result, 'Contrast PASSES the WCAG 2.0 AA 18pt+ standard.')

    def test_wcag_aa_at_least_18_compliant_fails(self):
        result = self.contrast.is_wcag_aa_at_least_18_compliant(2.99)
        self.assertEqual(result, 'Contrast FAILS the WCAG 2.0 AA 18pt+ standard; must be at least 3.00.')

    def test_wcag_aaa_compliant_passes(self):
        result = self.contrast.is_wcag_aaa_compliant(7.01)
        self.assertEqual(result, 'Contrast PASSES the WCAG 2.0 AAA standard.')

    def test_wcag_aaa_compliant_fails(self):
        result = self.contrast.is_wcag_aaa_compliant(0.15)
        self.assertEqual(result, 'Contrast FAILS the WCAG 2.0 AAA standard; must be at least 7.00.')

    def test_wcag_aaa_at_least_18_compliant_passes(self):
        result = self.contrast.is_wcag_aaa_at_least_18_compliant(4.67)
        self.assertEqual(result, 'Contrast PASSES the WCAG 2.0 AAA 18pt+ standard.')

    def test_wcag_aaa_at_least_18_compliant_fails(self):
        result = self.contrast.is_wcag_aaa_at_least_18_compliant(4.49987)
        self.assertEqual(result, 'Contrast FAILS the WCAG 2.0 AAA 18pt+ standard; must be at least 4.50.')
