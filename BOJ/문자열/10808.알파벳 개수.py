import collections
s = input()
cnt = collections.Counter(s)
for i in range(97,123):
    print(cnt[chr(i)], end=" ")