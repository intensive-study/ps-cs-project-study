'''
테스트23 1646.72ms
'''
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y,1] in answer or [x,y-1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or([x-1,y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)

'''
테스트23 48.13ms
'''    
def isValid(answer):
    for x,y,a in answer:
        if a==0:
            if (x,y-1,0) in answer or (x-1,y,1) in answer or (x,y,1) in answer or y==0:
                continue
            else:
                return False
        if a==1:
            if (x,y-1,0) in answer or (x+1,y-1,0) in answer or ((x-1,y,1) in answer and (x+1,y,1) in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = set()
    for x,y,a,b in build_frame:
        if b==0:
            answer.remove((x,y,a))
            if not isValid(answer):
                answer.add((x,y,a))
        else:
            answer.add((x,y,a))
            if not isValid(answer):
                answer.remove((x,y,a))

    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer