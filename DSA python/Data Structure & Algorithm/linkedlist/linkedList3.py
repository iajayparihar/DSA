class Node:
    def __init__(self,data,next1=None):
        self.data=data
        self.next=next1
class LinkedList3:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return

        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
            

ll=LinkedList3()
ll.insert(10)
ll.insert(11)
ll.display()