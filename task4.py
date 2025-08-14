#Напиши функцию reverse_string(s), которая переворачивает строку задом наперёд.
s = input("Введите текст: ")
def reverse_string(s):
    return s[::-1]
print(reverse_string(s))
