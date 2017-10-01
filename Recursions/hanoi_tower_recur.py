#def movement(source,desti):
#	print("move from " + str(source) + "move to " +str (desti))


#def towers(n, source,desti, extra):
#	if n==1:
#		print(movement(source,desti))
#	else:
#		towers(n-1, source, extra, desti)
#		towers(1, source,desti, extra)
#		towers(n-1, extra,source,desti)

#movement(1,3)
#towers(6,1,3,2)


def hanoi (n, start=1, aux=2, end=3):
	if n:
		hanoi(n-1, start,end,aux)
		print("Move disk %d from %d to %d."%(n,start,end))
		hanoi(n-1, aux,start,end)
		

hanoi(3)

