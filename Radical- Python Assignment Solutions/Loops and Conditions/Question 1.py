#Assignment Questions
#Q: Write a program which would calculate the addition of first N even numbers.
a = int(input ("Enter the number till which you want to find summation of even numbers: "))   
i=1
s=0
while i <= a:
    if i%2==0: 
        s+=i   #s = s + i
    i = i + 1
 
print("Sum is ", s)
    
