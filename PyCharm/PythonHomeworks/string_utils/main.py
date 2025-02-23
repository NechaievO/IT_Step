from string_utils import string_operations, string_analysis

user_input = input("Enter some words: ")

# Используем функции из модулей
reversed_str = string_operations.reverse_string(user_input)
capitalized_str = string_operations.capitalize_words(user_input)
vowel_count = string_analysis.count_vowels(user_input)
char_count = string_analysis.count_char(user_input)

# Вывод результатов
print(f"Reversed string: {reversed_str}")
print(f"Capital letter: {capitalized_str}")
print(f"Vowels number: {vowel_count}")
print(f"Total number of caracters: {char_count}")
