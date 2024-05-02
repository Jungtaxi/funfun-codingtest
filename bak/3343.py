# https://www.acmicpc.net/problem/3343
import sys
import math

input = sys.stdin.readline
# a개를 b원에 팔고, c개를 d원에 팔고
n, a, b, c, d = map(int, input().split())


# def get_lcm(x, y):
#     if x < y:
#         x, y = y, x
#     for i in range(x, x * y + 1):
#         if i % x == 0 and i % y == 0:
#             break
#     return i


def sol():
    if b / a == d / c:
        if a < c:
            return math.ceil(n / a) * b
        else:
            return math.ceil(n / c) * d
    elif b / a < d / c:
        effi_bundle, effi_price = a, b
        ineffi_bundle, ineffi_price = c, d
    else:
        effi_bundle, effi_price = c, d
        ineffi_bundle, ineffi_price = a, b

    ans = 0
    res = n % (effi_bundle * ineffi_bundle)
    ans += math.ceil((n - res) / effi_bundle) * effi_price

    min_cost = 1e9
    for i in range(math.ceil(res / effi_bundle) + 1):
        j = math.ceil((n - effi_bundle * i) / ineffi_bundle)
        if j < 0:
            j = 0
            cost = min(i * effi_price + j * ineffi_price, min_cost)
            break
        cost = min(i * effi_price + j * ineffi_price, min_cost)

    ans += cost
    return ans


print(sol() % (10**18))

"""
a와 b의 공배수에 대해서는 무조건 effi_bundle로 사는게 이득

ineffi_bundle로 사야할 때가 있을까?
=> effi_bundle로 살 경우, 불필요하게 물건을 추가 구입하는경우

그렇다면 구매는 어떻게 해야하냐.
공배수를 lcm이라고 할 때,

n = lcm * number + res

lcm * number에 대해서는 무조건 effi가 사야하고
res에 대해서는 브루트포스를 해야할 것 같음


가령 effi_bundle로만 구매했는데
res % effi_bundle 값이 크다면, 불필요한 소비가 될 가능성이 높다는 것

"""
