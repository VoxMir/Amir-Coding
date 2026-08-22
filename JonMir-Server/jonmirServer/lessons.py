s = 'GeeksforGeeks is a computer Science portal for Geeks'
ns = ''
cu = 0
cl = 0
cs = 0

for ch in s:
    if ch.isupper():
        cu += 1
        ns += ch.lower()
    elif ch.islower():
        cl += 1
        ns += ch.upper()
    elif ch.isspace():
        cs += 1
        ns += ch


if "iS".lower() in ns.lower():
    print("The word 'is' is in the string")
else:
    print("The word 'is' isnt in the string")


print(f"the length of the string is: {len(ns)}")


print("In original String:")
print("Uppercase -", cu)
print("Lowercase -", cl)
print("Spaces -", cs)
print("After changing cases:")
print(ns)