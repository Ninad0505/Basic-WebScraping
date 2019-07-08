f = open('coordinates.txt','r+')
a = ['=getGoogleOverlay']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open('coordinates.txt','w+')
for line in lst:
    f.write(line)


contents = f.read()
words = contents.split()
print(words)