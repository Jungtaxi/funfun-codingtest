# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

input = sys.stdin.readline


def is_outside(coordi):
    if coordi[0] < 0 or coordi[0] >= n or coordi[1] < 0 or coordi[1] >= n:
        return True
    return False


def bfs(size, start):
    """
    아기 상어는 크기 2부터 시작
    """
    visited = [[0] * n for _ in range(n)]
    que = deque()
    que.append(start)
    res_time = 1e9
    res_coordis = []
    # visited에다가 time 기록 ( 1부터 넣어야 안되돌아감 )
    visited[start[0]][start[1]] = 1
    while que:
        x, y = que.popleft()

        # 더 먼 거리의 물고기면 통과
        if visited[x][y] - 1 > res_time:
            continue

        # 물고기를 먹으면 좌표 기록
        if graph[x][y] and graph[x][y] < size:
            # 물고기와의 최단 거리 업데이트
            res_time = visited[x][y] - 1
            res_coordis.append((x, y))

        for d in direct:
            nx, ny = x + d[0], y + d[1]
            # boder 체크
            if is_outside((nx, ny)):
                continue
            # visited 체크
            if visited[nx][ny]:
                continue
            # 문제 조건 (상어 보다 큰 물고기면 못지나감)
            if graph[nx][ny] > size:
                continue
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))
    # 다 돌았는데, 물고기가 없다면 time 0 기록
    if not res_coordis:
        return 0, (x, y)
    else:
        # 가장 위, 그리고 그 중에서도 왼쪽에 있는 물고기
        res_coordis.sort()
        graph[res_coordis[0][0]][res_coordis[0][1]] = 0
        return res_time, res_coordis[0]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
start = False
# find starting point
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start = (i, j)
            graph[i][j] = 0
            break
    if start:
        break

# 방향
direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]

ans = 0
size = 2
cnt = 0
t = -1
while t:
    t, coordi = bfs(size, start)
    cnt += 1
    ans += t
    start = coordi
    # 먹을 때마다 cnt 세서 물고기 몸집만큼 먹으면 사이즈 업
    if cnt == size:
        size += 1
        cnt = 0

if t == -1:
    print(0)
else:
    print(ans)


"""
거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 
그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
"""
