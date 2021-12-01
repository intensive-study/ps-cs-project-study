# 156ms
import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
	N = int(input()) # 노드 개수
	parentList = [0] * (N+1)
	for _ in range(N-1):
		parent, child = map(int, input().split())
		parentList[child] = parent  # 인덱스 : child, 값 : parent
	# 찾을 노드 A, B
	a, b = map(int, input().split())
	parentsA, parentsB = [a], [b]
	while parentList[a]:
		a = parentList[a]
		parentsA.append(a)
	while parentList[b]:
		b = parentList[b]
		parentsB.append(b)

			
	while parentsA and parentsB and (parentsA[-1] == parentsB[-1]):
			a, b = parentsA.pop(), parentsB.pop()

	print(a)