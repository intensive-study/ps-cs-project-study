N = int(input())
arr = list(map(int, input().split()))
target = int(input())

adj = [[] for _ in range(N)]
start = 0
cnt = 0

for idx, root in enumerate(arr):
    if root == -1:
        start = idx 
    elif idx == target: #삭제한 노드는 넣어주지 않음
        #히든 테스트케이스: 노드를 삭제했을 경우, 삭제된 노드가 해당 노드의 유일한 자식노드이면 부모노드가 리프노드
        continue    
    else:
        adj[root].append(idx)
        
def dfs(node):
    global cnt, start

    if start == target:
        return cnt
    
    if not adj[node]:# 리프 노드면 +1
        cnt += 1
        
    for next in adj[node]:
        dfs(next)
        
    return cnt
        
print(dfs(start))