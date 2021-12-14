import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
counter = Counter(tuple(map(int, input().split())))
m = int(input())

for num in map(int, input().split()): print(counter[num], end=' ')