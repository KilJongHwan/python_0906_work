# 1번 문제 : 세자리 정수를 입력 받은 후 가장 큰 수 찾기 (123 = 3)
a = int(input("세자리 정수 입력 : "))
hundrad = a / 100
one = (a % 10)
ten = ((a % 100) / 10) - one
print(f"가장 큰 수는 = {int(max(one,ten,hundrad))} 입니다.")

# 2번 문제 : 주/야간 근무 시간을 입력받아 아르바이트 급여 계산하기
# 주간 근무 : 9620원
# 야간 근무 : 주간 시급 * 1.5
# 근무 시간 [1]주간 [2]야간:
# 근무 시간 입력 :
# 입력한 시간 동안 근무한 주간 또는 야간 급여 ___원 입니다.
sel = int(input("근무 형태를 입력하세요 [1]주간근무 [2]야간근무 : "))
time = int(input("근무 시간을 입력 하세요 : "))
if sel == 1:
    pay = 9620
else:
    pay = 9620 * 1.5
timeStr = sel == 1 and "주간" or "야간"
print(f"입력한 {timeStr} 시간급여는 {int(time * pay)}원 입니다.")

# 3번 문제 : 문자열 추가하기
# 2개의 문자열을 포인터 변수 s 와 k에 임의 정수를 정수형 변수 n에 각각 전달 받아 뒤부분의 n개 문자열 k 문자열 끼워 넣는 코드 작성
# s : seoul
# k : korea
# m : 2
# 결과 : ulkorea

s,k = input("문자열 2개 입력 : ").split()
m = int(input("끼워 넣을 문자열 개수 입력 : "))
insert = s[-m:]
print(f"끼어넣은 결과는 {insert + k}입니다")
