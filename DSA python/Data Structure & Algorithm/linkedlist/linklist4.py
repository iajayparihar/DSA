class Node:
    def __init__(self,data,next1=None):
        self.data=data
        self.next=next1

class LinkedList4:
    def __init__(self):
        self.head=None

    def insert_begning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb

    def insert_position(self,data,pos):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
    
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne

    def delete_at_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_at_last(self):
        temp=self.head.next
        pre=self.head
        while temp.next is not None:
            temp=temp.next
            pre=pre.next
        pre.next=None

    
    def delete_position(self,pos):
        temp=self.head.next
        pre=self.head
        for i in range(1,pos-1):
            temp=temp.next
            pre=pre.next
        pre.next=temp.next
        temp.next=None

    def display(self):
        temp=self.head
        if self.head is None:
            print("Linked list is empty")
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("None")
        print()

        
ll=LinkedList4()
ll.insert_begning(10)
ll.insert_begning(20)
ll.insert_begning(30)
ll.insert_begning(40)
ll.display()
# ll.delete_at_first()
# ll.delete_at_first()
# ll.delete_at_first()
# ll.delete_at_last()
# ll.delete_position(3)
# ll.delete_position(3)
ll.display()