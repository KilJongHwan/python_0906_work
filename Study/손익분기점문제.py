# 내가 푼 문제
a, b, c = map(int, input().split())
if c - b == 0: print(-1)
else:
    cost = a / (c - b) + 1
    if cost < 0:
        cost = -1
    print(int(cost))

# fix, var, sell = map(int, input().split())
# if sell <= var: print(-1)
# else : print(fix // (sell - var)+1)