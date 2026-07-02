def palendrom(i,s):
    r= len(s)-i-1
    
    if i>= len(s)/2:
        return True
    
    if s[i] != s[r]:
        return False
    
    return palendrom(i+1, s)

string="iitii"
a=palendrom(0, string)
if a:
    print("The string is palendrome.")
else:
    print("Not palendrome")