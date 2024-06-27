class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def list_to_btree(elements): 
    if not elements: 
        return 
    
    root = TreeNode(elements[0])
    queue = [root]
    i = 1

    while i < len(elements): 
        current = queue.pop(0)

        if i < len(elements) and elements[i] is not None: 
            current.left = TreeNode(elements[i])
            queue.append(current.left)
        i += 1

        if i < len(elements) and elements[i] is not None: 
            current.right = TreeNode(elements[i])
            queue.append(current.right)
        i += 1

    return root


def tree_to_list(root): 
    result = []
    

    def bfs(root):
        Q = [root]

        while Q: 
            root = Q.pop(0)

            result.append(root.val)

            if root.left: 
                Q.append(root.left)

            if root.right: 
                Q.append(root.right)

        
    bfs(root)

    return result



