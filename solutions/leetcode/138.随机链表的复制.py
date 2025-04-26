#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        p = dummy_p = Node(-1, head, None)
        q = dummy_q = Node(-1, None, head)
        p_pre = q_pre = None
        
        while p:
            p_ne = p.next
            p.next = q 
            p = p_ne
            if not p:
                break
            q.next = Node(p.val, None, p)
            q = q.next

        q = dummy_q
        while q:
            q.random = q.random.random
            if q.random:
                q.random = q.random.next
            q = q.next

        return dummy_q.next


        
# @lc code=end

