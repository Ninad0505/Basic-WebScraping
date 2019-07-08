import re

string = 'my name is ninad. I am very good in python.'
search = re.findall(r'[py]\w+', string)
print(search)

s = open("demo.txt")
contents = s.read()

# lat_long = re.findall(r'\w+', contents)
# print(lat_long)

f = 'kbdsj cbd djn. jhbsc. <sb> nknsc . dak123 ,ekhb.' \
    'sndkjds' \
    'ebdnn jc sbc knecs.kesb, besbjh 246 3876 82643.73' \
    '(bse) neskne.' \
    'ehdk (ehdkedkje kdcn)'

#print(re.findall('\(.*?\)',s))

words = contents.split()
print(words)

sub = "=getGoogleOverlay"

final = [ i for i in words if sub in i]
print(final)
print(len(final))

file = open('coordinates.txt', 'w+')
for i in final:
    file.write(str(i) + '\n')



