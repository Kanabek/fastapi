#Напиши функцию even_or_odd(number), которая возвращает 'Even' если число чётное и 'Odd' если нечётное.
number = int(input("Введите число: "))
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(number))