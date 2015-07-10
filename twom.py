def isPrime(a):
	for j in range(3,a/2,2):
		if (a%j)==0:
			return False
	return True

ans=2
b=20000
for i in range(3,b+1,2):
	if isPrime(i):
		ans = ans + i

print ans