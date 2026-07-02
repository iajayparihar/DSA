front = -1
rear =  -1

def insert(Queue,data):
    global rear,front
    if front ==-1: # first insert
        Queue.append(data)
        front+=1
        rear+=1
        return
    Queue.append(data)
    rear+=1
    return print(Queue)

def delete(Queue):
    global front , rear
    if front == rear :
        print("Queue is Empty. ")
        front=-1
        rear=-1
        return
    Queue.pop(front)
    front+=1
    return print(Queue)

q = []
insert(q,10)
insert(q,20)
insert(q,30)
insert(q,40)
insert(q,50)
print(front,rear)

delete(q)
print(front,rear)
delete(q)
print(front,rear)
delete(q)
print(front,rear)
# print(d)

