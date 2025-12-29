import unittest

from splitimagesandlinks import *
from textnode import *


class TestTextNodeConversion(unittest.TestCase):

    def test_twoimagesonenode(self):
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "PLAIN",
        )
        result = split_nodes_image([node])
        expected = [TextNode("This is text with a ", "PLAIN"), TextNode("rick roll", "IMAGE", "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", "PLAIN"),
                     TextNode("obi wan", "IMAGE", "https://i.imgur.com/fJRm4Vk.jpeg") ]
        self.assertEqual(result, expected)

    def test_twolinksonenode(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "PLAIN",
        )
        result = split_nodes_link([node])
        expected = [TextNode("This is text with a link ", "PLAIN"), TextNode("to boot dev", "LINK", "https://www.boot.dev"),
                    TextNode(" and ", "PLAIN"), TextNode("to youtube", "LINK", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result, expected)

    def test_fourlinkstwonodes(self):
        node1 = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "PLAIN",
        )
        node2 = TextNode(
            "This is text with a link [to someplace](https://placeholderlink) and [to some other place](https://anotherplaceholderlink)",
            "PLAIN",
        )
        result = split_nodes_link([node1, node2])
        expected = [TextNode("This is text with a link ", "PLAIN"), TextNode("to boot dev", "LINK", "https://www.boot.dev"),
                    TextNode(" and ", "PLAIN"), TextNode("to youtube", "LINK", "https://www.youtube.com/@bootdotdev"), TextNode("This is text with a link ", "PLAIN"), 
                    TextNode("to someplace", "LINK", "https://placeholderlink"),
                    TextNode(" and ", "PLAIN"), TextNode("to some other place", "LINK", "https://anotherplaceholderlink")]
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_fourimages_twonodes(self):
        node1 = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "PLAIN",
        )
        node2 = TextNode(
            "This is text with a ![random image](https://placeholder) and ![another random image](https://placeholder2)",
            "PLAIN",
        )
        result = split_nodes_image([node1, node2])
        expected = [TextNode("This is text with a ", "PLAIN"), TextNode("rick roll", "IMAGE", "https://i.imgur.com/aKaOqIh.gif"), TextNode(" and ", "PLAIN"),
                     TextNode("obi wan", "IMAGE", "https://i.imgur.com/fJRm4Vk.jpeg"), TextNode("This is text with a ", "PLAIN"), 
                     TextNode("random image", "IMAGE", "https://placeholder"), TextNode(" and ", "PLAIN"),
                     TextNode("another random image", "IMAGE", "https://placeholder2")]
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_noimages_onenode(self):
        node1= TextNode("this is a text with no images", "PLAIN")
        result = split_nodes_image([node1])
        expected = [TextNode("this is a text with no images", "PLAIN")]
        self.maxDiff = None
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()