# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def levelSymetric(nums):
            return nums[:] == nums[::-1]

        tree = [root]
        while tree:
            level = []
            for _ in range(len(tree)):
                tmp = tree.pop(0)
                if not tmp:
                    level.append(None)
                else:
                    level.append(tmp.val)
                    tree.append(tmp.left)
                    tree.append(tmp.right)
            if not levelSymetric(level):
                return False
        return True