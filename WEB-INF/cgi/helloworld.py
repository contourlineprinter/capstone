print("Content-type: text/html\n\n");
count = 0
while (count < 3):     
    count = count + 1
    print("WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOW!\n")

f = open('itworked.txt','w')
f.write("it worked.")
f.close()