def removeele(l):
    temp_l = l.copy()
    for i in range(len(l)):
        if l[i]=='.':
            temp_l.remove(l[i])
    return temp_l

def check(l):
    count = 0
    for i in range(len(l)):
        if i%2==0 and l[i]=='H':
            count=count+1
        elif i%2!=0 and l[i]=='T':
            count=count+1
        else:
            pass
    if count == len(l):
        print("Valid")
    else:
        print("Invalid")

R = int(input())
for _ in range(R):
    L = int(input())
    S = list(input())
    if len(S)==S.count('.'):
        print("Valid")
    else:
        S = removeele(S)
        if S[0]=='T':
            print("Invalid")
        else:
            if len(S)%2 !=0:
                print("Invalid")
            else:
                check(S)