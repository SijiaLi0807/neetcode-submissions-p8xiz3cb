# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # also bst (like 102)
        if not root:
            return []
        res = []
        d = collections.deque([root])
        while d:
            n = len(d)
            for i in range(n):
                node = d.popleft()
                if i == n - 1:
                    res.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res