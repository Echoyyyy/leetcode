# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            l3 = ListNode(0) 
            last_node = l3
            val = 0
            while(l1 or l2):
                if l1:
                    val += l1.val
                    l1 = l1.next
                if l2:
                    val += l2.val
                    l2 = l2.next               
                last_node.next = ListNode(val%10) 
                val = val//10
                last_node = last_node.next 
            
            if val:
               last_node.next = ListNode(1) 
            l3 = l3.next    
            
            return l3
        
        
        
        
        
        