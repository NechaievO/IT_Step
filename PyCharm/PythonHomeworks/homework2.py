input_year = int(input("Input a year:" ,  ))
n = input_year
i = 400
f = 4
x = 100
if (n % i == 0) or (n % 4 == 0) and (n % 100 != 0):
    print("It is a leap year")
else :
    print("It is a non-leap year")


