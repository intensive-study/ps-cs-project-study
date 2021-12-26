import sys
input = sys.stdin.readline

for _ in range(int(input())):
	n = int(input())
	parentList = [0] * (n+1)
	for _ in range(n-1):
		parent, child = map(int, input().split())
		parentList[child] = parent
	a, b = map(int, input().split())
	parent_a, parent_b = [a], [b]
	while parentList[a]:
		a = parentList[a]
		parent_a.append(a)
	while parentList[b]:
		b = parentList[b]
		parent_b.append(b)

	while parent_a and parent_b:
		a = parent_a.pop()
		b = parent_b.pop()
		if a == b:
			common_anc = a
		else:
			break
	print(common_anc)