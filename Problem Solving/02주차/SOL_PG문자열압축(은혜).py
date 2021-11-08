def solution(s):
    answer = len(s)
    
    #반복 주기 찾기
    for i in range(1, int(len(s) / 2) + 1) :
        tmp = s
        minlen = 0
        cnt = 0 #각 문자열 반복 횟수, 문자열이 바뀌면 아래에서 초기화
        while len(tmp) >= 2*i :
            if tmp[:i] == tmp[i:2*i] :
                cnt += 1 
                
            else : #비교할 문자열이 바뀔 예정
                minlen += len(str(cnt+1)) if cnt else 0
                #지금까지 반복된 숫자가 0이 아닐경우 숫자를 문자열에 더해줌 
                # ex) abcabcbbbbbb일 경우 2abcbbbbbb인 상태에서 2를 길이에 더해줌  
                minlen += i
                cnt = 0 
            
            tmp = tmp[i:]

            if len(tmp) < 2*i: # 반복문에서 빠져나갈 경우
                minlen += len(str(cnt+1)) if cnt else 0
                minlen += i + len(tmp[i:]) # 비교하지 못하는 나머지 문자열
                
        answer = min(answer, minlen)  
    
    return answer

print(solution("ababcdcdababcdcd"))

# print(solution("aabbaccc"))