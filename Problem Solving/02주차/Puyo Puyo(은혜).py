from collections import deque

pypy = [list(input()) for _ in range(12)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

# 행x, 열y
def delPY(pypan, xylist): # 뿌요삭제
    for xy in sorted(xylist):
        x, y = int(xy[0]), int(xy[1])
        for i in range(x, 0, -1):
            pypan[i][y] = pypan[i-1][y]
            if pypan[i][y] == '.':
                break
        pypan[0][y] = '.'
    return pypan


while True:
    q = deque([])
    visit = [[False]*6 for _ in range(12)]
    delList = []

    for i in range(11, -1, -1):
        for j in range(6):
            dlist = []
            cnt = 1

            if pypy[i][j] != '.' and not visit[i][j]:
                q.append([i,j])
                dlist= [[i,j]]
                visit[i][j] = True

                while q:
                    x, y = q.popleft()
                    for d in dir:
                        nx, ny = x+d[0], y+d[1]
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visit[nx][ny] and pypy[nx][ny] == pypy[x][y]:
                            q.append([nx, ny])
                            dlist.append([nx, ny])
                            visit[nx][ny] = True
                            cnt += 1
                
                #바운더리마다 bfs 수행하고 삭제할 리스트 더해줌
                if cnt >= 4:
                    delList.extend(dlist)

    #한바퀴 돌면 삭제하고 판 갱신
    if delList: 
        pypy = delPY(pypy, delList)
        answer += 1
    #판 갱신할게 없으면 반복문 나오기
    else:
        break

print(answer)
