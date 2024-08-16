from typing import Optional

metadata = {
    'title': '206. Reverse Linked List',
    'link': 'https://leetcode.com/problems/reverse-linked-list/description/',
    'difficulty': 'easy',
    'tags': ['linked list']
}

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        
        prevNode = None
        currNode = head
        nextNode = head.next

        while nextNode is not None:
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            nextNode = currNode.next
            if nextNode is None:
                currNode.next = prevNode
        
        return currNode