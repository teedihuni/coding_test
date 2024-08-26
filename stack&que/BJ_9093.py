# 단어 뒤집기

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    case = list(str(input()).split(' '))
    result = ' '.join([text[::-1] for text in  case])
    print(result)

# 전체를 뒤집고 ' ' 를 기준으로 텍스트 순서만 뒤집는 방법도 있음.. 
# 이게 훨씬 빠르다
for _ in range(n):
    text = sys.stdin.readline()
    print(text[::-1])
    text_reversed = text[::-1].split()[::-1]
    print(' '.join(text_reversed))