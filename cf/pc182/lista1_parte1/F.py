def sum_elements(n, x, A, B):
	for i in range(n):
		for j in range(n):
			if A[i]+B[j] == x:
				return 1
	return 0

n, x = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
print(sum_elements(n, x, A, B))
