#Напиши функцию bool_to_word(b), которая возвращает 'True' если b=True, иначе 'False'.
b = input("Введите слово: ")
def bool_to_word(b):
    if b == "True":
        return True
    else:
        return False
print(bool_to_word(b))