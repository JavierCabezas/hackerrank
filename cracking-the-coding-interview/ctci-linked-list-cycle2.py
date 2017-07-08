#This version uses the tortoise and hare method
def has_cycle(head):
    if head is None:
        return False

    fast = head.next
    slow = head
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next

    return False