def build(frame, x, y, type):
    if [x,y,type] not in frame: # 해당 구조물을 확인할 필요 없는 경우
        return True
    if type == 0 : #기둥 확인 과정
        if y == 0: # 바닥에 세운 기둥
            return True
        if [x-1, y, 1] in frame: #왼쪽 보 위에 올린 기둥
            return True
        if [x, y, 1] in frame: #오른쪽 보 위에 올린 기둥
            return True
        if [x, y-1, 0] in frame: # 기둥 위에 올린 기둥
            return True
    else: #보 확인과정
        if [x, y-1, 0] in frame: #왼쪽 기둥에 올린 보
            return True
        if [x+1, y-1, 0] in frame: # 오른쪽 기둥에 올린 보
            return True
        if [x-1, y, 1] in frame and [x+1, y, 1] in frame: # 양옆의 보 지지되는 보
            return True
    return False

def destroy(frame, x, y, type):
    if type == 0: #기둥 삭제할 경우 영향 받는 구조물 [x, y+1, 0], [x-1, y+1, 1], [x, y+1, 1]
        if build(frame, x, y+1, 0) and build(frame, x-1, y+1, 1) and build(frame, x, y+1, 1):
            return True
        else:
            return False
    else: #보 삭제할 때 영향 받는 구조물 [x, y, 0], [x+1, y, 0], [x-1, y, 1], [x+1, y, 1]
        if build(frame, x, y, 0) and build(frame, x+1, y, 0) and build(frame, x-1, y, 1) and build(frame, x+1, y, 1):
            return True
        else:
            return False


def solution(n, build_frame):
    answer = []

    for x, y, type, bType in build_frame:
        if bType == 0: # 삭제할 때
            if [x, y, type] in answer:
                answer.remove([x, y, type])
                if not destroy(answer, x, y, type):
                    answer.append([x, y, type])
        else: # 설치할 때
            answer.append([x, y, type])
            if not build(answer, x, y, type):
                answer.remove([x, y, type])

    answer.sort(key = lambda x :(x[0], x[1], x[2]))
    return answer

# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# n = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
# print(solution(n, build_frame))

build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
n = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]
print(solution(n, build_frame))