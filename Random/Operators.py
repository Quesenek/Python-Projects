
x = [i for i in range(1, 1000+1)]

outputList = []

for i in x:
    if(i % 3 == 0 and i % 5 == 0):
        outputList.append(f"FizzBuzz <{i}>")
    elif(i % 3 == 0):
        outputList.append(f"Fizz <{i}>")
    elif(i % 5 == 0):
        outputList.append(f"Buzz <{i}>")
    else:
        outputList.append(str(i))

print(outputList)