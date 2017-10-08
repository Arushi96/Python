#Assignment Questions       
#Q: Write a program, which prints the first 'N' numbers of fibonacci series.
def fib():
    n = int(input ("Enter the number till which you want to print fibonacci series: "))
    a=0
    b=1
    i=0
    sum1=0
    while i <=n-2:
        sum1=a+b
        a=b
        b=sum1
        #print(i)
        i = i+1
    print(sum1)
    
    
fib()
