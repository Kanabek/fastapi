#Напиши функцию remove_char(s), которая удаляет первый и последний символ строки s.
s = input("Введите текст: ")
def remove_char(s):
    return s[1:-1]
print(remove_char(s))