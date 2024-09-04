# https://www.acmicpc.net/problem/6987

from sys import stdin
from itertools import combinations as cb


def solution(round):
    global ans
    if round == 15:
        ans = 1
        for sub in res:
            if sub.count(0) != 3: # 다 -1 
                ans = 0
                break
        return

    t1, t2 = game[round]
    for x, y in ((0, 2), (1, 1), (2, 0)): #
        if res[t1][x] > 0 and res[t2][y] > 0: #서로 매치되는 경우 숫자를 하나씩 줄이면서 경우의 수를 줄여나감
            res[t1][x] -= 1
            res[t2][y] -= 1
            solution(round + 1)
            res[t1][x] += 1
            res[t2][y] += 1


answer = []
game = list(cb(range(6), 2)) # 6개 국가가 서로 매치하는 경우의 수
# 백트래킹
for _ in range(4): # 4가지 결과가 주어짐
    data = list(map(int, stdin.readline().split()))
    res = [data[i:i + 3] for i in range(0, 16, 3)] # 3을 기준으로 리스트 나누어서 행렬 구성
    ans = 0
    solution(0)
    answer.append(ans)

print(*answer)