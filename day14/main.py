r = int(input())
c = int(input())
a = []
i = 0
while(i < r):
    row = list(map(int, input().split()))
    a.append(row)
    i+=1
print(a)
s = 0
i = 0
while i < r:
    j = 0
    while j< c:
        s += a[j][i]
        j+=1
    i+=1
print(s)