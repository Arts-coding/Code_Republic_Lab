# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def hasCycle(self, head) -> bool:
#         first = head
#         second = head
        
#         while second and second.next:
#             first = first.next
#             second = second.next.next
#             if first == second:
#                 return True
#         return False  


# #OR/

# class Solution(object):
#     def hasCycle(self, head):
#         nodeSet = set()
        
#         while head:
#             if head not in nodeSet:
#                 nodeSet.add(head)
#                 head = head.next
#             else:
#                 return True
        
#         return False

def a(n):
    count = 0
    for i in range(0,n):
        j = i
        for j in range(i,0,-1):
            count += 1

print(4)