
def insert(Stk,item,size,top):
    if(top==size-1):
        print("Stack is OverFlow")
        return 
    top+=1
    Stk[top]=item
    return

Stk=[23,34,5,34,78,0]
size=len(Stk)+2
top=4
item=10
insert(Stk, item, size, top)
print(Stk)