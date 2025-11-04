import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_propstohtml1(self):
        node = HTMLNode(None, "this is test text", None, {
        "href": "https://www.google.com",
        "target": "_blank",
        })
        expected =  'href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)
    
    def test_propstohtml2(self):
        node = HTMLNode(None, "this is test text", None, { "src":"url/of/image.jpg", "alt":"Description of image",})
        actual = node.props_to_html()
        expected = 'src="url/of/image.jpg" alt="Description of image"'
        self.assertEqual(expected, actual)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        expected = "<p>Hello, world!</p>"
        actual = node.to_html()
        self.assertEqual(actual, expected)

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        actual = node.to_html()
        self.assertEqual(actual, expected)



if __name__ == "__main__":
    unittest.main()