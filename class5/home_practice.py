# #Q) 1 -->


# print("Starting up the program...")
# print("Doing some setup...")
# print "Hello!" # here its symntax error and also its compilation error 
# print("All done.")

# #Q) 2 -->


# x = 5
# print("x is", x)
# y = 7
# print("y is", y)
# x = "hello"
# print("now x is", x) 
# print(x + 10) # its again an error occured of type error and its a runtime error 
# print("This line never runs")


# #Q) 3 -->

# print("Starting up the program...")
# print("Doing some setup...")
# Print("Hello!") # here its an symntax error and also it is an runtime error 
# print("All done.")

# #Q) 4 -->

# print("Starting...")
# print(score) # its again a runtime error and also name error because score is not defined here 
# print("This never runs")

# #Q) 5 -->

# print("Starting...")
# age: int # its again an runtime error because age is not defined here
# print(age)

# # Q) 6 -->

# print("Calculating the class average...")
# total = 100
# count = 0
# print(total / count) # here its again a runtime erro and zero division error here
# print("Done")

# # Q) 7 -->

# x = 35
# y = 19
# rem = x - int(x/y) * y # this is also a way to find reminder without using modulo operator
# print(rem)

# # Q) 8 -->

# print(35 % 19) # 16
# print(17 % 5) # 2
# print(20 % 4) # 0
# print(5 % 8) # 5

# # Q) 9 -->

# print(13 % 2) # 1
# print(8 % 2) # 0
# print(2025 % 10) # 5
# print((10 + 5) % 12) # 3

# # Q) 10 -->

# print(12 % 4) # 0
# print(12 % 5) # 2
# print(12 % 6) # 0
# print(12 % 7) # 5

# # Q) 11 -->
# print(7 % 0) # this is a runtime error and also zero division error 

# # Q) 12 -->

# print(type(5 + 4)) # int
# print(type(5 - 4)) # int 
# print(type(5 * 4)) # int
# print(type(5 / 4)) # float
# print(type(5 % 4)) # int 

# # Q) 13 -->

# print(19 // 7) # 2
# print(100 // 7) # 14
# print(8 // 0) # this is again an runtime error and also zero division error 

# # Q) 14 -->

# print(int(-19 / 7)) # -2.81
# print(-19 // 7) # -3

# # Q) 15 -->

# print( 19 // 7) # 2
# print(-19 // -7)
# print(-19 // 7)
# print( 19 // -7)

# print(2 ** 14300)

# print(pow(0.2, 3))

# x , y = -19 , 7
# print(x -int(x/y) * y)
# print(x % y)

i = int(input("enter the year: "))

if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
    print(i, "is a leap year")
else:
    print(i, "is not a leap year")
    