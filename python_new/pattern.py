r = int(input("enter the value for the row:"))
for i in range(0,r):  #outer loop
    for j in range(0,i+1): #inner loop
        print("*",end=' ')
    print("\r")
