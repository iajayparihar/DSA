# this class is called when we need new nodes
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

# this class is called when we what to create a new linked list
class LinkedList:
    def __init__(self,head=None):
        self.head=head

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
        while temp.next != None : 
            temp=temp.next
        temp.next=new

# insert node at the given postion 
    def insert_position(self,data,idx):
        new = Node(data)
        if idx > 0 :
            temp = self.head.next
            pre=self.head
            i=1  # this means i is pointing to the second node 
            while i < idx:
                temp = temp.next
                pre = pre.next
                i+=1
            new.next = temp  # new.next = pre.next
            pre.next = new
        else:
            print("Index is not valid !!!")
        
        # new = Node(data)
        # if idx > 0 :
        #     temp = self.head.next
        #     pre=self.head
        #     i=1  # this means i is pointing to the second node 
        #     while i < idx:
        #         temp = temp.next
        #         pre = pre.next
        #         i+=1
        #     new.next = temp
        #     pre.next = new
        # else:
        #     print("Index is not valid !!!")


f=LinkedList()
f.add(10)
f.add(20)
f.add(30)
f.add(40)
# f.insert(5)
f.insert_last(50)
f.insert_position(6666,2)
f.PList()

















