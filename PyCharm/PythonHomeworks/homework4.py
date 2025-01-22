dayweek = input("Please, enter number of the day of the week: ")

if dayweek.isdigit():
    dayweek = int(dayweek)
    if 1 <= dayweek <=7:

     if dayweek in [1]:
            print("Monday")
     elif dayweek in [2]:
            print("Tuesday")
     elif dayweek in [3]:
            print("Wednesday")
     elif dayweek in [4]:
            print("Thursday")
     elif dayweek in [5]:
            print("Friday")
     elif dayweek in [6]:
            print("Saturday")
     elif dayweek in [7]:
            print("Sunday")
    else: print ("Print number in the range from 1 to 7")




monthNumber = input("Please, enter number of month: ")
try:
    if monthNumber.isdigit():
        monthNumber = int(monthNumber)
        if 1 <= monthNumber <= 12:

            if monthNumber in [1]:
                print("January")
            elif monthNumber in [2]:
                print("February")
            elif monthNumber in [3]:
                print("March")
            elif monthNumber in [4]:
                print("April")
            elif monthNumber in [5]:
                print("May")
            elif monthNumber in [6]:
                print("June")
            elif monthNumber in [7]:
                print("July")
            elif monthNumber in [8]:
                print("August")
            elif monthNumber in [9]:
                print("September")
            elif monthNumber in [10]:
                print("October")
            elif monthNumber in [11]:
                print("November")
            elif monthNumber in [12]:
                print("December")
        else:
            print("Please, enter number in the range from 1 to 12")
    else:
            print("Please, enter a valid number")

except ValueError:
    print("Please, enter number in the range from 1 to 12")




digitEnter = input("Please, enter number: ")
try:
    digitEnter = float(digitEnter)
    print("=====")
    if digitEnter > 0:
        print("Number is positive.")
    elif digitEnter < 0:
        print("Number is negative.")

    else:print("Number is equal to zero.")

except ValueError:
    print("Please enter a valid number.")






enterDigit1 = input("Please, enter a first number: ")
enterDigit2 = input("Please, enter a second number: ")
if enterDigit1.isdigit() and enterDigit2.isdigit():

    enterDigit1 = int(enterDigit1)
    enterDigit2 = int(enterDigit2)
    if enterDigit1 == enterDigit2:
        print("Two entered numbers are equal.")
    elif enterDigit1 < enterDigit2:
        print(enterDigit2,  enterDigit1)

    else: print(enterDigit1,  enterDigit2)






user_input = input("Please, enter six-digit number: ")
while len(user_input) != 6 or not user_input.isdigit():
    print("It is a not six-digit number! Please, try again")
    user_input = input("Please, enter six-digit number: ")

first_part = str(user_input)[:3]
second_part = str(user_input)[3:]

sum_first = sum(int(digit) for digit in first_part)
sum_second = sum(int(digit) for digit in second_part)

if sum_first == sum_second:
        print("You have got a happy number!")
else:
        print("It is a not happy number :")






while True:
    first_number_input = input('Enter the first number: ')
    if first_number_input.isdigit():
        first_number = int(first_number_input)
        break
    else:
        print('Please enter a valid integer.')
while True:
    second_number_input = input('Enter the second number: ')
    if second_number_input.isdigit():
        second_number = int(second_number_input)
        break
    else:
        print('Please enter a valid integer.')

if first_number <= second_number:
    for number in range(first_number, second_number + 1):
        print(number)
if first_number > second_number:
    for number in range(first_number, second_number - 1, -1):
        print(number)

