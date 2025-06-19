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
    length = 0
    while temp:
        print(temp.data)
        temp = temp.next
        length = length + 1
    print(f"Lenght of Linked List: {length}")

def checkIfPresent(head, n):
    p = head
    while p:
        if p.data == n:
            return True
        p = p.next
    return False

arr = [3,5,2,7,8]

head = array_to_linkedlist(arr)

# To print the data of head.
print("Head Data: ",array_to_linkedlist(arr).data)

# To print Linked List and its length.
printLL(head)  

# To check if an element exist in a linked list.
n = 7
print(f"Is {n} exist in Linked List? ",checkIfPresent(head, n))