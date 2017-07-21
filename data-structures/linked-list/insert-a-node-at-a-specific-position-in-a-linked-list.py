def InsertNth(head, data, position):
    if head is None:
        return Node(data)
    if position == 0:
        return Node(data, head)

    start = head
    for i in range(position + 1):
        if head.next is not None:
            head = head.next
    head = Node(data, start.next)
    return head
