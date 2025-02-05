


def greet(name = "Guest"):
    print(f"Hello, {name}!")

greet("Alice")
greet("Mike")
greet()

print("========")
print("========")



def add(a,b):
    return a + b

result = add(3, 5)
print(result)

print("========")
print("========")




def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(3))

print("========")
print("========")
#
#
#
#
def print_numbers(start_number, end_number):

    if start_number <= end_number:
        for print_numbers in range(start_number, end_number + 1):
            print(print_numbers)

    else:
        for print_numbers in range(start_number, end_number - 1, -1):
            print(print_numbers)


print_numbers(7, 3)
print("-------------------")
print_numbers(3, 7)

print("========")
print("========")
#
#
#
#
def calculate(first_number, second_number, operation):

    if operation == "+":
        return first_number + second_number

    if operation == "-":
        return first_number - second_number

    if operation == "/":
        return first_number / second_number

    if  operation == "*":
        return first_number * second_number

    else: return "Unsupported operation"


print(calculate(5, 3, "+" ))
print(calculate(0, 2, "/" ))
print(calculate(7, 15, "-" ))
print(calculate(25, 11, "*" ))
print(calculate(14, 9, "&" ))

print("========")
print("========")





def name_greet(name):
    return(f"Hello, {name}!")

names = ["Alice", "Bob", "Michael", "Tracy", "Judith"]
for name in names:
     print(name_greet(name))

print("========")
print("========")



def even_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if num % 2 == 0]

result = even_numbers_in_range(1, 10)
print(result)

print("========")
print("========")



def factorial(n):
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))
print(factorial(3))
print(factorial(1))
print(factorial(0))

print("========")
print("========")



def reverse_string():
    n = "hello"
    return n[:: -1]

print(reverse_string())

print("========")
print("========")



def sum_list():
    numbers = [1, 2, 3, 4, 5]
    return sum(numbers)

print(sum_list())



