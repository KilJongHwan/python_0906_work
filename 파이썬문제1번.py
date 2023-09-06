# 1. 정해진 형식으로 시간을 입력 받아서 출력하기
# 입력 형식 : 22:5:5 => 오후 10시 05분 05초

# hour, min, second = map(int ,input("시:분:초 입력 : ").split(":"))
# if(hour > 12):
#     hour -= 12
#     print(f"오후 {hour}시 {min}분 {second}초 입니다.")
# else:
#     print(f"오전 {hour}시 {min}분 {second}초 입니다.")
# # 2. 세 개의 정수를 받아서 최대값과 최소값 구하기
# num1,num2,num3 = map(int,input("3개의 정수 입력 : ").split())
# print(f"최대값 : {max(num1,num2,num3)}")
# print(f"최소값 : {min(num1,num2,num3)}")

# 3. 주민등록번호를 입력받아 생년월일, 성별 ,나이 출력하기
# 999999-1234567

from datetime import datetime
current_year = datetime.today().year
jumin = input("주민등록 번호를 입력하세요 : ").split("-")
birth = jumin[0][:6]
if jumin[1][0] == "1" or jumin[1][0] == "3": sex = "남성"
else: sex = "여성"
age = int(birth[:2])
current_year -= 2000
if (current_year - age) < 0: age = current_year + (100 - age)
else : age = (current_year - age)
print(f"""
생년월일 : {birth}
성별 : {sex}
나이 : {age}
""")

# 4. 갯수가 정해지지 않은 여러 개의 정수를 입력 받아 합계와 평균구하기
# list 사용

# list = list(map(int,input("값을 입력 하세요 : ").split()))
# sumList = sum(list)
# avList = sumList / len(list)
# print(f"합계 : {sumList}")
# print(f"평균 : {avList:.2f}")
