import string
str='!!!!!'
s=''
for i in string.punctuation:
    str = str.replace(i,'z')
    print i
    print str
print str
