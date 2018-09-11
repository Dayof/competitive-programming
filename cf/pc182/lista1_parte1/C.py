def get_diff(a, b):
	return abs(a-b)

n = int(input())
ai = list(map(int, input().split(' ')))
num = 0
for i in range(1, n):
	aux = get_diff(ai[i-1], ai[i])
	if aux > num:
		num = aux

print(num)
