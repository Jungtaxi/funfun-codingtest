# https://www.acmicpc.net/problem/3343
import sys
import math

input = sys.stdin.readline
# a개를 a_p원에 팔고, c개를 c_p원에 팔고
n, a, a_p, c, c_p = map(int, input().split())


def sol(n, a, a_p, c, c_p):
    # c는 효율적인 번들
    if a_p * c < c_p * a:
        a, a_p, c, c_p = c, c_p, a, a_p

    answer = float("inf")

    # i는 비효율적인 a번들 사는 개수
    # 비효율적인 번들을 c개 만큼 살 이유는 없음. 그때는 공배수라서 효율적 번들을 i개 사면 됨.
    for i in range(c):
        # j는 효율적인 c번들 사는 개수
        j = math.ceil((n - i * a) / c)

        # 비효율적 번들만으로 샀는데 N개를 넘어가는 경우 -> stop searching
        if j < 0:
            j = 0
            answer = min(answer, i * a_p + j * c_p)
            break

        answer = min(answer, i * a_p + j * c_p)
    return answer


print(sol(n, a, a_p, c, c_p))
