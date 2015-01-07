print "Please enter ten integers when asked and I will calculate the highest odd number entered."
ans = 0
a = int(raw_input("Please enter integer #1:"))
if a%2 != 0:
    ans = a
b = int(raw_input("Please enter integer #2:"))
if b%2 != 0 and b > ans:
    ans = b
c = int(raw_input("Please enter integer #3:"))
if c%2 != 0 and c > ans:
    ans = c
d = int(raw_input("Please enter integer #4:"))
if d%2 != 0 and d > ans:
    ans = d
e = int(raw_input("Please enter integer #5:"))
if e%2 != 0 and e > ans:
    ans = e
f = int(raw_input("Please enter integer #6:"))
if f%2 != 0 and f > ans:
    ans = f
g = int(raw_input("Please enter integer #7:"))
if g%2 != 0 and g > ans:
    ans = g
h = int(raw_input("Please enter integer #8:"))
if h%2 != 0 and h > ans:
    ans = h
i = int(raw_input("Please enter integer #9:"))
if i%2 != 0 and i > ans:
    ans = i
j = int(raw_input("Please enter integer #10:"))
if j%2 != 0 and j > ans:
    ans = j
print "Thanks! You entered the numbers",a,b,c,d,e,f,g,h,i,"and",j
if ans == 0:
    print "...and there's not an odd number among them!"
else:
    print "...and of these",ans,"was the highest odd number entered."
    
