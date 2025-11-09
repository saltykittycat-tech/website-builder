import unittest

from texttotextnodes import *
from textnode import *

class TestTextNodeConversion(unittest.TestCase):
    def text_one(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnode(text)
        expected = [
        TextNode("This is ", "PLAIN"),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", "PLAIN"),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", "PLAIN"),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", "PLAIN"),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", "PLAIN"),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def text_two(self):
        text = "this is a _italic_ word followed by a ![placeholder image](placeholderlink) and a **bold** word with a `code block` and finally a [link](placeholderlink)"
        result = text_to_textnode(text)
        expected = [
            TextNode("this is a ", "PLAIN"),
            TextNode("italic", "ITALIC"),
            TextNode(" word followed by a ", "PLAIN"),
            TextNode("placeholder image", "IMAGE", "placeholderlink"),
            TextNode(" and a ", "PLAIN"),
            TextNode("bold", "BOLD"),
            TextNode(" word with a ", "PLAIN"),
            TextNode("code block", "CODE"),
            TextNode(" and finally a ", "PLAIN"),
            TextNode("link", "LINK", "placeholderlink")
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

