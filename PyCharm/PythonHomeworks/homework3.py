

user_number = input ("Enter two-digit number: ")
if user_number.isdigit() and len(user_number) ==2 :
    print(user_number[0])
    print(user_number[1])
else:  print("Invalid input! Please enter a two-digit number.")




user_number = input("Enter three-digit number: ")
if user_number.isdigit and len(user_number) == 3:
    print(user_number[0])
    print(user_number[1])
    print(user_number[2])

    sum_of_digits = int(user_number[0]) + int(user_number[1]) + int(user_number[2])
    print(sum_of_digits)
else:
    print("Invalid input! Please enter a three-digit number.")




user_number1 = input("Enter first digit: ")
user_number2 = input("Enter second digit: ")
if user_number1.isdigit() and user_number2.isdigit():

     print (user_number1 + user_number2)
else:
     print ("Please, enter digits")





user_temperature_Celsius = input("Enter temperature in Celsius: ")
num = float(user_temperature_Celsius)
temperature_Farenheit = (num * 9 / 5 + 32 )
print("Temperature in Farenheit:", temperature_Farenheit)




