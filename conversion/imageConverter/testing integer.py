arg = " -1 90 -1"

arg = str(arg)
t = arg.split(" ")
a = "-1"
b = "-1"
c = "-1"

print(c)

##if int(c) < 0:
##
##    print("Value ", c)


for i in t:

    if i is not None:
        a = i

    if isinstance(i, str):
        print("string")
    elif isinstance(i, int):
        print("integer")

    
if int(a) < 0: print("Value ", a)
if a is not None: print("Not None")
