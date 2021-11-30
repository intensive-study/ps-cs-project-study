import sys

testcase = int(sys.stdin.readline())

for _ in range(testcase):
    
    N = int(sys.stdin.readline())
    adj = [0 for _ in range(N+1)]
    chk = [False for _ in range(N+1)]
    answer = 0
    
    for _ in range(N-1):
        root, child = map(int, sys.stdin.readline().split())
        adj[child] = root
    
    target1, target2 = map(int, sys.stdin.readline().split())
    
    chk[target1], chk[target2] = True, True     
    rt1, rt2 = adj[target1], adj[target2]
    
    while rt1 or rt2 :
        if rt1:
            if chk[rt1]:
                answer = rt1
                break
            else:
                chk[rt1] = True
                rt1 = adj[rt1]
        if rt2:
            if chk[rt2]:
                answer = rt2
                break
            else:
                chk[rt2] = True
                rt2 = adj[rt2]
                
    print(answer)
    
        