class Node:
    def __init__(self,val,add=None):
        self.data=val
        self.next=add

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)

    def insert_begnning(self,data):
        node=Node(data,self.head)
        self.head=node

    def insert_last(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        
    def insert_pos(self,pos,data):
        newnode=Node(data)
        prev=0
        cur=self.head
        for _ in range(pos-1):
            prev=cur
            cur=cur.next
        newnode.next=cur
        prev.next=newnode

    def display(self):

        if self.head is None:
            print('Linked list is empty')
            return
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        else:
            print("None")

l=LinkedList()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert_pos(3, 40)
l.display()