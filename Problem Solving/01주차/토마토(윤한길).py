from collections import deque
import sys
input = sys.stdin.readline


def check(l):
    for i in l:
        if 0 in i:
            return False  # 익지 않은 토마토 있음
    return True  # 토마도가 다 익은 상태


def find_ripe(l):
    tmp = []
    for i, v1 in enumerate(l):
        for j, v2 in enumerate(v1):
            if v2 == 1:
                tmp.append((i, j, 0))
    return tmp


def bfs(box, ripe_locations):
    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while ripe_locations:
        # print()
        v = ripe_locations.popleft()

        for i in range(6):
            nx = v[1] + dx[i]
            ny = v[0] + dy[i] + dz[i] * N  # 2차원으로 해결하기위해

            if i in [0, 1]:
                if 0 > ny >= N * H or v[0] // N != ny // N:
                    continue

            if 0 <= ny < N * H and 0 <= nx < M:  # 박스 범위 체크
                if box[ny][nx] not in [1, -1]:
                    box[ny][nx] = 1
                    ripe_locations.append((ny, nx, v[2] + 1))
                    # print((ny, nx, v[2] + 1))
    if 'v' in locals():
        return v[2]
    else:
        return


if __name__ == '__main__':
    answer = 0
    M, N, H = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N * H)]
    ripe_locations = deque(find_ripe(box))

    if check(box):
        print(0)
        # for i in box:
        #     for j in i:
        #         if j == 1:
        #             print(0)
        # else:
        #     print(-1)
    else:
        tmp = bfs(box, ripe_locations)
        if check(box):
            print(tmp)
        else:
            print(-1)
