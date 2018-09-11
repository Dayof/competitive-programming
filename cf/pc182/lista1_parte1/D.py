def fib(n, mat_fib):
	if n == 0 or n == 1:
		return n
	elif mat_fib[n]:
		return mat_fib[n]
	else:
		mat_fib[n] = fib(n-1, mat_fib)+fib(n-2, mat_fib)
		return mat_fib[n]

n = int(input())
print(fib(n, [0]*(n+1)))
