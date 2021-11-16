# key 줍줍 '|' 연산 
# 문 만나면 key 확인 '&' 연산
# key값의 비트마스크를 Z축으로 visited 3차원

# https://chldkato.tistory.com/51
# https://j2wooooo.tistory.com/39
# https://hj-bank.tistory.com/entry/%EB%8B%AC%EC%9D%B4-%EC%B0%A8%EC%98%A4%EB%A5%B8%EB%8B%A4-%EA%B0%80%EC%9E%90-1194%EB%B2%88-JAVA
from collections import deque

dir = [(-1,0), (1,0), (0,-1), (0,1)]
N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
# a 열쇠를 가지고 방문한 것과 키없을때 방문한건 중복 가능하기 때문에 3차원 배열
visited = [[[-1] * (1 << 6) for _ in range(M)] for _ in range(N)] #a abcdef 6개 문자

# 시작 지점 큐에 넣고 방문 처리
start_x, start_y = map(int, [(x, y) for x in range(N) for y in range(M) if maze[x][y] == '0'][0])
q = deque([[start_x, start_y, 0]])
visited[start_x][start_y][0] += 1 
answer = -1

while q:
    x, y, z = q.popleft() #z는 보유한 키

    if maze[x][y] == '1': #출구
        answer = visited[x][y][z]
        break

    for d in dir:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][z] == -1:
            next = maze[nx][ny]

            if next == '#': #벽
                continue

            if next == '.' or next == '1' or next == '0': #길 또는 출구 또는 시작점갈 수 있음
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])
                
            elif next in ['a','b','c','d','e','f']: #키
                nz = (z | 1 << (ord(next) - ord('a'))) #키 업데이트 0 | 1 = 1
                if visited[nx][ny][nz] == -1:
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append([nx, ny, nz])

            else: #문
                match = (z & 1 << (ord(next) - ord('A'))) #문에 맞는키 존재 1 & 1 = 1
                if match != 0 :
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])


print(answer)