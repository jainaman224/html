def isPrime(a):
	for j in range(3,(a/math.sqrt(a))+1,2):
		if (a%j)==0:
			return False
	return True
import math
ans=24465663438
for i in range(800001,2000000,2):
	if isPrime(i):
		ans = ans+i
print ans