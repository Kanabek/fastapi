#Напиши функцию sum_array(arr), которая возвращает сумму всех элементов списка arr. Если список пустой — вернуть 0.
import array

numbers = input("Введите числа через пробел: ")
numbers = list(map(int, numbers.split()))
arr = array.array("i", numbers)

print("Массив:", arr)

def sum_array(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
result = sum_array(arr)
print(result)