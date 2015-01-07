print "This is an alternative method for identifying largest odd number"
x = int(raw_input("Give me integer x..."))
y = int(raw_input("Give me integer y..."))
z = int(raw_input("Give me integer z..."))
ans=0
if x%2 != 0:
    ans = x
if y%2 != 0 and y > ans:
    ans = y
if z%2 != 0 and z > ans:
    ans = z
if ans == 0:
    print "All the numbers you entered were even!"
else:
    print "The largest odd number entered was",ans,"!"
