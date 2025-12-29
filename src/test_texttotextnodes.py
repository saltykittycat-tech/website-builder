import unittest

from texttotextnodes import *
from textnode import *

class TestTextNodeConversion(unittest.TestCase):
    def test_text_one(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        expected = [
        TextNode("This is ", "PLAIN", None),
        TextNode("text", "BOLD", None),
        TextNode(" with an ", "PLAIN", None),
        TextNode("italic", "ITALIC", None),
        TextNode(" word and a ", "PLAIN", None),
        TextNode("code block", "CODE", None),
        TextNode(" and an ", "PLAIN", None),
        TextNode("obi wan image", "IMAGE", "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", "PLAIN", None),
        TextNode("link", "LINK", "https://boot.dev"),
        ]
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_text_two(self):
        text = "this is a _italic_ word followed by a ![placeholder image](placeholderlink) and a **bold** word with a `code block` and finally a [link](placeholderlink)"
        result = text_to_textnode(text)
        expected = [
            TextNode("this is a ", "PLAIN", None),
            TextNode("italic", "ITALIC", None),
            TextNode(" word followed by a ", "PLAIN", None),
            TextNode("placeholder image", "IMAGE", "placeholderlink"),
            TextNode(" and a ", "PLAIN", None),
            TextNode("bold", "BOLD", None),
            TextNode(" word with a ", "PLAIN", None),
            TextNode("code block", "CODE", None),
            TextNode(" and finally a ", "PLAIN", None),
            TextNode("link", "LINK", "placeholderlink")
        ]
        self.maxDiff = None
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

