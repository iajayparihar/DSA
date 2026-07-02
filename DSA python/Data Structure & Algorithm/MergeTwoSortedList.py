# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def __init__(self):
        self.head1=None
        self.head2=None

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.head1=list1[0]
        self.head2=list2[0]

        while list1 and list2:
            list1=N=ListNode()

        print(list1)
        print(list2)



mer=Solution()

list1 = [1,2,4]
list2 = [1,3,4]
a=mer.mergeTwoLists(list1, list2)
print(a)