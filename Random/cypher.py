import string
def cipher_maker(message):
    oldMessage = cipher(message)
    newMessage = ""

    for x, i in enumerate(charCase(message)):
        if(i):
            newMessage += oldMessage[x].upper()
        else:
            newMessage += oldMessage[x]

    return newMessage

def cipher(message):
    message = message.lower()
    list = [i for i in string.ascii_lowercase]
    str1 = ""
    str2 = ""

    for i in list:
        str1 += i
    for i in reversed(list):
        str2 += i
    return message.translate(str.maketrans(str1, str2))



def charCase(message):
    
    caseList = []

    for i in message:
        caseList.append(i.isupper())
    return caseList

originalMessage = cipher_maker("thIs is a seCret messaGe")

for i in range(1):
    print(originalMessage)
    originalMessage = cipher_maker(originalMessage)