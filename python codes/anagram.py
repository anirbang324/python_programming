str1 = input("Enter your String:").lower()
str2 = input("Enter your String:").lower()
# checking the length of both the basestring
if (len(str1) == len(str2)):
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)

    if (sort_str1 == sort_str2):
        print('Anagram')
    else:
        print('Not Anagram')
else:
    print('Not Anagram')