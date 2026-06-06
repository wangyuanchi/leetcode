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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        int n {right - left + 1};
        if (left == 1) {
            return reverseN(head, n);
        }
        ListNode* cur {head};
        for (int i{1}; i < left - 1; ++i) {
            cur = cur->next;
        }
        cur->next = reverseN(cur->next, n);
        return head;
    }

    ListNode* reverseN(ListNode* head, int n) {
        ListNode* prev {};
        ListNode* cur {head};
        for (int i {}; i < n; ++i) {
            ListNode* temp {cur->next};
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        head->next = cur;
        return prev;
    }
};