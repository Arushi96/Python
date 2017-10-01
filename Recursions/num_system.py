def new_sys(n, st=""):
	if n==0:
		print(st)
		return 0
	new_sys(n-1, st + " " + 'alpha')
	new_sys(n-1, st + " " + 'beta')
	new_sys(n-1, st + " " + 'omega')
	new_sys(n-1, st + " " + 'gamma')

n=input("Enter the num: ")
new_sys(n)
#new_sys(2)
