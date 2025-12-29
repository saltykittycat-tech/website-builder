import unittest
from blocktype import *

class TestTextNodeConversion(unittest.TestCase):
    def test_heading1(self):
        block = "# This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading2(self):
        block = "## This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading3(self):
        block = "### This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading4(self):
        block = "#### This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading5(self):
        block = "##### This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_heading6(self):
        block = "###### This is a heading"
        expected = "HEAD"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_notaheading(self):
        block = "####### This is not a heading"
        not_expected = "HEAD"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)
    
    def test_code(self):
        block = "```this is a block of code```"
        expected = "CODE"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_notcode1(self):
        block = "````this is not a block of code````"
        not_expected = "CODE"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)
    
    def test_notcode2(self):
        block = "```this is not a block of code"
        not_expected = "CODE"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)
    
    def test_notcode3(self):
        block = "``this is not a block of code``"
        not_expected = "CODE"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)

    def test_quote(self):
        block = "> this is a quote"
        expected = "QUOTE"
        result = block_to_block_type(block)
        self.assertEqual(result, expected)

    def test_unorderedlist(self):
        block = "- This is a list\n- with items"
        expected = "UNORDERED_LIST"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_notunorderedlist(self):
        block = "- This is not a list\n with items"
        not_expected = "UNORDERED_LIST"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)
    
    def test_orderedlist(self):
        block = "1. this is\n2. a\n3. ordered list"
        expected = "ORDERED_LIST"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)
    
    def test_notorderedlist(self):
        block = "1. this is\n4. not\n2. a\n3. ordered list"
        not_expected = "ORDERED_LIST"
        result = block_to_block_type(block)
        self.assertNotEqual(not_expected, result)

    def test_paragraph(self):
        block = """this is a paragraph"""
        expected = "PARAGRAPH"
        result = block_to_block_type(block)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()