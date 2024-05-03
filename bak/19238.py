# https://www.acmicpc.net/problem/19238
import sys
from collections import deque

input = sys.stdin.readline


def isOutside(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return True
    return False


def bfs(s_x, s_y, fuel):
    visited = [[0] * n for _ in range(n)]
    que = deque()
    que.append((s_x, s_y))
    visited[s_x][s_y] = 1
    # 승객의 우선순위 고려 위해 최단 거리 기록 및 승객 리스트 기록
    min_dis = 1e9
    passengers = []

    while que:
        x, y = que.popleft()

        # 가는 길에 연료가 바닥난 경로
        if fuel - visited[x][y] + 1 < 0:
            continue

        # 승객인지 확인
        if grid[x][y] < 0:
            if not passengers or ((visited[x][y] - 1) <= min_dis):
                min_dis = visited[x][y] - 1
                passengers.append((x, y))
            # 해당 경로는 더 이상 탐색 안해도 됨.
            continue

        for d in direct:
            nx, ny = x + d[0], y + d[1]

            # border check
            if isOutside(nx, ny):
                continue
            # wall check
            if grid[nx][ny] == 1:
                continue
            # visited check
            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))

    # 중간에 연료가 바닥 났다면
    if not passengers:
        return -1, -1, -1, -1
    passengers.sort()

    # 다음에 태울 승객
    x, y = passengers[0]
    fuel -= visited[x][y] - 1
    passenger = -grid[x][y] - 1

    grid[x][y] = 0
    # 택시 좌표, 남은 연료, 승객 번호
    return x, y, fuel, passenger


def go_object(s_x, s_y, o_x, o_y, fuel):
    visited = [[0] * n for _ in range(n)]
    que = deque()
    que.append((s_x, s_y))
    visited[s_x][s_y] = 1

    while que:
        x, y = que.popleft()

        # 가는 길에 연료가 바닥난 경로
        if fuel - visited[x][y] + 1 < 0:
            continue

        # 도착지인지 확인
        if (o_x, o_y) == (x, y):
            fuel += visited[x][y] - 1
            return fuel

        for d in direct:
            nx, ny = x + d[0], y + d[1]

            # border check
            if isOutside(nx, ny):
                continue
            # wall check
            if grid[nx][ny] == 1:
                continue
            # visited check
            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))

    # 중간에 연료가 바닥 났다면
    return -1


# 행, 승객 수, 초기 연료
n, m, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
s_x, s_y = map(int, input().split())
s_x, s_y = s_x - 1, s_y - 1
objects = []
for i in range(1, m + 1):
    x, y, o_x, o_y = map(int, input().split())
    x, y, o_x, o_y = x - 1, y - 1, o_x - 1, o_y - 1
    grid[x][y] = -i
    objects.append((o_x, o_y))

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

answer = 0
x, y = s_x, s_y
for _ in range(m):
    x, y, fuel, passenger = bfs(x, y, fuel)
    if fuel < 0:
        answer = -1
        break
    o_x, o_y = objects[passenger]
    fuel = go_object(x, y, o_x, o_y, fuel)
    x, y = o_x, o_y
    if fuel < 0:
        answer = -1
        break
else:
    answer = fuel

print(answer)

"""
1. 도착지 가면, 소모한 연료의 두배 충전
2. 연료 바닥 시 영업 종료
3. 우선순위
    현재 위치에서 최단 거리 가장 짧은 승객
    행 번호가 가장 작은 승객
    열 번호가 가장 작은 승객
"""
