class Node:
    def __init__(self, data=None,next1=None):
        self.data=data
        self.next=next1
class LinkedList2:
    def __init__(self):
        self.head=None
    def insert_at_first_Node(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert(self,data):
        if self.head is None:
            self.head=Node(data,None) # Node(data,None) --> address of data
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data,None)

    def display(self):
        if self.head is None:
            print("Linked list id empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        else:
            print("None")
ll=LinkedList2()
ll.insert(10)
ll.insert(107)
ll.insert_at_first_Node(20)
ll.display()

