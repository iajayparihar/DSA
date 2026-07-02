# def insert(arr,data):
#     last = len(l)
#     l.append(data)
#     return l
# l=[5,6,7,8]
# x=insert(l, 10)
# x=insert(l, 12)
# print(x)

count=-1

def insert(l,data):
    global count
    count+=1
    l.append(data)
    return l

def delete(l):
    global count
    if count == -1:
        return print("List is empty.")
    count-=1
    l.pop()
    return l


l=[]
x=insert(l,10)
x=insert(l,20)
x=insert(l,30)
x=insert(l,40)
print(x)

d= delete(l)
d= delete(l)
print(d)
print(count)