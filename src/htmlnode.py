class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception
    
    def props_to_html(self):
        end_string = ""
        for key in self.props:
            new_string = f'{key}="{self.props[key]}"'
            if end_string == "":
                end_string = end_string + new_string
            else:
                end_string = end_string + " " + new_string
        return end_string
    
    def __repr__(self):
        string = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        return string
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        super()

    def to_html(self):
        if self.value == None:
            raise Exception(ValueError)
        if self.tag == None:
            return self.value
        else:
            if self.props == None:
                tag_start = f"<{self.tag}>"
            else:
                props = self.props_to_html()
                tag_start = f"<{self.tag} {props}>"
            tag_end = f"</{self.tag}>"
            text = self.value
            final_string = tag_start + text + tag_end
            return final_string
    