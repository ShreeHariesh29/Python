num = int(input("Enter a number to get its fibonacci series = "))
a = 0
b = 1
if(num == 1):
    print(a)
else:
    print(a,end=" ")
    print(b,end=" ")
for x in range(2,num):
    c = a+b
    a = b
    b = c
    print(c,end=" ")