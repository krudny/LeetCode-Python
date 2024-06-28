from util import list_to_btree, tree_to_list

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
targetSum = 22

root = list_to_btree(root)

def pathSum(root): 
    if not root: 
        return False
    
    def dfs(root, curr_sum): 
        if not root.left and not root.right: 
            if curr_sum == targetSum: 
                return True
            return False
        
        left, right = False, False
        
        if root.left:
            left = dfs(root.left, curr_sum + root.left.val)
            
        if root.right:
            right = dfs(root.right, curr_sum + root.right.val)

        return left or right
    
    return dfs(root, root.val)





print(pathSum(root))