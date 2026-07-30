# Recurse
def recurse_children(node, depth = 0):
    """Recursive function to print out all sub-elements of ANSYS mechanical injected model class"""
    print("  " * depth + getattr(node, "Name", "<unnamed>")) #NOTE: some attributes will be unnamed
    for child in node.Children:
        recurse_children(child, depth + 1)
recurse_children(DataModel.Project.Model)

