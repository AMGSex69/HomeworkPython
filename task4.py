from hashlib import new
import random
listNumber = int(input("Введите колличество элементов в списке: "))
position1, position2 = map(int, input("Введите позицию через пробел: ").split())
newList = list(random.randint(-listNumber, listNumber) for _ in range(listNumber))
print(newList[position1 - 1], '\n', newList[position2 - 1], '\n', newList[position1 - 1] * newList[position2 - 1])












