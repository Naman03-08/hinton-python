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

# year = int(input())
# if(year % 4 == 0 and not(year % 100 == 0) or (year % 400 == 0)):
#     print("leap year")
# else:
#     print("not a leap year")
    
# year = int(input())
# if(year % 4 == 0):
#     print("Leap")
# elif((year % 4 ==0) and (year % 100 != 0 or year % 400 ==0 )):
#     print("Not Leap")

# a, b, c, d = map(str ,input().split())
# c = int(c)
# d = float(d)
# multiply = c*d
# print(b, multiply.round(multiply, 2))

# name = "python"
# x = name[::-1]
# print(x)

# Q.no - 26 {python}

# amount = int(input())

# if (amount > 1000):
#     print("congrats!!! you got a discount of 10%, and your final amount is:",(amount - (amount/10)))
# else:
#     print("there is no discount and your final price is: ",amount)
    
    
# Q.no - 27 {pythoon}
# n = int(input())
# if( n >= 150 - 150//10):
#     print("merit Scholarship awarded")
# else:
#     print("Nothing")
    

    
    
# Q.no - 28 {python}

# scoreA, scoreB, scoreC = map(int, input().split())
# if((scoreA + scoreB + scoreB)/3 > 80):
#     print("Distinction Awarded")
# elif((scoreA < 60) and (scoreB < 60) and (scoreC < 60)):
#     print("Nothing")
# elif((scoreA + scoreB + scoreC)/3 < 80):
#     print("Nothing")

# Q.no - 29 {python}
# 
# number = int(input())
# if(number % 2 == 0):
#     print("Even")
# else:
#     print("Odd")


#Q.no - 30 {python}
# bill = int(input())
# if(bill <= 100):
#     print(float(bill*1.50))
# else:
#     print(float(bill*2.50))

# Write your reference solution here
# units = int(input())
# a = (units*3)
# b= units*5
# c = units*7
# d = units*10
# if(units <= 100):
#         print("Bill: Rs.",a)
# elif(units <=200):
#         print("Bill: Rs.",(b))
# elif(units<=300):
#         print("Bill: Rs.",(c))
# elif(units < 300):
#         print("Bill: Rs.",(d).round(d, 2))

# km = float(input())
# if(km <= 2):
#         print(50.00)
# elif(km >2):
#         print(50.00 + 15*(km - 2))
# else:
#         print("No trip")\
        
# num = int(input())
# if(num >0):
#         print("Positive")
#         if(num > 100):
#                 print("Large")
#         if(num % 2 == 0):
#                 print("Even")
# else:
#         print("nothing")

# player1 = input()
# player2 = input()
# a = "rock"
# b = "paper"
# c = "scissors"
# if(player1 == "rock" and player2 == "paper"):
#         print("Player 2 wins")
# elif(player1 == "rock" and player2 == "scissors"):
#         print("Player 1 wins")
# elif(player1 == "paper" and player2 == "rock"):
#         print("Player 2 wins")
# elif(player1 == "paper" and player2 == "scissors"):
#         print("Player 2 wins")
# elif(player1 == "scissors" and player2 == "rock"):
#         print("Player 2 wins")
# elif(player1 == "scissors" and player2 == "paper"):
#         print("Player 1 wins")
# elif(player1 == "rock" and player2 == "rock"):
#         print("Draw")
# elif(player1 == "scissors" and player2 == "scissors"):
#         print("Draw")
# elif(player1 == "paper" and player2 == "paper"):
#         print("Draw")

# age = int(input())
# income = int(input())

# if(age >= 18):
#     if(income >= 30000):
#         print("Loan approved.")
#     else:
#         print("Not eligible: income too low.")
# else:
#     print("Not eligible: age requirement not met.")   
# Write your reference solution here
# n = int(input())

# if(n>0):
#     print("Positive")
# elif(n >0 or n %2 == 0):
#     print("Even")
# elif(n > 100):
#     print("Large")    
# score = int(input())
# attendance = int(input())

# if(score > 90 and attendance > 90):
#     print("Star student")
#     print("Perfect attendance")
# elif(score > 90 or attendance < 90):
#     print("Star student")
# elif(score < 90 or attendance > 90):
#     print("Perfect attendance")
# else:
#     print("No badges earned.")
# units = float(input())
# total_price = 0.0
# if (units > 0.0):
#     if (units <= 100):
#         total_price = total_price + 3 * units
#         units = 0.0
#     else:
#         total_price = total_price + 300
#         units = units - 100

# if (units > 0.0):
#     if (units <= 100):
#         total_price = total_price + 5 * units
#         units = 0.0
#     else:
#         total_price = total_price + 500
#         units = units - 100

# if (units > 0.0):
#     if (units <= 100):
#         total_price = total_price + 7 * units
#         units = 0.0
#     else:
#         total_price = total_price + 700
#         units = units - 100

# if (units > 0.0):
#     total_price = total_price + 10 * units
#     units = 0.0

# print(f"{total_price:.2f}")

# a = int(input())
# b= int(input())
# c = int(input())
# d = int(input())

# if(a>b>c>d):
#         print("Man", a)
#         print("Min", d)
# elif(b>c>d>a):
#         print("Man", b)
#         print("Min", a)
# elif(c>d>a>b):
#         print("Man", c)
#         print("Min", b)
# elif(d>a>b>c):
#         print("Man", d)
#         print("Min", c)

# price = int(input())
# quantity = int(input())
# days = int(input())
# unit = int(input())
# if(price<500):
#     print("On sale")
#     if(quantity<10):
#         print("Low stock")
#         if(days < 30):
#             print("New arrival")
#             if(unit < 1000):
#                 print("Bestseller")
#             else:
#                 print("No tags applicable.")
#         else:
#             print("No tags applicable.")
#     else:
#         print("No tags applicable.")
# else:
#     print("No tags applicable.")

# score1 = int(input())
# score2 = int(input())
# score3 = int(input())

# average = (score1 + score2 + score3) / 3

# if average > 80 and score1 >= 60 and score2 >= 60 and score3 >= 60:
#     print("Distinction awarded.")
# else:
#     print("No distinction awarded.")

# Write your reference solution here
# score = int(input())
# percentage = (score/150)*100

# if(percentage >= 90):
#         print(f"Merit scholarship awarded. Percentage: {percentage:.2f}%")
# else:
#         print(f"Not eligible for merit scholarship. Percentage: {percentage:.2f}%")
        
# amount = int(input())
# discount = amount - (amount/100)*10
# if(amount > 1000):
#         print(f"Discounted price: Rs.{discount:.2f}")
# else:
#         print("No discount applied.")

# age = int(input())

# if(age>= 18):
#         print("You can vote.")
# else:
#         print("You can't vote.")

# spend = int(input())
# if(spend < 500):
#         print("Bronze")
# elif(500<= spend < 2000):
#         print("Silver")
# elif(2000<= spend < 5000):
#         print("Gold")
# else:
#         print("Platinum")

# sku, name, quantity, price = input().split(",")

# quantity = int(quantity)
# price = float(price)

# total = quantity * price

# print(name, f"{total:.2f}")

# n = int(input())
# tags = input().split()

# unique_tags = sorted(set(tags))

# print(*unique_tags)

# a, b = map(int, input().split())

# c = min(a, b)

# if a > b:
#     if 2*a > b:
#         print()

# n = int(input())

# if n % 2 == 0:
#     print(-(n//2))
# else:
#     print((n//2)+1)

# while loop----------->

# i = 1
# while(i <= 10):
#     print(i)
#     i += 1
    
# print(i)
# while True:
# while True:
#     password = input("Enter password: ")
#     if password == "secret":
#         print("unlocked")
#         break
#     print("Retry the correct password")

attempts = 1
while attempts <= 5:
    attempts += 1
    pin = int(input("Enter your pin: "))
    if attempts > 5:
        print("Too many attempts. Access denied.")
        break
    if pin == 1234:
        print("Access granted")
        break
    print("Incorrect pin. attempt left: " + str(5 - attempts))