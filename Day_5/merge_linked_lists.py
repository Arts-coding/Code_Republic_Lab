class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def solution(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
        
    current = dummy = ListNode(0)
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next
            
print(solution([1, 2, 3],[4, 5, 6]))
