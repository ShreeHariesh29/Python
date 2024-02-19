x = int(input("x = "))
y = int(input("y= "))
z = int(input("z = "))


def maxnum(x, y, z):
    if x > y and x > z:
        return "x is greater: " + str(x)
    elif y > x and y > z:
        return "y is greater: " + str(y)
    else:
        return "z is greater: " + str(z)



print(maxnum(x, y, z))