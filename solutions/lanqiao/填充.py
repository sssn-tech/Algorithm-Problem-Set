
s = list(input())
n = len(s)
ans = 0
for i in range(n):
    if i == 0:
        if s[i] == '?':
            if i + 1 < n and s[i + 1] != '?':
                s[i] = s[i + 1]
            else:
                s[i] = '0'
    else:
        if s[i] == '?':
            if s[i - 1] == 'x':
                if i + 1 < n and s[i + 1] != '?':
                    s[i] = s[i + 1]
                else:
                    s[i] = '0'
            else:
                s[i] = s[i - 1]
        if s[i] == s[i - 1] and s[i] != 'x':
            ans += 1
            s[i] = 'x'
            s[i - 1] = 'x'
print(ans)