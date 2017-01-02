char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

def Shorten_encode(index):
    ans = ""
    global char

    if index == 0:
        return ""
    if index<=62:
        return char[index-1]

    if index%62 == 0:
        print("1",index//63)
        return Shorten_encode(index//63)+"0"
    print("2",index//62)
    return Shorten_encode(index//62) + Shorten_encode(index%62)






def Shorten_decode(s):
    global char
    ans = 0
    length= len(s)
    for i in s:
        if length != 1:
            ans += (char.index(i)+1)*62**(length-1)
            length -= 1
        else:
            ans+=(char.index(i)+1)
    return ans



# for i in range(200):
#     print(Shorten_encode(i))
'''
for i in range(100000):
    a = Shorten_encode(i)
    b = Shorten_decode(a)
    if b == i:
        print(i,"good")
    else:
        print(i,a,b)
        break
print(Shorten_encode(1))
Shorten_decode('')
'''

print(Shorten_encode(3968))
