from util import list_to_btree, tree_to_list

# Given the root node of a binary search tree and two integers low and high, 
# return the sum of values of all nodes with a value in the inclusive range [low, high].

root = [10, 5, 15, 3, 7,None, 18]
low = 7
high = 15

root = list_to_btree(root)

def rangeSumBST(root, low, high): 
    result = 0

    def dfs(root):
        nonlocal result
        if not root: 
            return 
        
        if root.val in range(low, high + 1): 
            result += root.val

        dfs(root.left)
        dfs(root.right)


    dfs(root)
    return result

print(rangeSumBST(root, low, high))