# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        ans = []
        q = []
        if root:
            q.append(root)
        while q:
            levelsize = len(q)
            for i in range(levelsize):
                node = q.pop(0)
                if levelsize <= 1:
                    ans.append(node.val)
                elif i == 0 or i == levelsize-1:
                    ans.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return ans