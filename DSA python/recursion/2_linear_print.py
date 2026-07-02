# reverse liner print
def Rliner(i,num):
    if i==num:
        return 
    print(num)
    return Rliner(i, num-1)

Rliner(0, 10)


# liner print

# def liner(i,num):
#     if i==num:
#         return 
#     print(i)
#     return liner(i+1, num)

# liner(1, 11)