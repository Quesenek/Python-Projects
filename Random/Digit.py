
x = int(input("Enter Number: "))

x1 = x % 10
x2 = x / 10

print(f"Original {x}, x%10 {x1}, x/10 {x2}")
x = str(x) + str(x1)
x = int(x)

x1 = x % 10
x2 = x / 10

print(f"Original {x}, x%10 {x1}, x/10 {x2}")