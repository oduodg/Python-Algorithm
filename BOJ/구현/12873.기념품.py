n = int(input())
people = [i for i in range(1, n+1)]
t = 1
idx = 0
while len(people) > 1:
    idx = (idx + (t**3 - 1)) % len(people)
    people.pop(idx)
    t += 1
print(people[0])
