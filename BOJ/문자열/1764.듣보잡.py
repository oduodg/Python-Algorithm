import sys
input = sys.stdin.readline # 입력 가속
n, m = map(int, input().split())
ear = [0] * n
eye = [0] * m
for i in range(n):
    ear[i] = input().rstrip()
for j in range(m):
    eye[j] = input().rstrip()
ear = set(ear)
eye = set(eye)
answer = ear.intersection(eye)
print(len(answer))
for name in sorted(answer):
    print(name)