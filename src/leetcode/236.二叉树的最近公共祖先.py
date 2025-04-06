#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        le = self.lowestCommonAncestor(root.left, p, q)
        ri = self.lowestCommonAncestor(root.right, p, q)
        if le and ri:
            return root 
        elif le and not ri:
            return le 
        elif not le and ri:
            return ri 
        else:
            return None
        
# @lc code=end

