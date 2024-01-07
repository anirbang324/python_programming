def sod(num):
    sum =0
    for i in str(num):
        sum+=int(i)
        return sum

num=int(input())
print(sod(num))