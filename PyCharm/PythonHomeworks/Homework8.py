import json

# Sample data
students = [
    {"name": "John Doe", "age": 20, "grades": [88, 75, 92]},
    {"name": "Jane Smith", "age": 22, "grades": [91, 85, 78]},
    {"name": "Michael Jones", "age": 23, "grades": [89, 79, 93]},
    {"name": "Julie Burns", "age": 21, "grades": [94, 83, 85]},
]

with open("students.json", "w" ) as file:
    json.dump(students, file,  indent=4)

print("JSON file created successfully!")


with open("students.json", "r",) as file:
    students = json.load(file)
    for student in students:
        name = student["name"]
        grades = student["grades"]
        avg_grade = sum(grades) / len(grades)
        print(f"{name}: {avg_grade:.2f}")






