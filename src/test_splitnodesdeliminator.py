import unittest

from splitnodesdeliminator import *
from textnode import *

class TestTextNodeConversion(unittest.TestCase):
    def test_onedeliminatorcode(self):
        node = TextNode("This is text with a `code block` word", "PLAIN")
        new_nodes = split_nodes_delimiter([node], "`", "CODE")
        expected = [TextNode("This is text with a ", "PLAIN"), TextNode("code block", "CODE"), TextNode(" word", "PLAIN")]
        self.assertEqual(new_nodes, expected)
    
    def test_onedeliminatoritalic(self):
        node = TextNode("This is text with a _italic_ word", "PLAIN")
        new_nodes = split_nodes_delimiter([node], "_", "ITALIC")
        expected = [TextNode("This is text with a ", "PLAIN"), TextNode("italic", "ITALIC"), TextNode(" word", "PLAIN")]
        self.assertEqual(new_nodes, expected)
    
    def test_onedeliminatorbold(self):
        node = TextNode("This is text with a **bold** word", "PLAIN")
        new_nodes = split_nodes_delimiter([node], "**", "BOLD")
        expected = [TextNode("This is text with a ", "PLAIN"), TextNode("bold", "BOLD"), TextNode(" word", "PLAIN")]
        self.assertEqual(new_nodes, expected)
    

if __name__ == "__main__":
    unittest.main()