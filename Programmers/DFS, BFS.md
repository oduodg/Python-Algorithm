# DFS, BFS

## [타겟 넘버](https://programmers.co.kr/learn/courses/30/lessons/43165)

- dfs, bfs 인지 → 다음 수에 더하기 or 빼기로 이중 노드로 뻗어나간다 생각
- `map`과 `itertools.product` 활용
- `s = list(map(sum, itertools.product(*l)))`
    - s에는 모든 조합의 각각의 합이 담긴다.
    - 따라서 target값을 카운트하는 s.count(target)을 리턴

## itertools.product

데카르트 곱이라고도 하는 cartesian product를 표현할 때 사용하는 메소드이다(DB의 join, 관계 대수의 product를 생각하면 된다). 이 메소드의 특징은 두 개 이상의 리스트의 모든 조합을 구할 때 사용된다.

```python
from itertools import product

_list = ["012", "abc", "!@#"]
pd = list(product(*_list))
# [('0', 'a', '!'), ('0', 'a', '@'), ('0', 'b', '!'), ('0', 'b', '@'), ('1', 'a', '!'), ('1', 'a', '@'), ('1', 'b', '!'), ('1', 'b', '@')]
```
---

## [네트워크](https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3)

- 백준 바이러스 문제와 유사
- 굳이 그래프를 만들 필요가 없다.