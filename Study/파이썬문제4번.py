# 배수 찾기 문제
n = int(input())
mullist = []
for i in range(6):
    mullist.append(int(input()))

for e in mullist:
    if e == 0 : continue
    if e % n == 0:
        print(f"{e} is  a multiple of {n}")
    else : print(f"{e} is NOT a multiple of {n}")

# n = int(input())
# ls = []
# while True:
#     x = (int(input()))
#     if x == 0 : break
#     ls.append(x)
# for e in ls :
#     if e % n == 0 : print(f"{e} is a multiple of {n}.")
#     else : print(f"{e} is NOT a multiple of {n}")

# 피타고라스 문제
alist = []
while True:
    angle = list(map(int, input().split(" ")))
    n = max(angle)
    if n == 0 :
        break
    angle.remove(n)
    if pow(angle[0], 2) + pow(angle[1], 2) == pow(n, 2):
        alist.append("right")
    else: alist.append("wrong")
    if len(alist) >= 5:
        break
for e in alist:
    print(e)

# alist = []  # 결과를 출력하기 위한 빈 리스트
# while True:
#     ls = list(map(int, input().split()))
#     ls.sort()
#     if ls[0] == 0 and ls[1] == 0 and ls[2] == 0 : break
#     elif pow(ls[2],2) == pow(ls[0],2) + pow(ls[1],2):alist.append("right")
#     else : alist.append("wrong")
#
# for e in alist: print(e)

