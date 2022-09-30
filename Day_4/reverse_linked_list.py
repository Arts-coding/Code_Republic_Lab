from audioop import reverse

def reverseList(head):
        current = head
        prev = None
        
        while current:
            nod = current.next
            current.next = prev
            prev = current
            current = nod
        return prev






        