from sourcetodestination import *
from generate_content import *
import sys

def main():
    sourcetodestination("static", "docs")
    arguments = sys.argv
    if len(arguments) < 2:
        basepath = '/'
    else:
        basepath = arguments[1]
    generate_pages_recursive("/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/content", "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/template.html", "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/docs", basepath)
    #generate_content("content/index.md", "template.html", "public/index.html")
    
main()
