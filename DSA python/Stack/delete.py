count=-1
def delete(l,element):
    global count
    if element == -1:
        return print("List is empty.")
    count-=1
    l.pop()
    return l

l=[]

x=delete(l, count)
print(x)
