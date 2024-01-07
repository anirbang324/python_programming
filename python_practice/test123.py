

if __name__=="__main__":
    #Fill your code here.
    c = int(input())
    str1 = str(c)
    print(str1)
    lst = []
    cnt = 0
    for i in str1:

    # if i not in str1:
        lst.append(i)
    # print(lst)
    b = str(4)
    for i in lst:
        if i==b:
            cnt+=1
    print(cnt)
