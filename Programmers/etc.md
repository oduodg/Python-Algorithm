# etc

## [키패드 누르기](https://programmers.co.kr/learn/courses/30/lessons/67256)

Level1이라 만만하게 봤지만 처음 생각한 알고리즘대로 되지 않았다. 하지만 끝까지 혼자 풀려고 했고 성공!!

> 알고리즘

- 키패드의 *은 10으로, 0은 11으로, #은 12이라고 설정했다.
- 따라서 leftThumb = 10, rightThumb = 12로 시작한다.
- 주어진 배열 numbers의 number들을 for문으로 돌면서 answer에 ‘L’또는 ‘R’ 을 추가한다.
- 좌측 배열(1, 4, 7)의 조건 → 무조건 왼손이 입력
- 우측 배열(3, 6, 9)의 조건 → 무조건 오른손이 입력
    - 숫자가 아닌 *과 #은 입력하는 경우가 없으므로 제외했다.
- 중간 배열인(2, 5, 8, 0)의 조건
    - 맨 처음 숫자가 0인 경우는 number를 11로 변경해주어야 한다.
    - 왼손 엄지손가락과의 거리 측정과 오른손 엄지손가락과의 거리 측정을 한다.
        - 입력된 숫자와 현재 위치가 같다면 거리 = 0 이다.
        - `n = (현재 위치- 입력된 숫자)의 절댓값` 이라고 하면, `거리 = n // 3 + n % 3` 이다.
        - 왼손과의 거리와 오른손과의 거리를 비교한다.
- 배열 answer의 문자열로 합쳐서 return 한다.

---

## [두 개 뽑아서 더하기](https://programmers.co.kr/learn/courses/30/lessons/68644)

3분만에 풀 정도로 굉장히 쉬움.

> 알고리즘

- 이중 for문을 이용해 서로 다른 인덱스 두 개의 수를 더함.
- answer에 더한 값이 없으면 추가.
- 오름차순으로 정렬한 answer를 리턴

---

## [2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)

> 알고리즘

- 각 날짜를 새해가 시작한 이후 몇 번째 날인지로 설정함. (ex: 1월 1일은 `1`일째, 2월 1일은 `32`일째)
- 1월 1일이 금요일이므로 1월 7일은 목요일임. → 7의 배수이면 목요일, 나머지 요일은 7로 나눈 나머지로 판단
- 각 월마다 일 수가 다르므로 해당 딕셔너리를 만듬 {1: 31, 2: 29, 3: 31, 4: 30 ... }
- 1부터 a까지 for문을 이용해 b에 각 월에 해당하는 일 수만큼 더해줌(1월 1일을 기준으로 몇 번째날인지)
- b를 7로 나눈 나머지를 이용해 요일을 판단하고 리턴

---

## [내적](https://programmers.co.kr/learn/courses/30/lessons/70128)

매우 쉬움.

> 알고리즘
 
- 리스트 컴프리헨션을 이용해 a[i] * b[i] 값을 담는 리스트를 생성
- sum함수를 이용하여 sum(리스트)를 리턴

```python
def solution(a, b):
		return sum([x * y for x, y in zip(a, b)]
```
zip()을 이용한 한 줄 풀이

### zip()

: 여러 개의 iterable 자료형(리스트, 튜플 등 반복 가능한 자료형)이 **개수가 동일**할 때 묶어주는 역할을 하는 함수

```python
# iterable자료형
num = [1, 2, 3]
fruit = ['apple', 'banana', 'orange']
color = ['red', 'yellow', 'orange']

print(list(zip(num, fruit, color)))
👉🏻 [(1, 'apple', 'red'), (2, 'banana', 'yellow'), (3, 'orange', 'orange')]
```

---

## [약수의 개수와 덧셈](https://programmers.co.kr/learn/courses/30/lessons/77884)

쉬움.

> 알고리즘

- left부터 right까지 for문으로 돌면서
- 기본으로 cnt(약수의 개수) = 2 로 초기화했다.(1과 자기 자신)
- 예외) 숫자가 1인 경우는 cnt = 1
- 최대한 시간을 줄이기 위해, 2부터 숫자의 절반까지만 for문으로 돌림
- 약수인 경우
    - 제곱근인 경우엔 cnt += 1
    - 찾은 약수의 짝(?)이 숫자의 절반보다 작은 경우 cnt += 1
        
        (예를 들어,  15의 약수 중 3과 5)
        
    - 나머지의 경우는 숫자/2 한 것보다 큰 약수의 짝을 더해줘서 cnt += 2
- 구한 약수의 개수 cnt가 짝수이면 숫자를 그대로 answer에 추가하고, 홀수이면 -1을 곱해서 추가함
- sum(answer)로 리스트의 모든 요소의 합을 리턴.

> 다른 아이디어
 

제곱수의 약수는 홀수개, 제곱수가 아닌 수의 약수는 짝수개인 것을 이용

```python
def solution(left, right):
		answer = 0
		for i in range(left, right+1):
				if int(i**0.5) == i**0.5: # i**0.5가 자연수이면
						answer -= i
				else:
						answer += i
		return answer
					
```

시간 복잡도도 O(n)이고 1에 대한 예외 케이스도 생각하지 않아도 된다.

---

## [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935)

> 알고리즘

- n이 1, 2인 경우는 예외 케이스
- n 이 1이 아닐 때까지 while문으로
    - n을 3으로 나눈 나머지를 str형태로 num 배열에 추가
    - n은 n을 3으로 나눈 몫으로 초기화
- while문 종료 후 ‘1’을 num 배열에 추가
- reverse 해준 뒤, 3진법으로 계산하는 방식 사용

→ 시간 초과

> 다른 아이디어

파이썬 내장함수 int()는 진법 변환이 지원됨!!!

사용법: `int(숫자, n)` (n은 n진법의 n에 해당한다.)

`divmod()` 를 사용하여 몫과 나머지를 동시에 구하고 몫은 n으로 rest는 배열에 더해준다.

```python
def solution2(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3) # n을 3으로 나눈 몫(n)과 나머지(rest)
        answer += str(rest)
    
    answer = int(answer, 3) # answer를 3진법으로 변환(python의 int함수는 진법 변환을 지원한다.)

    return answer
```

---

## [음양 더하기](https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3)

매우 쉬움

> 알고리즘

- 정수 배열의 길이만큼 for문을 돌면서
- 부호 배열의 요소가 True이면 answer에 더하고, False이면 빼기
- answer를 리턴

---

## [나머지가 1이 되는 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/87389)

매우 쉬움

> 알고리즘

- 가장 작은 자연수를 찾는 것이므로 1부터 n까지 for문으로 반복하면서, 나머지가 1인 경우 바로 x를 리턴한다.

---

## [없는 숫자 더하기](https://programmers.co.kr/learn/courses/30/lessons/86051)

매우 쉬움

> 알고리즘

- 0~9까지의 합을 total에 저장하고, total에서 numbers의 합을 뺀 값을 리턴한다.

---

## [문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3)

매우 쉬움

> 알고리즘

- if: 문자열의 길이가 4와 6이 아닐 때, False 리턴
    
    → and 조건으로 연결해야 함(or 아님 주의)
    
- else: `.isdigit()` 을 사용하여, True or False 판별 후 리턴

---

## [문자열 내 p와 y의 개수](https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3)

매우 쉬움

> 알고리즘

- `.islower()` 를 사용하여 문자열 s를 모두 소문자로 변환한다.
- `.count('알파벳')` 를 사용하여 ‘p’와 ‘y’의 개수가 같으면 True를 리턴

---

## [문자열 내림차순으로 배치하기](https://programmers.co.kr/learn/courses/30/lessons/12917)

매우 쉬움

> 알고리즘

- `sorted()` 를 사용하여 s를 역순으로 정렬한다. (아스키 코드의 순서 상 A-Z, a-z 순이다.)
    
    → sorted()는 리스트로 변환해서 리턴한다.
    
- `.join()` 를 사용하여 리스트의 각 요소로 쪼개진 문자들을 합치고 리턴한다.

---

## 두 정수 사이의 합

매우 쉬움

> 알고리즘

- if: a와 b가 같은 수인 경우, a를 리턴한다.
- else: a, b 중 작은 값, 큰 값을 따로 저장하고, for문을 이용해 작은 값~큰 값까지 더해 주고 그 값을 리턴한다.

> 다른 아이디어

- a > b 인 경우, a와 b를 swap한다. `a, b = b, a`
- sum함수 내에 range함수를 이용해 리턴한다. `sum(range(a, b+1))`

---

## [나누어 떨어지는 숫자 배열](https://programmers.co.kr/learn/courses/30/lessons/12910)

매우 쉬움

> 알고리즘
 
- for문을 이용하여, arr에 들어있는 숫자 num이 divisor로 나눈 나머지가 0이면 answer에 num을 추가한다.
- answer이 빈 리스트이면 [-1]을 리턴
- 아니면, answer를 오름차순으로 정렬(`sorted()`)하여 리턴

> 다른 아이디어

- return 값으로 한 줄에 구현(리스트 컴프리헨션)

    → sorted([n for n in arr if n % divisor == 0]) or [-1]

- return에 or를 사용할 수 있다.

    → or 앞의 구문이 거짓이면 or 뒷부분 실행

---

## [약수의 합](https://programmers.co.kr/learn/courses/30/lessons/12928)

매우 쉬움

> 알고리즘

- 리스트 컴프리헨션을 이용하여 return에 한 줄로 구현
- 1부터 n까지의 수 중 num으로 나누었을 때 나머지가 0인 수를 sum()하여 리턴

---

## [수박수박수박수박수박수?](https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3)

매우 쉬움

> 알고리즘

- n이 짝수이면 “수박” * (n을 2로 나눈 몫)을 리턴
- n이 홀수이면 “수박” * (n을 2로 나눈 몫) + “수” 를 리턴

---

## [자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)

매우 쉬움

> 알고리즘

- n을 str타입의 리스트로 변환시킨다.
- `map()` 함수를 이용해 각 요소를 int 타입으로 다시 변환한 뒤, sum() 함수를 이용해 합을 리턴