import unittest
from textnodecoversion import *
from textnode import *
from htmlnode import *

class TestTextNodeConversion(unittest.TestCase):
    def test_plain(self):
        node = TextNode("This is a text node", "PLAIN")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("this is a text node", "BOLD")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "this is a text node")

    def test_italic(self):
        node = TextNode("this is a text node", "ITALIC")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is a text node")

    def test_code(self):
        node = TextNode("this is a text node", "CODE")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "this is a text node")

    def test_link(self):
        node = TextNode("this is a text node", "LINK", "https://fakeurl")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "this is a text node")
        self.assertEqual(html_node.props, {"href": "https://fakeurl"})
    
    def test_image(self):
        node = TextNode("this is a text node", "IMAGE", "https://fakeimagesource")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,{"src": "https://fakeimagesource", "alt": "this is a text node"})

if __name__ == "__main__":
    unittest.main()