# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Edge case
        if head == None:
            return False
        # method to find if the linked list has a cycle
        slow = head
        fast = head.next
        while slow!=fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         slow, fast = head, head
        
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
        