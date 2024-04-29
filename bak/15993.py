# https://www.acmicpc.net/problem/15993
import sys

dp = [(1, 0), (1, 1), (2, 2), (3, 4), (7, 6)]


def sol(num):
    if len(dp) >= num:
        return dp[num - 1]
    while len(dp) < num:
        even, odd = dp[-1][0] + dp[-2][0] + dp[-3][0], dp[-1][1] + dp[-2][1] + dp[-3][1]
        even %= 1000000009
        odd %= 1000000009
        dp.append((odd, even))
    return dp[num - 1]


input = sys.stdin.readline

t = int(input())
input_ = [int(input()) for _ in range(t)]
for n in input_:
    print(*sol(n))


"""
1                1 0
2                1 1
3                2 2
4                3 4
5                7 6

# num = 1
1       홀
# num = 2
1 1     짝
2       홀
# num = 3
1 1 1   홀
1 2     짝
2 1     짝
3       홀
# num = 4
1 1 1 1       1 1 1에 1이 붙음
1 1 2         1 1 에 2가 붙음
1 2 1         1 2 에 1이 붙음
2 1 1         2 1 에 1이 붙음
1 3           1에 3이 붙음
3 1           3에 1이 붙음
2 2           2에 1이 붙음

이전 3단계의 애들에다가 1 or 2 or 3을 붙여서 경우들이 만들어짐
1, 2, 3 더하기 문제라서 가능해진 케이스
만약 1, 2, 3, 4 더하기 문제라면 이전 4단계까지 더하면 됨.

"""
