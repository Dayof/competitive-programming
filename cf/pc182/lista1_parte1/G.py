def equality(most_rich, A):
	total = 0
	for person in A:
		total += most_rich - person

	return total
n = int(input())
A = list(map(int, input().split(' ')))
print(equality(max(A), A))
