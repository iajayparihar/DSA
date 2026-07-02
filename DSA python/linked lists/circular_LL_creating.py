class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class circular_LinkedList:
    def __init__(self,head=None):
        self.head=head

    def add(self,data):
        new=Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next=new
        else:
            self.head=new
        

    def Plist(self):
        temp = self.head.next
        first = self.head
        while temp != first:
            print(temp.data,end="-->")
            temp= temp.next
        # for the first node 
        print(temp.data)
        temp= temp.next
        

    def cir(self):
        # for circular linked list
        temp1 = self.head
        while temp1.next:
            temp1= temp1.next
        temp1.next=self.head

k=circular_LinkedList()
k.add(500) # first element
for i in range(0,100,10):
    k.add(i)
k.add(501) # last element 
k.cir()
k.Plist()
