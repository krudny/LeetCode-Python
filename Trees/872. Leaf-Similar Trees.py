from util import list_to_btree

# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

root1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,8,9]
root2 = [1,2,3,10,11,12,13]

root1 = list_to_btree(root1)
root2 = list_to_btree(root2)

def leafSimilar(root1, root2): 
    def dfs(root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return dfs(root.left) + dfs(root.right)
        
    leaves1 = dfs(root1)
    leaves2 = dfs(root2)
    
    return leaves1 == leaves2


        





print(leafSimilar(root1, root2))