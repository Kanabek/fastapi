#Напиши функцию area_or_perimeter(l, w), которая возвращает площадь если l == w, иначе периметр.
l = int(input("Введите целое значение длины 4 угольника: "))
w = int(input("Введите целое значение ширины 4 угольника: "))
def area_or_perimetr(l, w):
    if l == w:
        return l * w
    else:
        return (l + w) * 2
print(area_or_perimetr(l, w))