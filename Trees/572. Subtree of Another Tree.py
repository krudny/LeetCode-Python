from util import list_to_btree, tree_to_list

# Given the roots of two binary trees root and subRoot, return true
# if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.

# root = [3,4,5,1,2]
# subRoot = [4,1,2]

root = [3,4,5,1,2,None,None,None,None,0]
subRoot = [4,1,2]

root1 = list_to_btree(root)
root2 = list_to_btree(subRoot)

def isSubtree(root, subRoot): 
    if not subRoot:
        return True
    if not root: 
        return False
    
    def isSameTree(tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
            
        return (tree1.val == tree2.val and 
                isSameTree(tree1.left, tree2.left) and 
                isSameTree(tree1.right, tree2.right))

    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

print(isSubtree(root1, root2))