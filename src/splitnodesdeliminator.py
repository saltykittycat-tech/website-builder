from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type.value != "plain text":
            new_nodes.append(node)
        else:
            text = node.text
            listed_text = text.split(delimiter)
            length = len(listed_text)
            if length % 2 == 0:
                raise Exception("invalid markdown syntax")
            else:
                for i in range(0, length):
                    split_text = listed_text[i]
                    if i % 2 != 0:
                        new_node = TextNode(split_text, text_type)
                    else:
                        new_node = TextNode(split_text, "PLAIN")
                    new_nodes.append(new_node)
    return new_nodes


