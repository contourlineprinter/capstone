print("Content-type: text/html\n\n");
count = 0
while (count < 3):     
    count = count + 1
    print("WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOW!\n")

import os
print(os.environ)

f = open('/var/lib/tomcat8/webapps/ROOT/WEB-INF/cgi/itworked.txt','w')
f.write("it worked.")
f.close()