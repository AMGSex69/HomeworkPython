enteredNumber = input("Введите число: ")
result = 0

for counter in enteredNumber:
	if (counter.isdigit()):
		result += int(counter)
	else:
		pass
	
print(result)