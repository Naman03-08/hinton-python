n = int(input())

if n < 2:
    print("not prime")
else:
    i = 2
    is_prime = True
    
while(i < 2):
    if(n % i == 0):
        is_prime = False
        break;
i += 1

if(is_prime):
    print("prime")
else:
    print("not prime")
    