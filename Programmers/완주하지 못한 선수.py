import collections

def solution(participant, completion):
    p = collections.Counter(sorted(participant))
    c = collections.Counter(sorted(completion))
    result = p - c
    return list(result)[0]

# Test case
participant1 = ["leo", "kiki", "eden"]
completion1 = ["eden", "kiki"]
participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]

print(solution(participant1, completion1))
print(solution(participant2, completion2))
print(solution(participant3, completion3))

