class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head):
        stack = []

        while head is not None: 
            while stack and stack[-1] < head.val: 
                stack.pop()
            stack.append(head.val)
            head = head.next


        new_head = ListNode()
        curr = new_head

        for val in stack: 
            curr.next = ListNode(val)
            curr = curr.next

        return new_head.next