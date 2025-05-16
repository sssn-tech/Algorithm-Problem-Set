#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge2(h1, h2):
            dummy = curr = ListNode(-1)
            while h1 and h2:
                if h1.val <= h2.val:
                    curr.next = h1 
                    h1 = h1.next
                else:
                    curr.next = h2 
                    h2 = h2.next
                curr = curr.next
            curr.next = h1 if h1 else h2 
            return dummy.next

        dummy = ListNode(-float('inf'))
        for head in lists:
            dummy = merge2(dummy, head)
        return dummy.next
        
# @lc code=end

