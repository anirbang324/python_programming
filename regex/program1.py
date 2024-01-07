import re
# my sentence is starting with 'The' and ending with 'blue'
# t1 = "The sky is blue"
# b = re.search("^The.*blue$",t1)
# if b:
#     print("matched")
# else:
#     print("does not match")

#findall - returns all the matches
# s1 = "The ball is blue"
# y = re.findall("a",s1)
# print(y)

#search function
s2 = "He is a boy"
# s = re.search("\s",s2)
# print(s.start())

#split - splits the string and returns us the output by placing the elements in a list
d = re.split("\s",s2)
print(d)

#sub - used to replace

v = re.sub("a","b",s2,2)
print(v)

#special sequence : \

z = re.findall("\AHe",s2)
print(z)
if z:
    print("True")
else:
    print("False")