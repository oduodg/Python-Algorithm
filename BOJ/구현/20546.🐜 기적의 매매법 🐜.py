cash = int(input())
stock = list(map(int, input().split()))

def junhyun(cash):
	shares = 0
	for i in range(14):
		if cash >= stock[i]:
			shares += cash//stock[i]
			cash = cash%stock[i]

	return cash + (shares * stock[13])

def sungmin(cash):
	shares = 0
	three_days = []
	for i in range(1, 14):
		if stock[i-1] < stock[i]: # 전일 대비 상승
			three_days.append(1)
		elif stock[i-1] > stock[i]: # 전일 대비 하락
			three_days.append(-1)
		else: # 전일과 동일
			three_days.append(0)

		# 3일 연속 상승 => 전량 매도
		if sum(three_days[-1:-4:-1]) == 3:
			cash += shares * stock[i]
			shares = 0
		# 3일 연속 하락 => 전량 매수
		if sum(three_days[-1:-4:-1]) == -3:
			if cash >= stock[i]:
				shares += cash//stock[i]
				cash = cash%stock[i]

	return cash + (shares * stock[13])

jh = junhyun(cash)
sm = sungmin(cash)
if jh > sm:
	print("BNP")
elif jh < sm:
	print("TIMING")
else:
	print("SAMESAME")