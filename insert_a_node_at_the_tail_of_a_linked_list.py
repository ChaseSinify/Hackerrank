

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    temp = head
    val = SinglyLinkedListNode(data)
    if head == None:
        head = val
    else:
        while temp.next:
                temp = temp.next
        temp.next = val
    return head
    

