import heapq
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
adj = [[] for _ in range(N+1)] # 학생 번호가 1부터 시작
indegree = [0] * (N+1) #해당 학생 차수
hq = []   
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

# 차수가 0인 학생 추가(현재 줄 설 수 있는 학생)
for i in range(N):
    if indegree[i+1] == 0:
        heapq.heappush(hq, i+1)
        
while hq:
    a = heapq.heappop(hq)
    answer.append(a)
    for b in adj[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            heapq.heappush(hq, b)
            
print(*answer)