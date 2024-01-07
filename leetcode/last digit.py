class Solution:
    def plusOne(self, digits):
        mystring = ""

        for i in range(len(digits)):
            mystring += str(digits[i])
        mystring = int(mystring) + 1
        mystring = str(mystring)

        newlist = []

        for i in range(len(mystring)):
            newlist.append(int(mystring[i]))

        return newlist


ob = Solution()
inputlist = list(map(int,input().split(',')))
b = ob.plusOne(inputlist)
print(b)