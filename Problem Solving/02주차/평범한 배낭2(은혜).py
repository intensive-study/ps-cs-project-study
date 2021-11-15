# 평범한 배낭1처럼 풀어서 2차원 DP 테이블에 K개 물건 입력받으면 시간초과
# 어떤 물건이 4개 존재하고 가치가 3이라면, 이를 가치 3, 6, 12, 24를 가지는 상품으로 분할
# 하나씩만 있는 상품으로 바꾼다. 시간복잡도 O(MNlog(K)), N = 물건의 개수, M = 가능한 최대무게

# https://thsd-stjd.tistory.com/m/83 링크
# for (int j = 0; count > 0; j++) {		// 비트마스크로 저장
#     int tmp = Math.min(1 << j, count);
#     int curWeight = weight * tmp;
#     int curHappy = happy * tmp;
#     product.add(new int[] { curWeight, curHappy });
#     count -= tmp; # 7개의 물건이 있으면 1(1) 10(2) 100(4)번의 조합으로 7개까지 만들수 있음
# } -> 쪼개진 물품을 기존 문제처럼 풀이

N, M = map(int, input().split())
queue = []

for _ in range(N):
    w, v, qtt = map(int, input().split())
    exp = 0
    while qtt > 0:
        tmp = min(1 << exp, qtt)
        queue.append((w * tmp, v * tmp)) #수량 tmp(이진수의 각자리수) 배한 물품을 추가
        qtt -= tmp
        exp += 1

dp = [[0] * (M + 1) for _ in range(len(queue) + 1)]

for i, (w, v) in enumerate(queue): 
    for j in range(1, M + 1):
        if j < w:
            #해당 물품이 배낭 제한 무게보다 클 때 이전 행 참고
            dp[i + 1][j] = dp[i][j]
        else :
            #배낭에 들어갈 무게라면, 이전 행 값과 새로 들어간 물품과의 조합을 확인 
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
# print(dp)
# print(M, queue)
print(dp[len(queue)][M])