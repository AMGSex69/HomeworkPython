# numbersAmount = int(input("Задайте длину списка: "))

# result = 0

# for k in range(1, numbersAmount+1):
# 	result += (1 + 1 / k) ** k

# print(result)

numbersAmount = int(input("Задайте длину списка: "))
result = [0] * numbersAmount

for k in range(1, numbersAmount +1):
	result[k -  1]= (1 + 1 / k) ** k

print(sum(result))
	
	