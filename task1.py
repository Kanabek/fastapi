#Напиши функцию two_fer(name), которая возвращает строку: 'One for <name>, one for me.' Если имя не передано — подставить 'you'.

name = input("Введите имя (или оставьте пустым): ").strip()
def two_fer(name: str = "you"):
    return f"One for {name}, one for me."
if name == "":
    print(two_fer())
else:
    print(two_fer(name))