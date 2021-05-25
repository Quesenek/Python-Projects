x = 1.0
x1 = f"Subtraction: {x} "

while x > 0:
    x -= 0.25
    x = float('%.2f' % x)
    x1 += f"{x} "
x1 += " Addition: 0.0 "
while x < 1:
    x += 0.25
    x = float('%.2f' % x)
    x1 += f"{x} "

print(x1)