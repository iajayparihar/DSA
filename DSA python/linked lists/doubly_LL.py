class Node:
    def __init__(self,data,next=None,prev=None):
        self.prev = prev
        self.data = data
        self.next = next

class Doubly_linkedList:
    def __init__(self,head=None):
        self.head=head

# previous pointer problem <--
    def add(self,data):
        new=Node(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = new # adding new node to the last 
        else:
            self.head = new
#-----------------------------------------------
#        need 2 pointer's
        first = self.head.next
        last = self.head

        while first.next:
            first.prev=last

    def Plist(self):
        temp = self.head 
        while temp:
            print(temp.data,end="--")
            temp = temp.next
        else:
            print("None")

        # print(temp.prev)
    

k=Doubly_linkedList()
k.add(10)
k.add(20)
k.add(30)
k.Plist()
