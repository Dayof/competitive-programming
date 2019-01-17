def power_set(arr):
	ps, all_ps = set(), set()
	for i in range(2**len(arr)):
		ss = tuple([x for j, x in enumerate(arr) if (i >> j) & 1])
		if len(ss)>0:
			if len(ss)<3:
				if len(ss) == 1:
					ps.add((ss[0],0))
				else:
					ps.add(ss)
			else:
				all_ps.add(ss)
	return ps, all_ps

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
	for i in range(1, len(arr)):
		res = gcd(res, arr[i])
	return res

def rm_int(two_pos, all_pos, big_gcd, arr, n, max_n):
	max_gcd = big_gcd
	comb = arr
	res = [[0]*(max_n+1)]*(max_n+1)
	ms, bgcs, mg = n, 0, 0
	print(big_gcd)
	print(two_pos)
	for a in two_pos:
		new_gcd = all(a)
		if new_gcd > max_gcd:
			if n-len(a) < ms and new_gcd >= bgcs:
				ms, mg = n-len(a), new_gcd
		res[a[0]][a[1]] = new_gcd
		print(a, res[a[0]][a[1]])

	last_min, last_big = ms, mg
	for a in all_pos:
		new_a = list(a)
		new_a.sort()
		#print('outer', new_a, n-len(a), res[new_a[0]][new_a[1]])
		if res[new_a[0]][new_a[1]] > last_big and n-len(a) < last_min:
			print('inner', a, n-len(a))
			last_min = n-len(a)
	return last_min if last_min != 0 else -1

n = int(input())
arr = list(map(int, input().split(' ')))
big_gcd = all(arr)
two_pos, all_pos = power_set(arr)
print(rm_int(two_pos, all_pos, big_gcd, arr, n, max(arr)))
