class Solution:
    def hasCycle(self, head: Opitonal[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if slow is fast:
                return True
        return False
    
    #time: O(n)    space: O(1)