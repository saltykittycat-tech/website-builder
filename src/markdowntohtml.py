from markdowntoblocks import *
from blocktype import *
from htmlnode import *
from textnode import *
from textnodecoversion import *
import re
from texttotextnodes import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        #print(f" block type: {block_type}")
        if block_type == "CODE":
            html_node = code_type_to_html_node(block)
            html_nodes.append(html_node)
        else:
            html_node = block_to_html_node(block, block_type)
            html_nodes.append(html_node)
    parent_node = ParentNode("div", html_nodes)
    return parent_node
                

            
        

def block_to_html_node(block, block_type):
    if block_type == "PARAGRAPH":
        children = text_to_children(block)
        html_node = ParentNode("p",children)
    elif block_type == "HEAD":
        hashtags = re.findall(r"#", block)
        heading_number = len(hashtags)
        heading_tag = f"h{heading_number}"
        text = block.strip("#")
        children = text_to_children(text)
        html_node = ParentNode(heading_tag, children)
    elif block_type == "QUOTE":
        text = block.strip(">")
        children = text_to_children(text)
        html_node = ParentNode("blockquote", children)
    elif block_type == "UNORDERED_LIST":
        block_lines = block.split("\n")
        #print(f"block lines: {block_lines}")
        child_nodes = []
        for line in block_lines:
            new_line = line.split("-")
            final_line = new_line[1]
            children = text_to_children(final_line)
            node = ParentNode("li", children)
            child_nodes.append(node)
        html_node = ParentNode("ul", child_nodes)
    elif block_type == "ORDERED_LIST":
        block_lines = block.split("\n")
        child_nodes = []
        for line in block_lines:
            new_line = line.split(".")
            final_line = new_line[1]
            children = text_to_children(final_line)
            node = ParentNode("li", children)
            child_nodes.append(node)
        html_node = ParentNode("ol", child_nodes)
    return html_node

def text_to_children(text):
    text_nodes = text_to_textnode(text)
    children_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children_nodes.append(html_node)
    return children_nodes


def code_type_to_html_node(block):
    text = block.strip("```")
    text_node = TextNode(text, "CODE")
    child_node = text_node_to_html_node(text_node)
    html_node = ParentNode("pre", [child_node])
    return html_node

