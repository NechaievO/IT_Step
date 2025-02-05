# def clean_teeth(elektrichbrush, usualbrush):
#     print("Take a teeth-brush")
#     print("Press on brush a toothpaste")
#     print("Brush teeth")
#     print("Rinse with water")
#     print("Spit out!")
#
#     if electricbrush:
#         print("Take care and slowly")
#     if usualbrush:
#         print("Press stronger than usual")
#
#
# electricbrush = False
# usualbrush = True
#
# clean_teeth(electricbrush,usualbrush)
#
#
# def make_coffee(sugar, milk):
#     print("Вскипятить воду")
#     print("Положить кофе в чашку")
#     print("Залить кипятком")
#     if sugar:
#         print("Добавить сахар")
#     if milk:
#         print("Добавить молоко")
#     print("Перемешать")
#     print("Кофе готов!")
#
# # Вызов функции
# sugar=True    # Здесь мы говорим, что мы добавляем сахар
# milk=False    # Здесь мы говорим, что мы не добавляем молоко
# make_coffee(sugar, milk)
#
#
#
# # Определение констант
# PI = 3.14159
# GRAVITY = 9.8
# MAX_CONNECTIONS = 100
#
# # Использование констант в функциях и выражениях
# def calculate_circle_area(radius):
#     return PI * radius ** 2
#
# def calculate_free_fall_time(height):
#     return (2 * height / GRAVITY) ** 0.5
#
# print("Circle area with radius 5:", calculate_circle_area(5))
#
# print("Time to fall from height 20m:", calculate_free_fall_time(20))
#
# print("Maximum allowed connections:", MAX_CONNECTIONS)
#
#
#
# strings = ['apple', 'banana', 'cherry', 'date', 'orange']
#
# strings = {7: 'apple', 'key': 'banana', 3: 'cherry', 4: 'date', 5: 'orange'}
#
# # print(strings[7])
# print(strings['key'])
# strings['key'] = 'blueberry'
# print(strings['key'])
#
# fruits = ['apple', 'banana', 'cherry', 'date', 'orange']
#
# # Перебор элементов списка
# for fruit in fruits:
#     print(fruit)
#
# #Исходный словарь
# fruit_inventory = {10: 'apple', 'key': 'banana', 15: 'cherry', 5: 'date', 8: 'orange'}
#
# # Перебор элементов словаря
# for quantity, fruit in fruit_inventory.items():
#     print(f'There are {quantity} {fruit}s')
# print('==============')
# for fruit in fruit_inventory.values():
#     print(f'There are  {fruit}s')
#
#
#
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# # empty_dict = {}  # Пустой словарь
#
# print(person['name'])
# # del person['age']
# print(person.keys())
# print(person.values())
# print(person)


# with open("example_1.txt", "r") as file:
#     content = file.read()
#     print(content)

with open("example_1.txt_txt", "w") as file:
    file.write("Hello,")

with open("example_1.txt_txt", "a") as file:
    file.write("world!")


with open("example_1.txt_txt", "r+") as file:
    content = file.read()
    print(content)


def open_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content
print(open_file("example_1.txt"))
print(open_file("example_1.txt_txt"))


# - 'r' — чтение.
# - 'w' — запись.
# - 'a' — добавление.
# - '+' — чтение и запись.