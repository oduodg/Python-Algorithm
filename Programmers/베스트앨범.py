import collections

def solution(genres, plays):
    answer = []

    genreDict = collections.defaultdict(int) # {장르 : 총 재생 횟수}
    playDict = collections.defaultdict(list) # {장르 : [(플레이 횟수, 고유 번호)]}

    # 딕셔너리 만들기
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genreDict[genre] += play
        playDict[genre] += [(play, i)]

    # 장르별 재생 횟수가 많은 순으로 정렬
    genreSort = sorted(genreDict.items(), key=lambda x: x[1], reverse = True) # 딕셔너리 value로 정렬하기

    # 재생 횟수가 많은 순, 고유 번호가 낮은 순으로 정렬
    for (genre, totalPlay) in genreSort:
        playDict[genre] = sorted(playDict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in playDict[genre][:2]]  # 장르별로 노래 최대 2개 수록
    return answer

# Test Case
gen = ["classic", "pop", "classic", "classic", "pop"]
pla = [500, 600, 150, 800, 2500]

print(solution(gen, pla))