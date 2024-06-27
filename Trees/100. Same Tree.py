from util import list_to_btree
#  Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

p = [1, 2, 3]
q = [1, 2, 3]

root1 = list_to_btree(p)
root2 = list_to_btree(q)

def sameTree(root1, root2): 
    if not root1 and not root2:
            return True
    if root1 and root2 and root1.val == root2.val:
        return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
    else:
        return False

print(sameTree(root1, root2))