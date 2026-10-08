#Q) print the sum of all the number which are in input 
# n = int(input())
# a = n
# s = 0
# while(n > 0):
#     x = n%10
#     s = s*10 +x
#     n = n//10
# if(s == a):
#     print("palindrome")
# else:
#     print("Not Palindrome")

# Q2) 

# n = int(input())
# c=0
# s=0
# while(n>0):
#     c+=1
#     n=n//10
# while(n>0):
#     x=n%10
#     s=s+(x**c)
#     n=n//10
# if(n==s):
#     print("yes")
# else:
#     print("no")
    
    
n = int(input())
a=n
x=0
s=0
while(n>0):
    k=n%10
    if k==0 :
     continue
    s=s*10+k
    n=n//10
while(a>0):
    k1=a%10
    x=x*10+k1
    a=a//10
print(x)