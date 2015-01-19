#this runs with the traditional python version, so just use python in the command line as opposed to python3.3 like you usually do

print "Content-Type: text/html"     

print "<html><head></head><body><pre>"
a = ['f','d','s','a']
x = -1
scope = vars()
for i in a:
    scope['x']+=1
    print a[x]
print "</pre></body></html>"