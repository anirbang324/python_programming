# n = int(input())
# dig = str(n)
#
# sencslastdig = dig[-2]
#
# num = int(sencslastdig)
#
# lastdig = n%10
# ans = num+lastdig
#
# if(ans==3 or ans==8):
#     print("lucky winner")
# else:
#     print("no lucky winner")

n= int(input())

if(n%2==0):
    print(n)
else:
    print(n*2)