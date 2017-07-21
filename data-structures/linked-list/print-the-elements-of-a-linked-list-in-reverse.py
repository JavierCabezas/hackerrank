def ReversePrint(head):
    stack = []
    if head is not None:
        stack.append(head.data)
        while head.next is not None:
            head = head.next
            stack.append(head.data)

        while stack:
            print(stack.pop())