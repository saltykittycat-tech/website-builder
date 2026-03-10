import unittest
from extract_title import *

class TestTextNodeConversion(unittest.TestCase):
    def test_1(self):
        markdown = "# hello"
        expected = "hello"
        result = extract_title(markdown)
        self.assertEqual(expected, result)

    def test_2(self):
        markdown = '''# this is a title

        this is a paragraph'''
        expected = "this is a title"
        result = extract_title(markdown)
        self.assertEqual(expected, result)

    def test_3(self):
        markdown = "## this is not a title"
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_4(self):
        markdown = '''This is a paragraph not a title

        # this is also not a title'''
        with self.assertRaises(Exception):
            extract_title(markdown)


    








if __name__ == "__main__":
    unittest.main()