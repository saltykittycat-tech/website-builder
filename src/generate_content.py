from markdowntohtml import *
from extract_title import *
import os
import pathlib

def generate_content(frm_path, tmplate_path, dst_path):
    location = "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/"
    print(f"Generating page from {frm_path} to {dst_path} using {tmplate_path}")
    from_path = os.path.join(location, frm_path)
    template_path = os.path.join(location, tmplate_path)
    dest_path = os.path.join(location, dst_path)
    f = open(from_path)
    f_text = f.read()
    f.close()
    t = open(template_path)
    t_text = t.read()
    t.close
    html_node = markdown_to_html_node(f_text)
    html_string = html_node.to_html()
    title = extract_title(f_text)
    new_text = t_text.replace("{{ Title }}", title)
    final_text = new_text.replace("{{ Content }}", html_string)
    dest_dir_path = os.path.dirname(dest_path)
    if os.path.exists(dest_dir_path) == False:
        os.makedirs(dest_dir_path)
    d = open(dest_path, "x")
    d.write(final_text)
    d.close

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    print(f"recursively generating")
    starting_level = dir_path_content
    starting_level_files = os.listdir(starting_level)
    files = []
    to_travel = []
    traveled = []
    md_files = []
    for item in starting_level_files:
        path = os.path.join(starting_level, item)
        is_file = os.path.isfile(path)
        if is_file == True:
            file = pathlib.Path(path)
            files.append(file)
        elif is_file == False:
            to_travel.append(path)
    while len(to_travel) != 0:
       #print(f"to travel = {to_travel}")
       to_travel, traveled, files = recursive_pages(to_travel[0], to_travel, traveled, files)
    for file in files:
        #print(f"checking file {file}")
        suffix = file.suffix
        if suffix == '.md':
            md_files.append(file)
    for md_file in md_files:
        partial_path_new = md_file.relative_to(starting_level)
        path_new = os.path.join(dest_dir_path, partial_path_new)
        path_new_class = pathlib.Path(path_new)
        full_path_new = path_new_class.with_suffix(".html")
        generate_content_V2(md_file, template_path, full_path_new)


def recursive_pages(dir_path, to_travel, traveled, files):
    current_level = dir_path
    #print(f"current level = {current_level}")
    traveled.append(current_level)
    to_travel.pop(0)
    current_level_files = os.listdir(current_level)
    for item in current_level_files:
        path = os.path.join(current_level, item)
        is_file = os.path.isfile(path)
        if is_file == True:
            file = pathlib.Path(path)
            files.append(file)
        elif is_file == False:
            to_travel.append(path)
    return to_travel, traveled, files




def generate_content_V2(frm_path, tmplate_path, dst_path):
    #print(f"Generating page from {frm_path} to {dst_path} using {tmplate_path}")
    from_path = frm_path
    template_path = tmplate_path
    dest_path = dst_path
    f = open(from_path)
    f_text = f.read()
    f.close()
    t = open(template_path)
    t_text = t.read()
    t.close
    html_node = markdown_to_html_node(f_text)
    html_string = html_node.to_html()
    title = extract_title(f_text)
    new_text = t_text.replace("{{ Title }}", title)
    final_text = new_text.replace("{{ Content }}", html_string)
    dest_dir_path = os.path.dirname(dest_path)
    if os.path.exists(dest_dir_path) == False:
        os.makedirs(dest_dir_path)
    d = open(dest_path, "x")
    d.write(final_text)
    d.close
    