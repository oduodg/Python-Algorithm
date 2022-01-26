import collections, math
n = int(input()) # 방 번호 n
n = str(n)
n = n.replace('9', '6') # 9를 6으로 변경
cnt = collections.Counter(n)
if not cnt['6']:
    print(cnt.most_common(1)[0][1])
else:
    cnt['6'] = math.ceil(cnt['6'] / 2)
    print(cnt.most_common(1)[0][1])