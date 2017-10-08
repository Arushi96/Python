#Assignment Questions
# Q:Write a program which calculates the summation of first N odd numbers.
a = int(input ("Enter the number till which you want to find summation of odd numbers: "))
i=1
s=0
while i <= a:
    if i%2==1:   # or if i%2!=0:
        #s = s + i
        s+=i
    i = i + 1

print("Sum is ", s)

