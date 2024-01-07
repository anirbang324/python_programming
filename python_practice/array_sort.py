A = [12,34,45,21]
t = 0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if(A[i]<A[j]):
            t=A[i]
            A[i]=A[j]
            A[j]=t

listToStr = ''.join([str(elem) for elem in A])

print(listToStr)