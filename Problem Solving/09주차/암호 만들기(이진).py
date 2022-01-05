import sys
input = sys.stdin.readline

l, c = map(int, input().split())
chars = list(input().split())
# l, c = 4, 6
# alphabet = ['a', 't', 'c', 'i', 's', 'w']
alphabet.sort()  # ['a', 'c', 'i', 's', 't', 'w']
visited = [0] * c
answer = []


def check_vowels(lst):
	cnt = 0
	for alpha in lst:
		if alpha in ('a', 'e','i', 'o', 'u'):
			cnt += 1
	return cnt



def dfs(depth, idx):
	if depth == l:
		if check_vowels(answer) >= 1 and (l - check_vowels(answer))>= 2:
			print(''.join(answer))
			return

	for i in range(c):
		if idx < i:
			if not visited[i]:
				visited[i] = 1
				answer.append(alphabet[i])
				dfs(depth + 1, i)
				visited[i] = 0
				answer.pop()

dfs(0, -1)