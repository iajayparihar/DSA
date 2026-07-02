class Node:
    def __init__(self,d):
        self.data=d
        self.next=None

class Linklist1:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if self.head is None:
            print("Linked list is empty.")
        while temp:
            print(temp.data)
            temp=temp.next


ll=Linklist1()
n1=Node(10)
n2=Node(20)
n3=Node(30)

ll.head=n1
n1.next=n2
n2.next=n3
ll.display()