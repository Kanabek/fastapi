#Напиши две функции: find_max(lst) — возвращает максимум, find_min(lst) — возвращает минимум.
numbers = input("Введите числа через пробел: ")
numbers = list(map(int, numbers.split()))
def find_max(numbers):
    return max(numbers)
def find_min(numbers):
    return min(numbers)
print(find_max(numbers))
print(find_min(numbers))