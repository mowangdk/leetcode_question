"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution(object):
    """
    @param root: the root of binary tree
    @return an integer
    """

    def maxsum(self, root):
        if root == None: return 0
        sum = root.val
        lmax = 0; rmax = 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax

        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax

        if sum > Solution.max:
            Solution.max = sum

        return max(root.val, max(root.val + lmax, root.val + rmax))

    def maxPathSum(self, root):
        Solution.max = -10000
        if root == None:
            return 0
        self.maxsum(root)
        return Solution.max


