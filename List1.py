num = int(input("Enter the first number = "))
num2 = int(input("Enter the first number = "))
num_factors = []
num2_factors =[]
for x in range(1,num+1):
    if num%x == 0:
        num_factors.append(x)
for x in range(1,num2+1):
    if num2%x == 0:
        num2_factors.append(x)
