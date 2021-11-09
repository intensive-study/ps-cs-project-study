def solution(s):
    answer = 1001
    n = len(s)
    for i in range(1, n+1):
        tmp = []
        lp = 0
        while lp < n:
            tmp += [s[lp:lp+i]] if lp+i < n else [s[lp:]]
            lp += i
        
        prev_s = '' if not tmp else tmp[0]
        new_s = ''
        cnt = 1
        for j in range(1, len(tmp)):
            if prev_s == tmp[j]: cnt += 1
            else:
                new_s = new_s + prev_s if cnt < 2 else new_s + str(cnt) + prev_s
                cnt = 1
                prev_s = tmp[j]
            
            if j == len(tmp) - 1: new_s = new_s + prev_s if cnt < 2 else new_s + str(cnt) + prev_s
                
        if not new_s: new_s = ''.join(tmp)
        answer = min(answer, len(new_s))

    return answer