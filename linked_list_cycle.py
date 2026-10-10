class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode) -> bool:
    un=head
    dos=head

    while dos is not None and dos.next is not None:
        un = un.next
        dos =dos.next.next

        if un is dos:
            return True

    return False