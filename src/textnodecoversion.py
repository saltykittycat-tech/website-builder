from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    try:
        if text_node.text_type.value == "plain text":
            node = LeafNode(None, text_node.text)
            return node
        elif text_node.text_type.value == "Bold text":
            node = LeafNode("b", text_node.text)
            return node
        elif text_node.text_type.value == "Italic text":
            node = LeafNode("i", text_node.text)
            return node
        elif text_node.text_type.value == "Code text":
            node = LeafNode("code", text_node.text)
            return node
        elif text_node.text_type.value == "link":
            node = LeafNode("a", text_node.text, {"href": text_node.url})
            return node
        elif text_node.text_type.value == "image":
            node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
            return node
    except Exception as e:
        raise Exception("invalid text type")
    