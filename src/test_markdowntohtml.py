import unittest
from markdowntohtml import *

class TestHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph text in a p tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.maxDiff = None
        self.assertEqual(html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.maxDiff = None
        self.assertEqual(
        html,
        "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

    def test_links(self):
        md = """ this is a **bolded** paragraph text with a [link](placeholderlink) and _italic_ text

        this is another paragraph

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a <b>bolded</b> paragraph text with a <a href="placeholderlink">link</a> and <i>italic</i> text</p><p>this is another paragraph</p></div>'
        self.assertEqual(expected_html, html)

    def test_images(self):
        md = """this is a _italic_ paragraph text with a ![image](placeholderimagelink) and **bolded text**

this is another paragraph
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a <i>italic</i> paragraph text with a <img src="placeholderimagelink" alt="image" /> and <b>bolded text</b></p><p>this is another paragraph</p></div>'
        self.assertEqual(expected_html, html)

    def test_headings(self):
        md = """this is a **bolded** paragraph text

        ###this is a 3 heading

        ##this is a 2 heading

        #this is a **one** heading with bolded text

        this is another paragraph"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a <b>bolded</b> paragraph text</p><h3>this is a 3 heading</h3><h2>this is a 2 heading</h2><h1>this is a <b>one</b> heading with bolded text</h1><p>this is another paragraph</p></div>'
        self.assertEqual(html, expected_html)

    def test_unorderedlists(self):
        md = """this is a paragraph text with _italic_ text

        this is a new paragraph

- this is
- a unordered
- list

        this is a final paragraph"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a paragraph text with <i>italic</i> text</p><p>this is a new paragraph</p><ul><li> this is</li><li> a unordered</li><li> list</li></ul><p>this is a final paragraph</p></div>'
        #print(f"html: {html}")
        #print(f"expected html: {expected_html}")
        self.assertEqual(html, expected_html)

    def test_orderedlist(self):
        md="""this is a paragraph text

1. this is
2. a ordered
3. list **with** bold text

        this is a final paragraph"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a paragraph text</p><ol><li> this is</li><li> a ordered</li><li> list <b>with</b> bold text</li></ol><p>this is a final paragraph</p></div>'
        #print(f"html: {html}")
        #print(f"expected html: {expected_html}")
        self.assertEqual(html, expected_html)

    def test_quotes(self):
        md = """this is a paragraph

        > this is a quote

        this is another paragraph

        > this is a quote with _italic_ text"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        expected_html = '<div><p>this is a paragraph</p><blockquote> this is a quote</blockquote><p>this is another paragraph</p><blockquote> this is a quote with <i>italic</i> text</blockquote></div>'
        #print(f"html: {html}")
        #print(f"expected html: {expected_html}")
        self.assertEqual(html, expected_html)

if __name__ == "__main__":
    unittest.main()