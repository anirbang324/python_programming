def io(a):
    return ' '.join([a[::-1] for a in a.split(' ')])

a=input()
print(io(a))