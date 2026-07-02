class Node:
    def __init__(self,data,add=None):
        self.data=data
        self.next=add

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode

    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        else:
            print('None')

    def insertFirst(self,data):
        if self.head is None:
            newNode=Node(data)
            self.head=newNode
            return 
        newNode=Node(data,self.head)
        self.head=newNode

    def insertPos(self,pos,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return 
        prev=0
        cur=self.head
        while pos>0:
            prev=cur
            cur=cur.next
            pos-=1
        newNode.next=cur
        prev.next=newNode
    
    def rev(self):
        prev=0
        cur=self.head
        fu=self.head
        while cur:
            fu=fu.next
            cur.next=prev
            prev=cur
            cur=fu
        self.head=prev
    #----------------------------------------------------
    def recur(self,head,cur,prev):
        if cur==None:
            self.head=prev
            return 
        self.recur(self.head,cur.next,cur)
        cur.next=prev
        

    def recursive(self):
        prev=0
        cur=self.head
        fu=self.head
        self.recur(fu,cur,prev)
    #----------------------------------------------------
        

l=Linkedlist()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
# l.insertPos(1, 56) # by index positioning
l.display()
l.recursive()
l.display()