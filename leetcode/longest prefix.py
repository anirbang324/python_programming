str1 = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()
    str1.append(ele)

min1=min([len(word) for word in str1])
pre =""
for i in range(min1):
    if "" in str1:
        pre=""
    else:
        chars = [c[i] for c in str1]
        if len(set(chars)) == 1:
            pre= pre+chars[0]

            print(pre)
        else:
            break
print(pre)