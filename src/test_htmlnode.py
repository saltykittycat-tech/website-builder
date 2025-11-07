import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>",)
    
    def test_to_html_no_children(self):
        parent_node = ParentNode("div")
        with self.assertRaises(ValueError) as err:
            parent_node.to_html()
        exception = err.exception
        message = exception.args
        self.assertEqual(message, ('children missing',))

    def test_to_html_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as err:
            parent_node.to_html()
        exception = err.exception
        message = exception.args
        self.assertEqual(message, ('no tag',))
        

if __name__ == "__main__":
    unittest.main()