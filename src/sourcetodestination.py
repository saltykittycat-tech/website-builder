import shutil
import os

def sourcetodestination(source, destination):
    location = "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/"
    cleardestination(destination, location)
    srcpath = os.path.join(location, source)
    destpath = os.path.join(location, destination)
    srcdirlist = listsourcedir(srcpath)
    print(f"source directory list: {srcdirlist}")
    copysrctodest(srcpath, destpath, srcdirlist)
    print("content copied")

def cleardestination(destination, location):
    path = os.path.join(location, destination)
    shutil.rmtree(path, ignore_errors=False)
    os.mkdir(path)
    return path

def listsourcedir(sourcepath):
    dirlist = os.listdir(sourcepath)
    return dirlist

def copysrctodest(sourcepath, destinationpath, srcdirlist):
    dest_path = destinationpath
    for item in srcdirlist:
        srcpath = sourcepath
        item_path = os.path.join(srcpath, item)
        is_file = os.path.isfile(item_path)
        if is_file == True:
            shutil.copy(item_path, dest_path)
            print(f"{item} copied")
        elif is_file == False:
            new_list = listsourcedir(item_path)
            new_dir = os.path.join(dest_path, item)
            os.mkdir(new_dir)
            print(f"recursing into {item_path}")
            copysrctodest(item_path, new_dir, new_list)