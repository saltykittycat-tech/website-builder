from markdowntoblocks import *
from blocktype import *
import re


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    title = blocks[0]
    title_type = block_to_block_type(title)
    if title_type != "HEAD":
        raise Exception("No title")
    title_number = check_heading_number(title)
    if title_number != 1:
        raise Exception("No title")
    final_title = strip_title(title)
    return final_title
    
    
def check_heading_number(block):
     hashtags = re.findall(r"#", block)
     heading_number = len(hashtags)
     return heading_number

def strip_title(title):
    no_hashtags = title.strip("#")
    no_whitespace = no_hashtags.strip()
    return no_whitespace