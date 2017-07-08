#This version uses the tortoise and hare method
def has_cycle(head):
    if head is None:
        return False

    fast = head.next
    slow = head

    while fast is not None or fast.next is not None:
        if fast == slow:
            return True

        fast = fast.next.next
        slow = slow.next

    return False