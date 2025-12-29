from textnode import *
from imageandlinkextraction import *

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        image_texts = extract_markdown_images(text)
        if len(image_texts) == 0:
            new_nodes.append(node)
        else:
            for i in range(0, len(image_texts)):
                image_tuple = image_texts[i]
                image_string = f"![{image_tuple[0]}]({image_tuple[1]})"
                image_removed = text.split(image_string, 1)
                before_image = image_removed[0]
                before_image_node = TextNode(before_image, "PLAIN")
                new_nodes.append(before_image_node)
                image_node = TextNode(image_tuple[0], "IMAGE", image_tuple[1])
                new_nodes.append(image_node)
                after_image_text = image_removed[1]
                after_image_node = TextNode(after_image_text, "PLAIN")
                text = after_image_text
                if i == (len(image_texts) - 1) and after_image_text != "":
                    new_nodes.append(after_image_node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
        link_texts = extract_markdown_links(text)
        if len(link_texts) == 0:
            new_nodes.append(node)
        else:
            for i in range(0, len(link_texts)):
                link_tuple = link_texts[i]
                link_string = f"[{link_tuple[0]}]({link_tuple[1]})"
                link_removed = text.split(link_string, 1)
                before_link = link_removed[0]
                before_link_node = TextNode(before_link, "PLAIN")
                new_nodes.append(before_link_node)
                link_node = TextNode(link_tuple[0], "LINK", link_tuple[1])
                new_nodes.append(link_node)
                after_link_text = link_removed[1]
                text = after_link_text
                if i == (len(link_texts) - 1) and after_link_text != "":
                    after_link_node = TextNode(after_link_text, "PLAIN")
                    new_nodes.append(after_link_node)
    return new_nodes
