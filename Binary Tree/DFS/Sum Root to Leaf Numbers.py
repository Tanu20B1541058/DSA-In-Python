# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        self.ans = 0
        def solve(root, csum):
            if not root:
                return
            csum = csum*10 + root.val
            if not root.left and not root.right:
                self.ans += csum
                return
            solve(root.left, csum)
            solve(root.right,  csum)
        solve(root,  0)
        return self.ans