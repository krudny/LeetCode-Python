from util import list_to_btree

# Given the root of a binary tree, return its maximum depth.

# A binary tree maximum depth is the number of nodes along 
# the longest path from the root node down to the farthest leaf node.

elements = [3, 9, 20, None, None, 15, 7]
root = list_to_btree(elements)

def maxDepth(root): 
    if not root: 
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
    
print(maxDepth(root))
