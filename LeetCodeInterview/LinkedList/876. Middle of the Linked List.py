'''
876. Middle of the Linked List
'''

'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

'''


def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = [1,2,3,4,5]
middleNode(head)

# the quicker way but cheating in an interview
def middleNode(self, head: ListNode) -> ListNode:
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return arr[len(arr) // 2]