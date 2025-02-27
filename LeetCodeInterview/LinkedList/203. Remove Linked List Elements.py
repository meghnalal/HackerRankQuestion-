def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    current = head
    prev = None
    while current:
        if current.val == val:
            if prev:
                prev.next = current.next
            else:
                head = current.next
            current = current.next
        else:
            prev = current
            current = current.next
    return head