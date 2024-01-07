# lst = [1,2,3,4,5,6]
# sum = lst[0] + lst[4]
# lst[0] = 13
# print(sum)
# print(lst)

# list = []
# size = int(input("enter the size"))
# for i in range(0,size):
#     val = int(input())
#     list.append(val)
#
# print(list)


lst = list(map(int,input().split(" ")))
print(lst)

# a,b,c,d = map(int,input().split(" "))
# print(a,b,c,d)

# for i in lst:
#     print(i)
i = 0
while i < len(lst):
    print(lst[i])

    i=i+1

