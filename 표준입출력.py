print(53) # 정수형
print("문자열") # 문자열
print([1,2,3]) # 리스트 형
print(1+3)
print("피"+ "이" + "썬") # 문자열 이어 붙이기
print("파""이""썬")
print("파","이","썬") # 콤마를 구분자 라고 부른다 기본적으로 한칸의 공백을 갖고 있음
print("파\n\n\n이\t\t썬")

print("안녕하세요 '누군가'가 인사했다")

# end 와 sep 옵션
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션 - \n
# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 - 기본은 space
print("Hello", end="$")
print("Hello", end= "*")
print("Hello")

print("life", "is", "too", "short", sep="\\")
print("010", "1234", "5678", sep="-")

year = 2023
month = 9
day = 6
print(year,month,day, sep="/")