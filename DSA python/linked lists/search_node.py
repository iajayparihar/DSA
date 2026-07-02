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
# searching the node from the linked list
    def search_Node(self,val):
        print("The given element is:- ",val)
        temp=self.head
        idx=0
        while temp:
            if temp.data == val:
                print("The given value is found:- ",idx)
                break
            temp=temp.next
            idx+=1
        else: # this else is not elecuted when if condition hit's the break statement
            print("Element is not fount in the linked list.")

f=LinkedList()
f.add(10)
f.add(20)
f.add(30)
f.add(40)
f.add(50)
f.PList()
f.search_Node(40)
f.search_Node(80)

