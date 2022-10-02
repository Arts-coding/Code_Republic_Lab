def removeElements( head, val: int):
        prev = None 
        current = head

        while current:
            if current.val == val:  
                if prev: 
                    prev.next = current.next
                else: 
                    head = current.next
                current = current.next  
            else:  
                prev, current = current, current.next
                
        return head