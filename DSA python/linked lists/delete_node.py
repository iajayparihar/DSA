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
            new.next = temp
            pre.next = new
        else:
            print("Index is not valid !!!")

#--------------------Node-deleting-part---------------------------------------------

# deleting the first node of the linked list
    def First_del(self):
        temp = self.head
        self.head = self.head.next
        temp=None
# deleting the last node of the linked list
    def last_del(self):
        temp = self.head
        while temp.next != None:
            pre = temp # previous pointer bye temp then temp incresed 
            temp = temp.next
        pre.next = temp.next # pre.next = None
    #--------- other way for 2 pointer's
        # temp=self.head.next
        # pre = self.head
        # while temp.next != None :   #     while temp :
        #     temp=temp.next
        #     pre = pre.next
        # pre.next= None
#-----------------------------------------------------------------------------
# delete node by value 
# we can't delete first element with this !!!
    def del_by_value(self,val) :
        temp = self.head
        found=False
        while temp:
            if temp.data == val :
                print("we found")
                found=True
                break
            else :
                pre = temp # previous pointer bye temp then temp incresed 
                temp = temp.next
        if found == True:
            pre.next = temp.next
            temp.next=None
        else:
            print("we cant not found the value in this linked list")
# "-----------------------------------------"
        # temp = self.head.next
        # pre = self.head
        # while temp:
        #     if temp.data == val :
        #         print("we found the element")
        #         break
        #     else:
        #         temp = temp.next
        #         pre = pre.next
        # pre.next=temp.next
        # temp.next =None

f=LinkedList()
f.add(10)
f.add(20)
f.add(30)
f.add(40)
f.add(50)
f.add(60)
f.PList()
f.del_by_value(20)
f.PList()

















