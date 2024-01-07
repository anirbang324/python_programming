#to write something in a file

# s = open("abc.txt","a")
# s.write("this is new content of the  file")
# s.close()
#
# s = open("abc.txt","r")
# print(s.read())
#

#overwrite
s = open("abc.txt","w")
s.write("This is overwrite")
s.close()
s = open("abc.txt","r")
print(s.read())