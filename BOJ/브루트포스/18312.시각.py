n, k = map(int, input().split())

# 00시 00분 00초 ~ n시 59분 59초
h = [i for i in range(0, 24)]
m = [i for i in range(0, 60)]

def convert(li):
	for i in range(len(li)):
		if len(str(li[i])) == 1:
			li[i] = list("0" + str(li[i]))
		else:
			li[i] = list(str(li[i]))
	return li

h, m = convert(h), convert(m)

h_cnt = 0
for i in range(0, n+1):
	if str(k) in h[i]:
		h_cnt += 1

h_not_cnt = n+1 - h_cnt # k가 포함되지 않은 시

m_cnt = 0
for i in range(0, 60):
	if str(k) in m[i]:
		m_cnt += 1

m_not_cnt = 60 - m_cnt  # k가 포함되지 않은 분(초)

total = (n+1) * 60 * 60
complement = h_not_cnt * m_not_cnt * m_not_cnt
print(total - complement)