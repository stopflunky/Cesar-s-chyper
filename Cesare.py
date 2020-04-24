max_key = 26

def getMode():

    options = ["c", "d", "b"]

    print('''
            
            ************* Program to encrypt / decrypt *************
                    Warning this program uses Caesar's method

                            what do you want to do ? 

    - encrypt              ----> c 

    - decrypt            ----> d

    - decrypt brut-force ----> b


    Reply: ''')

    while True:

        mode = input().lower()

        if mode in options:

            return mode
        else:

            print('''You wrong!!
            
            - encrypt              ----> c 

            - decrypt            ----> d

            - decrypt brut-force ----> b

            Try again!
                ''')
        

def getMessage():
    print("Enter your message: ")
    return input()


def getKey():

    key = 0
    while True:

        print("Enter the key:  (1-26)" )
        key = int(input())
        if key >=1 and key <= max_key:
            return key


def getTranslatedMessage(mode, msg, key):

    transalted = ""
    if mode[0] == "d":
        key = -key

    for symbol in msg:

        if symbol.isalpha():

            num = ord(symbol)
            num += key 

            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26

            transalted += chr(num)

        else:
            transalted += symbol


    return transalted

mode = getMode()
msg = getMessage()

if mode[0] != "b":
    key = getKey()

if mode[0] != "b":
    print("Here is the modified text: ")
    print(getTranslatedMessage(mode, msg, key))

else:
    for key in range(1, max_key+1):
        print(key, getTranslatedMessage("d", msg, key))


