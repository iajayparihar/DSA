class Node:
    def __init__(self, data, add=None):
        self.data = data
        self.next = add


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        else:
            print('None')

    def deleteLast(self):
        prev = 0
        cur = self.head
        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None

    def deleteFirst(self):
        temp = self.head
        self.head = self.head.next
        temp.next = None

    def deletePos(self,pos):
        prev=0
        cur=self.head
        for _ in range(pos):
            prev=cur
            cur=cur.next
        temp=cur.next
        prev.next=temp
        cur.next=None

l = Linkedlist()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
l.display()
l.deletePos(3) # by indexing
l.display()