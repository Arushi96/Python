#Assignment Questions
#Q: Write a program which calculates the summation of first N numbers except those which are divisible by 3 or 7.
n = int(input ("Enter the number till which you want to find summation: "))
s=0
i=0
while i<=n:
    if (i%3==0)or(i%7==0):
        #print(i)
        i+=1
        continue
    else:
        s=s+i
        i=i+1
print("sum is: ", s)

