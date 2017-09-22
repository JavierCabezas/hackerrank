def has_cycle(head):
    slow = head
    fast = head

    while slow.next is not None:
        if slow.data == fast.data:
            return True
        else:
            slow = slow.next
            if fast.next is None or fast.next.next is None:
                return True
            else:
                fast = fast.next.next
    return False