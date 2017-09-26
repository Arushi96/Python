#count down recursion
# def countdown(n):
#     #Base Case
#     if n==0:
#         print("done!")
#     #Recursive Case
#     else:
#         print(n)
#         countdown(n-1)
         
#print(countdown)- will print address of countdown
 
#countdown(10)
        
#sum of all integers nos using recursion
# def sum_int(n):
#     if n==0:
#          return 0
#     else:
#          a= n+sum_int(n-1)
#          #print(a) - for debugging
#          return a
#  
# print(sum_int(10))
#  
# #sum_int(3)- to be used while debugging

#factorial using recursions
# def fact(n):
#     if n==0:
#         return 1
#     else:
#          #print(n)
#         n=n*fact(n-1)
#         return n
#          
# print(fact(5))

#fibonacci series using recursions
# def fib(n):
#     if n==0 or n==1:
#         #print(n)
#         return n
#     else:
#         #print(n)
#         a=(fib(n-1)+fib(n-2))
#         #print(a)
#         return (a)
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print fib(i)
#      
# #print(fib(5))

#binary series using recursions
# def binary(n):
#     #l=input("Enter the length of the binary: ")
#  
#     if n<1:
#         return n
#     else:
#         a= binary(n//2) 
#         print n%2,
#      
# binary(5)





#fibonacci series using recursions
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         #print(n)
#         a=(fib(n-1)+fib(n-2))
#         print(a)
#         return (a)
    
    
# print(fib(4))


# def Print(n):
#     if n==0:
#         return 0
#     else:
#         print n
#         return Print(n-1)
#      
# print(Print(4))




# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print fibonacci(i)

#fibonacci without recursion
# def fib(n):
#     a=0
#     b=1
#     i=0
#     while i <= n-2:
#         print(i)
#         sum1=a+b
#         a=b
#         b=sum1
#         i = i+1
#     print(sum1)
#     
# print(fib(10))
#         
#     
# def binary(n):
#     if n < 2:
#         print (n)
#     else:
#         a=binary(n/2)
#         print(a)
#         print(n%2)
#         
# binary(4)

# def printbits(n, st=""):
#     if n==0:
#         print(st)
#         return 0
#     printbits(n-1, st+'0')
#     printbits(n-1, st+'1')
# 
# printbits(2)


# n =5
# for i in range(n):
#     print (int(i)*int(i))
