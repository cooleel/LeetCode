#Given a linked list, determine if it has a cycle in it.





class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if hasattr(head,"visited"):
                return True
            head.visited = True
            head = head.next
        return False