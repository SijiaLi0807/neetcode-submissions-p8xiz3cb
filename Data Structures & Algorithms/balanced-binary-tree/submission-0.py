# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            leftheight = height(node.left)
            rightheight = height(node.right)
            if leftheight == -1 or rightheight == -1 or abs(leftheight-rightheight)>1:
                return -1
            else:
                return max(leftheight,rightheight)+1
        if height(root)==-1:
            return False
        else:
            return True
            