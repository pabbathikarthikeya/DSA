def totalcost(s):
    keypad = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    total=0
    previouskey=None
    #s="hello"
    for char in s:
        for key,value in keypad.items():
            if char in value:
                res=value.index(char)+1
                total+=res
                if previouskey==key:
                    total+=1
                previouskey=key
                break
    return total

s="hello"
print(totalcost(s))


