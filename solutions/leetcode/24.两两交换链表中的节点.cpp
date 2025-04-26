/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
    public:
        ListNode* swapPairs(ListNode* head) {
            if (!head || !head->next) 
                return head;
            ListNode *dummy = new ListNode(-1, head), 
                     *p = head, 
                     *q = head->next;
            ListNode *pre = dummy;
            while (q) {
                // pre -> p -> q
                ListNode *q_ne = q->next;
                pre->next = q;
                p->next = q_ne;    
                q->next = p;
                
                pre = p;
                p = q_ne;
                q = q_ne;
                if (q) q = q->next;
    
                //break;
            }
    
            return dummy->next;
        }
    };
// @lc code=end

