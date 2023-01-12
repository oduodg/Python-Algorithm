import collections
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0

    stack = [begin]

    answer = 0
    while len(words):
        sub = []
        for data in stack:
            print('data', data)
            for word in words:
                cnt = 0
                for i in range(len(word)):
                    if word[i] != data[i]:
                        cnt += 1
                    if cnt == 2:
                        break
                if cnt == 1:
                    sub.append(word)
                    words.remove(word)
            print(sub)
        answer += 1
        print(answer)

        if target in sub:
            return answer
        else:
            stack = sub

    return answer

# Test Case
begin = "hit"
target = "cog"

words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]

print(solution(begin, target, words1))
#print(solution(begin, target, words2))
