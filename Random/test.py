import math
prompt = "This app can calculate the volume of several 3D shapes."
prompt += "\nYour options are cube, sphere, cylinder, or cone."
prompt += "\nWhich shape's volume would you like to calculate first?"

user = input(prompt)

def input_check(user):
    valid = ("cube", "sphere", "cylinder", "cone")
    while user not in valid:
        user = input("Please enter cube, sphere, cylinder, or cone!")
        if(user.lower() in valid):
            print(f"You chose a {valid[valid.index(user.lower())]}!")
            return(user.lower())
    return user.lower()

print(input_check(user))
print(math.pi)
print(math.pow(3, 3))