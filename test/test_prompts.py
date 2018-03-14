import unittest

from app.utilities.prompts import ask_for_color


class PromptsTests(unittest.TestCase):

    def test_asking_for_3_colors_returns_message(self):
        result = ask_for_color(3)
        self.assertEqual(result, 'Can only compare two colors at a time. Please enter 1 or 2.')
