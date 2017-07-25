def SortedInsert(node_list):
   if len(node_list) == 0:
       return Node()

   head = Node(node_list.pop(0))
   while len(node_list) > 0:
        node_to_insert = Node(node_list.pop(0))
        stop = False
        while not stop:
            if node_to_insert.data > head.data:
                if head.next is None:
                    head.next = node_to_insert
                    node_to_insert.prev = head
                    stop = True
                elif node_to_insert.data < head.next.data:
                    node_to_insert.next = head.next
                    head.next.prev = node_to_insert
                    node_to_insert.prev = head
                    head.next = node_to_insert
                    stop = True
                else:
                   head = head.next
            elif node_to_insert.data < head.data:
               if head.prev is None:
                   head.prev = node_to_insert
                   node_to_insert.next = head
                   stop = True
               else:
                   head = head.prev

   while head.prev is not None: #return head to beggining
       head = head.prev

   return head

test_number = int(input())
all_lists = []
for _ in range(test_number):
   number_of_nodes = int(input())
   all_lists.append([int(x) for x in input().split(" ")])

for node_list in all_lists:
   SortedInsert(node_list)



