#Task 1

num = input("Please, enter a number: ")

try:
    num = int(num)
    print(num)
except ValueError:
    print("Error: Enter a valid number")

finally: print("Please, try again :)")


#Task 2

file_name = input("Please, enter a name of file for reading: ")

try:
    with open("file_name" "r") as file:
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")


#Task 3

user_string = str(input("Please, input some information: "))

try:
    number = int(user_string)
    print(f"number is: {number}")

except ValueError:
    print("Error: The input cannot be converted to valid integer.")


#Task 4

import math
user_number = int(input("Please, enter a number: "))

try:
    square_root = math.sqrt(user_number)
    print(square_root)

except ValueError:
    print("Error: Impossible to take square root of a negative number! ")


#Task 5

user_input = input("Please, enter a string of numbers separated by comma (for example, '1,2,3,4,5'): ")

try:

    numbers_str = user_input.split(",")


    numbers = [int(num.strip()) for num in numbers_str]

    print("List of numbers:", numbers)
except ValueError:
    print("Error: Is allowed only string of integers separated by commas!")


#Task 6
import json

user_json_file = input("Please, enter a name of json file: ")

try:
   with open("user_json_file", "r") as file:
    data = json.loads(user_json_file)
   print(data)

except FileNotFoundError:
    print("Error: File not found!")
except json.JSONDecodeError as e:
    print(f"Error: wrong decoding of JSON: {e}")











