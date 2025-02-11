try:

        num1 = int(input("Please, enter first number: "))
        num2 = int(input("Please, enter second number: "))
        division_result = num1 / num2
        print(division_result)


except ValueError:
                print('Error: only digit input is valid!')
except ZeroDivisionError:
                print('Error: division by zero is invalid!')
print("=" * 30)






try:
        with open("data.txt", 'r') as file:
                content = file.read()
                print(content)


except FileNotFoundError:
        print("File not found!")
finally:
        print("Anyway you may try again")

        print("=" * 30)





try:

        num1 = int(input("Please, enter first number: "))
        num2 = int(input("Please, enter second number: "))
        math_operation = str(input("Please, enter one of the next four mathematical operations: +, -, *, /:   "))

        if math_operation == "+":
                print(f"The result of {num1} + {num2} is: {num1 + num2}")
        elif math_operation == "-":
                print(f"The result of {num1} - {num2} is: {num1 - num2}")
        elif math_operation == "*":
                print(f"The result of {num1} * {num2} is: {num1 * num2}")
        elif math_operation == "/":
                print(f"The result of {num1} / {num2} is: {num1 / num2}")
        else:
         print("Error: Invalid operation! Please enter one of the following: +, -, *, /.")

except ValueError:
    print("Error: Please enter valid integers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    print("=" * 30)






try:
    number = int(input("Please, enter a number: "))
    print(number)

except ValueError as e:

    print(f"Error: {e}")
