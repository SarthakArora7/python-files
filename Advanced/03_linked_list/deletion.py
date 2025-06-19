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

# Deletion of head
# def delHead(head):
#     print("After deletion of head LL is: ")
#     head = head.next
#     return head
# printLL(delHead(head))
# printLL(head)

# Deletion of Tail
# def delTail(head):
#     print("After deletion of tail LL is: ")
#     p = head
#     while p.next.next != None:
#         p = p.next
#     p.next = None  # This will detach the last node completely from the linked list.
#     return head
# printLL(delTail(head))
# printLL(head)
# After deletion of tail LL is:
# Linked List:
# 3 5 2 7
# Linked List:
# 3 5 2 7

# Deletion of nth element
def nthElement(head, n):
    print("After deletion of nth element: ")
    if head == None:
        print("No LL exists!")
        return head
    if head.next == None:
        print("Single head is deleted: ")
        head = None
        return head
    p = head
    c = 1
    prev = p
    if c == n:
        head = head.next
    while p != None:
        if c == n:
            prev.next = p.next
            p = None
            return head
        prev = p
        p = p.next
        c += 1
    return head
printLL(nthElement(head, 2))
# After deletion of nth element:
# Linked List:
# 3 5 7

# Deletion of specific node having some value
# def delValue(head, value):
#     print(f"After deletion of {value} LL is: ")
#     if head == None:
#         print("No LL exists!")
#         return head
#     if head.next == None:
#         print("Single head is deleted: ")
#         head = None
#         return head
#     if head.data == value:
#         head = head.next
#         return head
#     p = head
#     while p != None:
#         if p.data == value:
#             prev.next = p.next
#             p = None
#             return head
#         prev = p
#         p = p.next
#     return head
# printLL(delValue(head, 8))