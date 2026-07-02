# this class is called when we need new nodes
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# this class is called when we what to create a new linked list
class LinkedList:
    def __init__(self,head=None):
        self.head=head
            # add elements
            
    def add(self,data):
        new = Node(data)
        # self.head is the memory location of the first node
        if self.head:
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next=new
        else:
            self.head=new

    def PList(self,first=None):
        # self.first=first
        first=self.head
        # self.first and first are different from each other
        # print(id(first)) 
        # print(id(self.first))
        while first:
            # fist runs into the last condition 
            # fist.next runs into the second last conditon
            print(first.data,end="-->")
            first=first.next
        else: 
            print("None")

f=LinkedList()
f.add(10)
f.add(20)
f.add(30)
f.add(40)
f.add("A")
f.add([1,2,3])
f.add((4,5,6))
f.add({7,8,9})
f.add({1:"One",2:"Two"})
f.PList()