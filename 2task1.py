#Напиши функцию count_digits(n, d), которая считает, сколько раз цифра d встречается в квадрате всех чисел от 0 до n включительно.
n = int(input("Введите число n: "))
d = input("Введите цифру d: ")
def count_digits(n, d):
    count = 0
    for i in range (n + 1):
        sqr = i ** 2
        count += str(sqr).count(d)
    return count
print(count_digits(n, d))



