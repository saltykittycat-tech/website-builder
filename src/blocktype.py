from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph block"
    HEAD = "heading block"
    CODE = "code block"
    QUOTE = "quote block"
    UNORDERED_LIST = "unordered list block"
    ORDERED_LIST = "ordered list block"

def block_to_block_type(markdown):
    hashtags = re.findall(r"#", markdown)
    back_ticks = re.findall(r"```", markdown)
    code = is_code(markdown)
    quotes = markdown.split()
    block_lines = markdown.split("\n")
    length_of_unordered_list = []
    ordered_list_numbers = []
    has_space = []
    for line in block_lines:
        found = line.find("- ")
        if found != -1:
            length_of_unordered_list.append(line)
    for line in block_lines:
        split_line = line.split(".")
        number = split_line[0]
        ordered_list_numbers.append(number)
        space = line.find(". ")
        if space != -1:
            has_space.append(True)
    ordered_list_in_order = check_list_numbers_are_in_order(ordered_list_numbers)
    if len(hashtags) <= 6 and len(hashtags)>= 1:
        block_type = "HEAD"
    elif len(back_ticks) == 2 and code == True:
        block_type = "CODE"
    elif quotes[0] == ">":
        block_type = "QUOTE"
    elif len(length_of_unordered_list) == len(block_lines):
        block_type = "UNORDERED_LIST"
    elif ordered_list_in_order == True and len(has_space) == len(block_lines):
        block_type = "ORDERED_LIST"
    else:
        block_type = "PARAGRAPH"
    return block_type

def check_list_numbers_are_in_order(numbers):
    prev_number = 0
    for number in numbers:
        num = number
        expected = str(prev_number + 1)
        if num == expected:
            prev_number = int(expected)
        elif num != expected:
            return False
    return True

def is_code(markdown):
    split_md = markdown.split("```")
    extra = []
    for item in split_md:
        find_extra = re.findall(r"`", item)
        if len(find_extra) != 0:
            extra.append(find_extra)
    if len(extra) == 0:
        return True
    else:
        return False
    
