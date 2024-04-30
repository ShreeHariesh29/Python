print("Temperature converter \nChoice the convertion Option 1 or 2")
print("Options \n1. Fahrenheit to Celcius \n2. Celcius to Fahrenheit")
option = int(input("Enter your option ="))
if(option == 1):
    fahrenheit = float(input("Fahrenheit = "))
    convertCelcius = (fahrenheit - 32)*5/9
    print("Celcius = ",convertCelcius)
elif(option == 2):
    celcius = float(input("Celcius = "))
    convertFahrenheit = (celcius*9/5)+32
    print("Fahrenheit = ",convertFahrenheit)
else:
    print("invalid option")