def check_adjacent(row):
    for col in range(row):
        if board[row] == board[col] or abs(board[row] - board[col]) == row - col:
            return False
    return True


def dfs(row):
    global answer
    if row == n:
        # print(board)
        answer += 1
    else:
        for col in range(n):  # 열 검사
            board[row] = col
            if check_adjacent(row):  # 대각선이거나 같은 행/열이 아닌 경우, 겹치지 않는 경우
                dfs(row + 1)  # 다음행 탐색


n = int(input())
board = [0] * n
answer = 0

dfs(0)  # row 0부터 탐색
print(answer)