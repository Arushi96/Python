#Assignment Questions
# Q: Similar to above Q8, WAP to print the below patterns:
#*
#**
#***
#****
#*****
#*****
#****
#***
#**
#*
#    *
#   **
#  ***
# ****
#*****
#*****
# ****
#  ***
#   **
#    *
for i in range (1,6,1):
    print("*"*i)
for j in range (5,0,-1):
    print("*"*j)

for i in range (1,6,1):
    a=("*"*i)
    print(a.rjust(5))
for j in range (5,0,-1):
    b=("*"*j)
    print(b.rjust(5))
