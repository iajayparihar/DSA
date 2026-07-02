# call bye value and refrence
# list, set, dictionary --> is pass by refrence
# lest all pass bye value 

# if we want to pass list as a value then use copy() method 
def check(x):
    print(x)
    # operation
    x.clear()
    print(x)

lit=[1,2,3,4,5]
st=set()
e={1,2,3,40,5,55}
st.update(e)

dic={1:'one',2:'two'}
check(dic)
print(dic)

# dictionary
# bool
# string

# list
# tuple
# set

