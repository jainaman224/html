small=0
for i in range(80,500000000,80):
	for j in range(11,20):
		if (i%j)==0:
			x=True
		else :
			x=False
			break
	if x:
		small=i
		break

print small
			
