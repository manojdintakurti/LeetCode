# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        def level(i,root):
            if not root:
                return
            if len(res) == i:
                res.append([root.val])
            else:
                res[i].append(root.val)
            if root.left:
                level(i+1,root.left)
            if root.right:
                level(i+1, root.right)
            return res
        return level(0,root)