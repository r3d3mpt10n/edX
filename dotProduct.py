def dotProduct(listA, listB):
	i = 0
	result = 0
	while i < len(listA) and len(listB):
		result += listA[i] * listB[i]
		i += 1
	return(result)
		



listA = [1,2,3]
listB = [4,5,6]

print(dotProduct(listA,listB))
