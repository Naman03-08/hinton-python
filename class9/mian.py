# x = 10
# if(x>5):
#     print("big")
#     print("number")
# else:
#     print("small.number")
num = int(input())
if(num % 3 == 0 and (num % 5!=0)):
    print("fizz")
    
if(num % 5 == 0 and ( num % 3!=0)):
    print("buzz")  

if(num % 3 == 0 & num % 5 == 0):
    print("fizzbuzz")
    