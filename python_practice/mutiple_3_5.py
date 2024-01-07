n = int(input())
arr = []

for i in range(n):
    if (i%3==0 or i%5==0):
        arr.append(i)

print(sum(arr))