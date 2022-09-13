
numberEntered = int(input("Введите число: "))

result = 1
listAppears = list() 

for count in range(1, numberEntered + 1):
	result *= count
	listAppears.append(result)

print(listAppears)