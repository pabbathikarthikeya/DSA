def asciiconversion(s):
    n=len(s)
    res=0
    for i,char in enumerate(s):
        ascival=ord(char)
        pos=10**(n-i-1)
        res+=ascival*pos
    return res

s="ABCD"
print(asciiconversion(s))