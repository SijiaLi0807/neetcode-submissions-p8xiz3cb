# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        d = collections.deque([root]) #first in first out
        while d:
            vec = [] #one-dimensional list for the current level
            for _ in range(len(d)):
                node = d.popleft()
                vec.append(node.val) #注意提交类型
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            res.append(vec)
        return res