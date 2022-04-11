s = list(map(int, input()))
group0 = 0
group1 = 0

prev = s[0]
for i in range(1, len(s)):
    if s[i] != prev:
        if prev == 0:
            group0 += 1
        else:
            group1 += 1
        prev = s[i]
if prev == 0:
    group0 += 1
else:
    group1 += 1
    
print(min(group0, group1))
