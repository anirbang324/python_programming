f1 = open("abc.txt","rt")
# print(f1.read())
#to read a specific number of characters
# print(f1.read(3))
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
# print(f1.readline())
for i in f1:
    print(i)
f1.close()

