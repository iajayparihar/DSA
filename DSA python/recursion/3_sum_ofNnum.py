#paramer
def add(i,sum=0):
    if i<1:
        print("The sum is :- ",sum)
        return
    add(i-1,sum+i)

# add(3)


# Funtional call return somthing always

def Add(num):
    if num == 0 :
        return 0
    return num + Add(num-1)

print("The sum is :-",Add(5))


