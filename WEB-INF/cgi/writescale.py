import sys

#print('Argument list', str(sys.argv))
#print(sys.argv[1])

f = open("/var/lib/tomcat8/webapps/ROOT/next/scale.txt", "w+")
f.write(sys.argv[1])
f.close()

