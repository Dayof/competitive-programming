def no3(a,b,c):
	return not any(filter(lambda x:x%3==0, [a,b,c]))

def solution(a,b,c,n):
	not_div = True
	add = 1
	while True:
		if no3(a,b,c):
			break
		if c%3==0:
			a,b = a+add, b+add
			c -= (2*add)
			if no3(a,b,c):
				break
		if a%3==0:
			a,b = a-(2*add), b-(2*add)
			c += (4*add)
			if no3(a,b,c):
				break

	return a,b,c


n = int(input())
div = int(n/3)
rest = n%3
r = [div, div, div+rest]
r = solution(r[0], r[1], r[2], n)
print(f'{r[0]} {r[1]} {r[2]}')

