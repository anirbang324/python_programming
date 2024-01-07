def listsum(samplelist):
    samplelist=[]
    # Python program to find sum of elements in list
    # Iterate each element in list
    total=0
    # and add them in variable total
    for ele in range(0, len(samplelist)):
        total = total + samplelist[ele]
    # printing total value
    return total
samplelist = []
a = int(input("plesase enter the number of elements of the list: "))
for i in range(0,a):
    e = int(input())
    samplelist.append(e)
print("sum is: ",listsum(samplelist))