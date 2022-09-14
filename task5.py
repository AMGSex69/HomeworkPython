import random
newList = list(random.randint(-100, 100) for _ in range(20))
print(newList)
random.shuffle(newList)
print(newList)