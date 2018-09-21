def power_set(arr):
	ps = set()
	for i in range(2**len(arr)):
		ss = tuple([x for j, x in enumerate(arr) if (i >> j) & 1])
		if len(ss)>1:
			ps.add(ss)
	return ps

def gcd(a, b):
	if a == 0:
		return b
	elif b == 0:
		return a
	while a!=b:
            if a > b:
                a -= b
            else:
                b -= a
	return a

def all(arr):
        res = arr[0]
        for i in range(1, len(arr)-1):
                res = gcd(res, arr[i])
        return res

def rm_int(all_pos, big_gcd, arr, n):
	max_gcd = big_gcd
	comb = arr
	res = []
	for a in all_pos:
		new_gcd = all(a)
		if new_gcd > max_gcd:
			res.append(n-len(a))
	return res

def calc(all_pos, big_gcd, arr, n):
	ret = rm_int(all_pos, big_gcd, arr, n)
	if not ret:
		return -1
	else:
        	return min(ret)



n = int(input())
arr = list(map(int, input().split(' ')))
big_gcd = all(arr)
all_pos = power_set(arr)
ret = calc(all_pos, big_gcd, arr, n)

print(ret)
