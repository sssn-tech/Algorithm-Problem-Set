#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def find_mid(head):
            fast = slow = head
            while fast:
                fast = fast.next
                if fast:
                    fast = fast.next
                if fast:
                    slow = slow.next
            return slow

        def merge_sort(head1):
            if not head1 or not head1.next:
                return head1 
            mid = find_mid(head1)
            head2 = mid.next
            mid.next = None 
            head1 = merge_sort(head1)
            head2 = merge_sort(head2)

            # 合并两个有序链表head1, head2
            dummy = curr = ListNode(-1)
            while head1 and head2:
                if head1.val <= head2.val:
                    curr.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    curr.next = ListNode(head2.val)
                    head2 = head2.next
                curr = curr.next
            curr.next = head1 if head1 else head2
            return dummy.next

        return merge_sort(head)
        
# @lc code=end

