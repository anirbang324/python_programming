# -----------------
# Option 1
# -----------------
s = "Hello, World!"
new_s = ""

COMMA = ","
DOT = "."

for char in s:
    if char == COMMA:
        new_s += DOT
    else:
        new_s += char

print(new_s)

# -----------------
# Option 2
# -----------------
s = "Hello, World!"
COMMA = ","
DOT = "."

print(s.replace(COMMA, DOT))