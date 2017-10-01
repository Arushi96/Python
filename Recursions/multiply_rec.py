def multiply(a,b):
	m=0
	if b == 1:
		print a
		return a
	else:
		m=a+ multiply(a,b-1)
		print m
		return m

multiply(6,3)

