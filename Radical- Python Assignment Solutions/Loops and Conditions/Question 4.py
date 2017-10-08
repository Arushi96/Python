#Assignment Questions
#Q: Write a program which calculates the summation of first N numbers except those which are divisible by 3 or 7, and are odd numbers.
n= int(input("Enter the nos till which you want to find summation: "))
s=0
i=0
while i<=n:
    if (i%3==0) or (i%7==0) or (i%2==1):
        #print(i)
        i+=1
        continue
    else:
       #print(i)
	s=s+i
        i+=1
print("sum is: ", s)
