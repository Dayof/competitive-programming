def total_hours(n, k):
	res = n-k+1
	idx = n
	while res > 0:
		idx += 1
		res = res-k+1
	return idx

n, k = list(map(int, input().split(' ')))
print(total_hours(n, k))
