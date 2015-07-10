ans=0
l=1
def isPrime(a):
	for j in range(2,a):
		if (a%j)==0:
			return False
	return True
b=1001
if (b%2)==0:
		ans = 2
for i in range(3,b+1,2):
	if isPrime(i):
		if (b%i)==0:
			ans =i
			l=l*i
		if l == b:
			break

print ans