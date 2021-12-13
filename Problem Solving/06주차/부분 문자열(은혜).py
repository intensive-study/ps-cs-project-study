# KMP 이해 https://bowbowbow.tistory.com/6
# plist 생성 참고 https://devbull.xyz/python-kmp-algorijeumeuro-munjayeol-cajgi/

S = input()
P = input()

plist = [0 for _ in range(len(P))]
answer = 0 # 부분 문자열 아닌걸로 초기화

leng = 0 #이전까지 일치했던 문자열 위치
i = 1
while i < len(P):
    if P[i] == P[leng]: #그 다음 문자열이 일치할 경우
        leng += 1
        plist[i] = leng
        i += 1
    else: # 그 다음 문자열이 일치하지 않는 경우
        if leng == 0: #이전에 일치한 문자열 길이가 0일 경우
            plist[i] = 0
            i += 1
        else: #이전에는 일치한 문자열이 있는 경우 leng을 수정해 다시 확인
            leng = plist[i]

si = 0 #S 문자열 인덱스 위치   
pi = 0 #P 문자열 인덱스 위치
while si < len(S):
    if P[pi] == S[si]: # 문자가 일치하면 다음 문자 확인
        si += 1
        pi += 1
    elif pi != 0: #일치하지 않는 경우 pi가 0이 아니면 KMP 알고리즘 사용(plist에서 그 전 일치했던 문자열 넣어주기)
            pi = plist[pi-1]
    else: # 일치하지 않으면서 pi는 0이면 S의 인덱스만 다음으로 넘겨서 비교
        si += 1
    
    if pi == len(P): #pi가 끝까지 도달하면 일치하는 문자열이 있는 것.
        answer = 1
        break

print(answer)