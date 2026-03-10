from sourcetodestination import *
from generate_content import *

def main():
    sourcetodestination("static", "public")
    generate_pages_recursive("/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/content", "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/template.html", "/home/saltykittycat/workspace/github.com/saltykittycat-tech/website-builder/public")
    #generate_content("content/index.md", "template.html", "public/index.html")

main()
