# https://www.acmicpc.net/problem/1110
import sys

input = sys.stdin.readline


def colcul(n):
    """
    먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고,
    각 자리의 숫자를 더한다.
    주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의
    가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
    """
    return (n % 10) * 10 + (n // 10 + n % 10) % 10


N = int(input())
col = N
ans = 0
while ans == 0 or N != col:
    col = colcul(col)
    ans += 1
print(ans)
