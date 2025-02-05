

def is_number(value):
    try:

        float(value)
        return True
    except ValueError:

        return False

def main():

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")


    if is_number(num1) and is_number(num2):

        num1 = float(num1)
        num2 = float(num2)
        result1 = num1 * num2
        result2 = num1 / num2
        result3 = num1 + num2
        result4 = num1 - num2
        print(f"The sum after multiplication of {num1} on {num2} is: {result1}")
        print(f"The sum after division of {num1} on {num2} is: {result2}")
        print(f"The sum after addition of {num1} to {num2} is: {result3}")
        print(f"The sum after subtraction from {num1} a {num2} is {result4}")
    else:
        print("Invalid input. Please enter valid numbers.")


main()










