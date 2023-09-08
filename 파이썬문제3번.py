# 상근날드,
# price = list(map(int, input().split()))
# print(min(price) + min(price[0:2]) - 50)

# 저항
# s = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
# res = list(input().split())
# b = []
# for i in range(len(s)):
#     for j in range(len(res)):
#         if res[j] == s[i] :
#             b.append(str(i))
# c = b[-2] + b[-1]
# str 값을 직접 받아서 index를 구해서 풀이 방법
# color = "black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"
# print(int(c) * (10 ** int(b[-3])))
# f_name = color.index(input())  # input()으로 입력 받은 문자열이 color 튜플 내의 인덱스로 반환
# s_name = color.index(input())
# t_name = color.index(input())
# print(int(str(f_name) + str(s_name)) * (10 ** t_name))

# # pc방 알바
# n = list(map(int, input().split()))
# pc = [0] * 100
# cnt = 0
# for e in n : # 항상된 for 문으로 e 값을 고객이 요청한 좌석 번호
#     if pc[e-1] != 0 : cnt += 1
#     else: pc[e-1] = 1
# print(cnt)

# kmp 문제
# cap = ""
# for e in input(): # 입력 받는 갯수 자동 순회
#     if e.isupper() : cap += e
# print(cap)
