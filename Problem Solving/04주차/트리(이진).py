# 136ms
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
parents = list(map(int, input().split()))
delNode = int(input())
tree = defaultdict(list) # 키: 부모, 값: [자식인덱스,...]
leaf = []  # leaf 노드 저장하는 리스트
cnt = 0

for idx, parent in enumerate(parents):
    if idx == delNode or parent == delNode:
        continue
    tree[parent].append(idx)

# 루트 노드 확인하기    
if -1 in tree:
    leaf.append(-1)

while leaf:
    node = leaf.pop()
    if node in tree:
        leaf += tree[node]
    else: # not in
        cnt += 1

print(cnt)        