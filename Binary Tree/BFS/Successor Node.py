# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root, targetNode):
        ans = []
        q = []
        if root:
            q.append(root)
        while q:
            levelSize = len(q)
            for i in range(len(q)):
                node = q.pop(0)
                if node == targetNode:
                    if len(q) == 0:
                        return -1
                    return q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return ans