#finding duplicate

# a = [1,2,3,1,2,4]
# c = 0
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]==a[j]):
#             c = c+1
# if(c>1):
#     print("duplicate present")
# else:
#     print("no duplicate present")

#removing duplicate

# a = [1,2,3,1,2,3]
# new = []
#
# for i in a:
#     if i not in new:
#         new.append(i)
# print(new)


#reversing an array and sorting

# a = [4,5,2,321,4, 32,2]
# r = 0
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]>a[j]:
#             r = a[i]
#             a[i] = a[j]
#             a[j] = r
# print(a)

#finding missing number

# a = [1,2,3,4,6,7,8,9]
# lastele = a[-1:][0]
# print(lastele)
# sum1 = lastele*(lastele+1)/2
# sum2 = sum(a)
# print(int(sum1-sum2))
