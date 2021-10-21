# Q. 16236
#백준 아기상어
from collections import deque
import sys
from pprint import pprint

input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, weight, time, eat):
    q, can_eat = deque(), []
    q.append([x, y])
    c = [[-1]*n for _ in range(n)]  # -1로 채워진 N*N 2차원 배열
    c[x][y] = time  # 초기값 0
    while q:
        qlen = len(q)
        while qlen:  # q의 길이 만큼 while 문 반복
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if c[nx][ny] == -1:  # not visited!
                        if a[nx][ny] == 0 or a[nx][ny] == weight:  # 지나만 갈 수 있는 칸!
                            c[nx][ny] = c[x][y] + 1  # 이동하는 데 1초 걸려서 -> +1초
                            q.append([nx, ny])  # 이동한 칸
                        elif 0 < a[nx][ny] < weight:  # 먹을 수 있는!
                            can_eat.append([nx, ny])
            qlen -= 1

        if can_eat:
            nx, ny = min(can_eat)
            eat += 1
            if eat == weight:  # 상어 레벨업
                eat = 0
                weight += 1  # 상어 크기 + 1
            a[nx][ny] = 0
            return nx, ny, weight, c[x][y] + 1, eat
        
    pprint(a)
    pprint(c)
    print('--------------------')

    print(time)
    sys.exit()

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            a[i][j] = 0

weight, time, eat = 2, 0, 0
while True:
    x, y, weight, time, eat = bfs(x, y, weight, time, eat)