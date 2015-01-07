s = 'abcdaefghi'
i = 1
ans = 0
while i < len(s):
    if s[i] > s[i-1]:
        ans = ans + 1
        print s[1]
        i = i + 1
