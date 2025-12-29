from splitnodesdeliminator import *
from splitimagesandlinks import *
from textnode import *

def text_to_textnode(text):
    first_node = TextNode(text, "PLAIN", None)
    #print(f"text to text node first node {first_node}")
    images_split = split_nodes_image([first_node])
    #print(f"text to text node image split {images_split}")
    links_split = split_nodes_link(images_split)
    #print(f"text to text node links split {links_split}")
    bold_split = split_nodes_delimiter(links_split, "**", "BOLD")
    #print(f"text to text node bold split {bold_split}")
    italic_split = split_nodes_delimiter(bold_split, "_", "ITALIC")
   # print(f"text to text node italic split {italic_split}")
    code_split = split_nodes_delimiter(italic_split, "`", "CODE")
   # print(f"text to text node final node {code_split}")
    return code_split