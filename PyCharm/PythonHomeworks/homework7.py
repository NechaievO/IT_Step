with open("data.txt", "r") as file:
    content = file.read()
    print(content)


    print("==========")
    print("=========")



with open("output.txt", "w") as file:
    file.write("New file 'output.txt' is created\n")
    file.write("It works fabulously!\n")
    file.write("It does show how Python is great!\n")


with open("output.txt", "r") as file:
    content = file.read()
    print(content)
    print("File is created and has some data\n")


    print("=========")
    print("=========")


with open("output.txt", "a") as file:
    file.write("...and incredibly easy!\n")


with open("output.txt", "r") as file:
    content = file.read()
    print(content)


if "...and incredibly easy!" in content:
    print("Data have been successfully added to the file 'output.txt'\n")
else:
    print("Sorry, but data were not added\n")


print("=========")
print("=========")
print("=========")



with open("output.txt", "r+")as file:
    content = file.read()
    print(content)
    file.seek(0, 2)
    file.write("We are adding a new string!\n")
    file.write("File is successfully updated!\n")


print("=========")
print("=========")
print("+++++++++")


with open("output.txt", "r")as file:
    content = file.read()
    print(content)