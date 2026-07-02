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
        self.first=first # know its pointing to the last node
        first=self.head
        # print(id(first))
        # print(id(self.first))
        while first:
            print(first.data,end="-->")
            first=first.next
        else:
            print("None")
            # print(self.head.data)         # fist node
            # print(self.head.next.data)    # second node

# insert the node at beginning
    def insert(self,data):
        new = Node(data)
        new.next = self.head
        self.head=new
# insert node at the end of the linked list
    def insert_last(self,data):
        new=Node(data)
        temp=self.head
        
        while temp.next != None: 
            temp=temp.next

        temp.next=new

# delete node by value
    def del_by_value(self,val):
        temp = self.head
        while temp:
            if temp.data == val:
                print("we found")
                break
            else: 
                pre = temp # previous pointer bye temp then temp incresed 
                temp = temp.next
        pre.next = temp.next
        temp.next=None

# Sorting the node from the linked list
    def sort(self):
        temp= self.head
        a=[]
        while temp:
            a.append(temp.data)
            temp=temp.next
        a.sort()
        # making new linked list 
        f = LinkedList() # new is object of ll
        for i in a:
            f.add(i) # with the help of obj, we can call the methods in the method
        f.PList()


f=LinkedList()
f.add(80)
f.add(20)
f.add(70)
f.add(10)
f.add(50)
f.PList()
f.sort()
