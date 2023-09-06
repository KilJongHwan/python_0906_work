# 인덱싱과 슬라이싱

jumin = "901212-1234567"

gender = jumin[7] # 성별
year = jumin[:2]  # 출생년도
mon = jumin[2:4]  # 월, 2번 ~ 4번 인덱스
day = jumin[4:6]  # 일

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 : " + jumin[-7:])  # 맨 뒷자리가 -1

if gender == "1":
    print("남성 입니다.")
else:
    print("어성 입니다.")
a = "life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)
# a[1] = "L" # 문자열 요소는 읽을 순 있지만 변경은 불가능. 리터럴 상수

# 대소문자 바꾸기
aa ="Hello Python Program..."
bb = aa.upper()
print(bb)
print(bb.lower())

# 문자열 변경 : replace("")
input_str = "Hello Python Program..."
new_str = input_str.replace("Python", "JavaScript")
print(new_str)

# 문자열 포함된 문자 갯수 세기
input_str2 = "Hello Python Program"
print(input_str2.count("lo")) # 문자열에서 포함된 문자(열)의 갯수를 반환
print(len(input_str2))  # 문자열의 길이를 반환, 별도의 외부 함수를 사용하는 방식

test = [1,2,3,4,5,6,7,8,9,10]
print(f"리스트 길이 {len(test)}")

print(input_str2.__len__())   # 문자열애 포함된 내장 함수