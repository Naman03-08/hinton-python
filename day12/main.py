# a = int(input())
# b = int(input())

# gcd = 1
# i = 1
# while i <= min(a, b):
#     if(a % i == 0) and (b % i == 0):
#         gcd = i
#     i += 1
# print(gcd)

a = int(input())
b = int(input())
n = 0
c = int(input())
d = int(input())
count = 0
while (n <= d):
    if(n % a == 0)or(n % b == 0)or(n % c == 0):
        count += 1
    n += 1
    
print(count)