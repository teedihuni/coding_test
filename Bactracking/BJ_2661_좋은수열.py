# https://www.acmicpc.net/problem/2661

import sys

input = sys.stdin.readline

def check(num):
    length = len(num)
    # 현재 수열 길이의 절반이 인접한 두개의 수열중 가장 긴 경우
    for idx in range(1, length//2 + 1):  # 절반까지만 살펴보면된다
        # 수열의 끝에서 i개의 부분 수열이 같다면 나쁜 수열
        if num[-idx:] == num[-(idx*2):-idx]:
            # 예를 들어 num = "123123" 일때
            # i = 1  / num[-1:] = '3' vs num[-2:-1] = '2'
            # i = 2  / num[-2:] = '23'  vs num[-4:-2] = '31'
            # i = 3  / num[-3:] = '123' vs num[-6:-3] = '123'
            return False
    else:
        return True

def backtracking(num): # 백트래킹
    global N
    if len(num) == N:
        print(''.join(map(str, num)))
        exit() # 최소값만 찾으면 끝남
    for i in range(1,4): 
        num.append(i)
        if check(num):
            backtracking(num)
        num.pop()
    return

N = int(input())
backtracking([1])
