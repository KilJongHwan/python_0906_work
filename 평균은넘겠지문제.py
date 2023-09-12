# 내가 푼 문제
def avr():
    cnt = 0
    array_list = list(map(int, input().split()))
    for e in array_list:
        if (sum(array_list) - array_list[0]) / (len(array_list) - 1) < e:
            cnt += 1
    average = cnt / (len(array_list) - 1) * 100
    return average

C = int(input())
alist = []
for i in range(C):
    alist.append(avr())
for e in alist:
    print(f"{e:.3f}%")

# def over_rate():  # 각 케이스에서 평균이 넘는 비율 구하기
#     ls = list(map(int, input().split()))  # 공백기준으로 입력 받아서 정수형 리스트로 받기
#     average = sum(ls[1:]) / len(ls[1:])  # list 멘앞의 요소 제외한 나머지 평균
#     cnt = 0  # 평균이 넘는 인원
#     for i in range(1, len(ls)):
#         if ls[i] > average : cnt += 1
#     return cnt / (len(ls) - 1) * 100  # 백분율 표기로 변경
#
# n = int(input()) # 총 테스트 개수
# rst = []    # 각 케이스에 대한 결과값 list
# for i in range(n):  # 총 테스트 개수 만큼 반복
#     rst.append(over_rate())
# for e in rst:
#     print(f"{e:.3f}%")