# i = 1
# while(i < 5):
#     j = 1
#     while(j <= i):
#         print(j, end="");
#         j+=1
#     print()
#     i+=1

i = 1
n = int(input())
while(i<n):
    j = 0
    while(j<=i):
        print("*" * n)
        j+=1
    print();
    i+=1;