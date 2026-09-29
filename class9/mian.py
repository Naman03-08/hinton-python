# x = 10
# if(x>5):
#     print("big")
#     print("number")
# else:
#     print("small.number")
# num = int(input())
# if(num % 3 == 0 and (num % 5!=0)):
#     print("fizz")
    
# if(num % 5 == 0 and ( num % 3!=0)):
#     print("buzz")  

# if(num % 3 == 0 & num % 5 == 0):
#     print("fizzbuzz")
  
  
# num = int(input())
# if(num >= 12):
#     print(num+7)
# elif(num >= 10):
#     print(num+5)
    
# print(num)
# marks = int(input())
# if (marks >= 90):
#     print("You Got A Grade ")
# elif(marks >= 80):
#     print("You Got B Grade")
# elif(marks >= 70):
#     print("You Got C Grade")
# elif(marks >= 60):
#     print("You Got D Grade")
# elif(marks >= 50):
#     print("You Got E Grade")
# else:
#     print("You Got F Grade")

# age = int(input())
# if(age>= 18):
#     print("you can vote")
# else:
#     print("nothing")

year = int(input())
if(year % 4 == 0 and not(year % 100 == 0) or (year % 400 == 0)):
    print("leap year")
else:
    print("not a leap year")