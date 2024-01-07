# def listsum(samplelist):
#     samplelist=[]
#     # Python program to find sum of elements in list
#     # Iterate each element in list
#     total=0
#     # and add them in variable total
#     for ele in range(0, len(samplelist)):
#         total = total + samplelist[ele]
#     # printing total value
#     print("Sum of all elements in given list: ", total)
# mylist = []
# a = int(input("plesase enter the number of elements of the list: "))
# for i in range(0,a):
#     e = int(input())
#     mylist.append(e)
# listsum(mylist)
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum((8, 2, 3, 0, 7)))
# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))



