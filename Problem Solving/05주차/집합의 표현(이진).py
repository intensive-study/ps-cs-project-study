#시간초과
'''
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

numSets = []
dp = [0 for i in range(n+1)]

for i in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0: # 합집합
        if a == b:
            continue
        
        if dp[a] == 0 and dp[b] == 0:
            dp[a] += i+1
            dp[b] += i+1
        else:
            temp = min(dp[a], dp[b])
            dp[a], dp[b] = max(dp[a], dp[b]), max(dp[a], dp[b])
            for j in range(n+1):
                if dp[j] == temp:
                    dp[j] = max(dp[a], dp[b])

    if op == 1: # check
        if dp[a] == dp[b]:
            print('YES')
        else:
            print("NO")
'''

# Union-Find
# 110088kb	604ms
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = [i for i in range(n+1)]

def find(x):
	if x == lst[x]:
		return x
	lst[x] = find(lst[x])
	return lst[x]

def union(a, b):
	a = find(a)
	b = find(b)

	if a < b:
		lst[b] = a
	else:
		lst[a] = b


for i in range(m):
	op, a, b = map(int, input().split())

	if op == 0:
		union(a, b)

	else:
		if find(a) == find(b): print("YES")
		else: print("NO")
####################################
import sys
sys.setrecursionlimit(10 ** 5)


def solve():
  n, m = map(int, sys.stdin.readline().split())
  p = [-1] * (n + 1)  # 자기자신의 Root를 기록한 Array
  def find(n):  # 두 원소가 같은 root를 갖는지(같은 집합인지) 확인해주는 함수
    if p[n] < 0:
      return n  # p[root]는 음수
    p[n] = find(p[n])  # 재귀반복을 줄여주는 line, 직선상에서 같은 root를 갖고 있다면 root를 새로 갱신해줌
    return p[n]

  def union(x, y):  # 두 집합을 합치는 func => 두 가지 root중 임의의 root로 묶기
    a = find(x)  # root search 1
    b = find(y)  # root search 2
    if a == b:
      return  # 이미 a,b의 root가 동일하면 새로 작업해줄 필요 X
    if p[a] > p[b]:  # 더 큰 Rank가 부모노드가 되게끔 하는 작업
      p[b] += p[a]
      p[a] = b
    else:
      p[a] += p[b]
      p[b] = a

  for _ in range(m):
    c, x, y = map(int, sys.stdin.readline().split())
    if c == 0:  # union
      union(x, y)
    else:
      if x == y:
        sys.stdout.write("YES\n")
        continue
      sys.stdout.write("YES\n") if find(x) == find(y) else sys.stdout.write("NO\n")

solve()		
'''
import sys
input = sys.stdin.readline


n, m = map(int, input().split())

parent = [-1] * (n + 1)


def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    # print(a, b, 'union')
    # print(parent, 'before')
    if a == b:
        return

    if -parent[a] > -parent[b]:  # a가 더 큰 집합
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
    # print(parent, 'after')


for _ in range(m):
    inst, a, b = map(int, input().split())
    if inst == 0:  # a , b 합침
        union(a, b)
    elif inst == 1:  # a, b가 같은 집합에 포함되어있는가
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
'''