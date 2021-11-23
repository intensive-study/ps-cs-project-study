from collections import deque

N = int(input())
S = list(input())

q = deque()
hold = 0
left, right = 0, 0
alpha = [0 for _ in range(26)]
answer = 0

while True:
    if right == len(S):
        answer = max(answer, right-left)
        break
    
    if not right: #첫문자 넣어주기
        alpha[ord(S[right])-ord('a')] += 1
        hold += 1
        right += 1
        continue
    
    if alpha[ord(S[right])-ord('a')]:#이미 홀드된 문자
        alpha[ord(S[right])-ord('a')] += 1
        right += 1
        continue
        
    elif hold < N: # 더할 수 있는 경우
        alpha[ord(S[right])-ord('a')] += 1
        hold += 1
        right += 1
        continue

    else: #현재 가지고 있지 않는 문자면서 홀드 갯수를 넘어가는 경우
        #길이 확인 필요
        answer = max(answer, right-left)
        while left < right:
            alpha[ord(S[left])-ord('a')] -= 1
            if not alpha[ord(S[left])-ord('a')]: #다 비워졌으면
                left += 1
                break
            else:
                left += 1

        answer = max(answer, right-left)
        alpha[ord(S[right])-ord('a')] += 1
        right += 1

print(answer)

        


