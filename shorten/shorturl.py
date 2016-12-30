char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

def Shorten_encode(index):
    ans = ""
    global char
    # print(len(char))
    num1 = index//62
    num2 = index%62
    tag = 0
    while 1:
        # print("ans",ans,"num1",num1,"num2",num2)

        if num1 >62:
            if tag == 62:
                ans += "0"
                tag = 0
            else:
                tag+=1
            num1= num1//62
        else:
            print(char[num1-1],char[tag-1],char[num2-1])

            return char[num1-1] + char[tag-1]+ char[num2]



for i in range(200):
    print(Shorten_encode(i))
