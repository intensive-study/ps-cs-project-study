       
def chk(x) :
    for i in range(x):
        if chess[i] == chess[x]: # 위아래로 공격 가능
            return False
        if abs(chess[i] - chess[x]) == x - i: # 대각선 공격 가능
            return False
    return True # 공격받지 않는 위치

def dfs(x) :
    global rslt
    if x == n : # 마지막 행까지 도달하면 결과값 + 1
        rslt += 1
    else : 
        for i in range(n): 
            chess[x] = i
            if chk(x): #x번째 행의 i번째 열에 위치할 수 있는지 확인
                dfs(x+1)

n = int(input())
rslt = 0
chess = [0] * n #체스판 row
dfs(0)
print(rslt)
        