import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize
team1 = []


def teamStat(team1, team2):  # 팀 능력치 계산
    stat1 = 0
    stat2 = 0
    for i in range(n//2-1):
        for j in range(i+1, n//2):
            stat1 = stat1 + s[team1[i]][team1[j]] + s[team1[j]][team1[i]]
            stat2 = stat2 + s[team2[i]][team2[j]] + s[team2[j]][team2[i]]
    return abs(stat1 - stat2)


def makeTeam(number_of_players, start):
    global ans
    if number_of_players == n//2:  # team1 결성이 완료되면
        # team2 = list(set([i for i in range(n)]) - set(team1))
        team2 = [i for i in range(n) if i not in team1]  # team2 결성
        diff = teamStat(team1, team2)  # 팀 능력치 차이 구하기
        ans = min(diff, ans)

        # 차가 0이면 출력하고 바로 종료
        if ans == 0:
            print(ans)
            sys.exit()
        return

    for player in range(start, n):  # 백트래킹으로 팀 구성
        if player not in team1:
            team1.append(player)
            makeTeam(number_of_players+1, player)
            team1.remove(player)


makeTeam(0, 0)
print(ans)
