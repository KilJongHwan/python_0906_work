# 세 개의 자연수 A, B, C가 주어질 때
# A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

n1 = int(input())
n2 = int(input())
n3 = int(input())
mul = n1 * n2 * n3
result = str(mul)
for i in range(ord("0"), ord("9") + 1):
    print(result.count(chr(i)))

# a,b,c = map(int,input().split())
# total_val = str(a * b * c)
# for i in range(10):
#     print(total_val.count(str(i)))

# 영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은
# 시간 통화를 했으면 10원이 청구된다.
# 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.
# 민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면
# 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.
# 동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면
# 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.
# 영식은 Y로, 민식은 M으로 출력한다.

# n = int(input())
# ySum = mSum = 0
#
# call = list(map(int, input().split()))
# for i in range(n):
#     ySum += (call[i] // 30) * 10 + 10
#     mSum += (call[i] // 60) * 15 + 15
#
# Y = 30
# M = 60
# for i in range(n):
#     t = int(input())
#     if t - Y > 0 : ySum += 10 * (t / Y)
#     if t - M > 0 : mSum += 15 * (t / M)
#     ySum += 10
#     mSum += 15
#
# if ySum > mSum : print(f"M {int(mSum)}")
# elif ySum < mSum: print(f"Y {int(ySum)}")
# else: print(f"YM {int(ySum)},{int(mSum)}")

# 대소문자 바꾸기
# rst = ""
# for e in input():   # 입력 받는 문자열 만큼 자동 출력
#     if e.islower():
#         rst += e.upper()
#     else:
#         rst += e.lower()
# print(rst)