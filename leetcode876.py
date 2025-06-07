class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[Listode]:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    
#time: O(n)    space: O(1)