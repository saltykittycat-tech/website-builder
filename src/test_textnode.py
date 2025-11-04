import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", "BOLD")
        node2 = TextNode("This is a text node", "BOLD")
        self.assertEqual(node, node2)
    
    def test_noteq1(self):
        node = TextNode("text node", "ITALIC")
        node2 = TextNode("text node", "BOLD")
        self.assertNotEqual(node, node2)
    
    def test_noteq2(self):
        node = TextNode("text node", "PLAIN", "https:://fake_url")
        node2 = TextNode("text node", "PLAIN", "https://differentfakeurl")
        self.assertNotEqual(node, node2)
    
    def test_noteq3(self):
        node = TextNode("text node 1", "ITALIC")
        node2 = TextNode("text node 2", "ITALIC")
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("text node", "ITALIC", None)
        node2 = TextNode("text node", "ITALIC")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()