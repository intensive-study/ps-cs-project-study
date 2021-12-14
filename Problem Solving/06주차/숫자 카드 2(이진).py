import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
target_cards = list(map(int, input().split()))
cards_dict = defaultdict(int)
answer = []

for card in cards:
	cards_dict[card] += 1

for card in target_cards:
	if cards_dict[card]:
		answer.append(cards_dict[card])
	else:
		answer.append(0)
  
print(*answer)