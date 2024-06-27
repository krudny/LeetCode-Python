from util import list_to_btree, tree_to_list

# Given the root of a binary tree, invert the tree, and return its root.

elements = [4,2,7,1,3,6,9]
root = list_to_btree(elements)

def invertTree(root): 
    if not root: 
        return
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root


print(tree_to_list(invertTree(root)))



