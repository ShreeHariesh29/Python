# Get any number from user and give the factorial value of that number
# Eg:
# user input = 5
# 5*4*3*2*1 = 120
# 120 is the Factorial value of 5

num = int(input("Enter any number to check the Factorial Value\n num ="))
sum=1
for i in range(num,0,-1):
    sum = sum*i
    print(i)
print(sum)

