from splitnodesdeliminator import *
from splitimagesandlinks import *
from textnode import *

def text_to_textnode(text):
    first_node = TextNode(text, "PLAIN", None)
    images_split = split_nodes_image([first_node])
    links_split = split_nodes_link(images_split)
    bold_split = split_nodes_delimiter(links_split, "**", "BOLD")
    italic_split = split_nodes_delimiter(bold_split, "_", "ITALIC")
    code_split = split_nodes_delimiter(italic_split, "`", "CODE")
    return code_split