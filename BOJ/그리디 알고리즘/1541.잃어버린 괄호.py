ans = 0
exp = input().split('-')
for i in exp[0].split('+'):
    ans += int(i)
for j in exp[1:]:
    for k in j.split('+'):
        ans -= int(k)

print(ans)
