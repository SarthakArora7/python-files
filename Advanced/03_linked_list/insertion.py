class Node():
    def __init__(self, x, pointer=None):
        self.data = x
        self.next = pointer

def array_to_linkedlist(arr):
    head = Node(arr[0])
    p = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        p.next = temp
        p = temp
    return head

def printLL(head):
    print("Linked List: ")
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

arr = [3,5,2,7,8]
head = array_to_linkedlist(arr)
printLL(head)

# # Insertion at head
# def insertAtHead(head, el):
#     n = Node(el)
#     n.next = head
#     head = n
#     return head
# printLL(insertAtHead(head, 4))

# def insertAtTail(head, el):
#     n = Node(el)
#     p = head
#     while p.next is not None:
#         p = p.next
#     p.next = n
#     return head
# printLL(insertAtTail(head, 9))  # this 9 will be added at the last of the actual linked list. And will be printed whenever we print head.

# Insert at nth element
# def insertAtnthElement(head, value, el):
#     n = Node(value)
#     if head is None:
#         if el == 1:
#             head = n
#             return head
#         else:
#             print("There is no linked list!")
#     if el == 1:
#         n.next = head
#         head = n
#         return head
#     p = head
#     c = 1
#     while p is not None:
#         if c == el-1:
#             n.next = p.next
#             p.next = n
#             return head
#         c += 1
#         p = p.next
#     return head
# printLL(insertAtnthElement(head, 100, 6))

# Insert before a specific value
def insertBeforeValue(head, value, new_node):
    if head == None:
        print("There is no Linked List!")
    if head.data == value:
        n = Node(new_node, head)
        head = n
        return head
    p = head
    while p.next != None:
        if p.next.data == value:
            n = Node(new_node, p.next)
            p.next = n
            return head
        p = p.next
    return head
printLL(insertBeforeValue(head, 9, 100))