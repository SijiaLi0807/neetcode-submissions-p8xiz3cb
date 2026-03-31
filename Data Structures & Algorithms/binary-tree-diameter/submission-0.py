# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 1 #全局变量
        def height(node):
            if not node:
                return 0
            L = height(node.left) #左子树的高度传递给父节点，作为左路径的长度
            R = height(node.right)
            self.ans = max(self.ans, L+R+1) #迭代路径值
            return max(L,R)+1 #返回高度
        height(root)
        return self.ans - 1