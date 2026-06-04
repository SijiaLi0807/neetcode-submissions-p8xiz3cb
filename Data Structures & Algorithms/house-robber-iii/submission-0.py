# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robtree(self, cur: Optional[TreeNode]) -> list:
        if not cur:
            return [0,0]
        
        #post-order
        leftdp = self.robtree(cur.left)
        rightdp = self.robtree(cur.right)
        #dp[0]: non-robbed itself; dp[1]: robbed itself

        val1 = cur.val + leftdp[0] +rightdp[0] #偷自己
        val2 = max(leftdp[0], leftdp[1])+ max(rightdp[0], rightdp[1]) #不偷自己
        return [val2, val1]

    def rob(self, root: Optional[TreeNode]) -> int:
        res = self.robtree(root)
        return max(res[0], res[1])