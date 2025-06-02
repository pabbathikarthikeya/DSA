def encript(message,key):
    res=""
    for char in message:
        if char.isalpha():
            if char.isupper():
                base=ord('A')
                shift=key%26
                res+=chr((ord(char)-base+shift)%26+base)
            else:
                base=ord('a')
                shift=key%26
                res+=chr((ord(char)-base+shift)%26+base)
    return res
def decript(res,key):
    return encript(res,-key)

mesaage="Hello World"
key=3
encripted=encript(mesaage,key)
decripted=decript(encripted,key)
print("Mesaage:",mesaage)
print('Encripted:',encripted)
print('Decripted:',decripted)