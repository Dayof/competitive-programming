def get_max_idx(n, x, A):
	max_idx = -1
	for i in range(n):
		if A[i] >= x:
			max_idx = i+1
	return max_idx

n, x = list(map(int, input().split(' ')))
A = list(map(int, input().split(' ')))
print(get_max_idx(n, x ,A))
