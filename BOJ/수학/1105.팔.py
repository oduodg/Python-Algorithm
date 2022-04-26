L, R = map(int, input().split())
cnt = 0
if len(str(L)) != len(str(R)):
    print(cnt)
else:
    for i in range(len(str(L))):
        if str(L)[i] != str(R)[i]:
            break
        else:
            if str(L)[i] == '8':
                cnt += 1
    print(cnt)

