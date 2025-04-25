/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
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
        ListNode* getMid(ListNode* head) {
            ListNode *fast = head, *slow = head;
            while (fast != nullptr) {
                slow = slow->next;
                fast = fast->next;
                if (fast != nullptr) 
                    fast = fast->next;
            }
            return slow;
        }
        ListNode* reverseList(ListNode* head) {
            if (head == nullptr)
                return head;
            ListNode *pre = nullptr;
            while (head != nullptr) {
                ListNode *ne = head->next;
                head->next = pre;
                pre = head;
                head = ne;
            }
            return pre;
        }
        bool isPalindrome(ListNode* head) {
            ListNode *mid = getMid(head);
            ListNode *checkpoint = mid;
    
            mid = reverseList(mid);
            while (head != nullptr && mid != nullptr) {
                if (head->val != mid->val || head == checkpoint)
                    return false;
                head = head->next;
                mid = mid->next;
            }
            return true;
        }
    };
// @lc code=end

