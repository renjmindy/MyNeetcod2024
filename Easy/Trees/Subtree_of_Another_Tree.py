# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSametree(self, p, q):

        if p == q: return True
        elif not p or not q: return False
        else:
            return p.val == q.val and self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root: return False
        elif not subRoot: return True
        else: return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
