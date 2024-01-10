# 함수란 ? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램

# 이름, 주소 , 전화번호를 매개변수로 전달받아서 출력하는 함수
# def name_card(name, addr, phone):
#     print(f"주소 : {addr}")
#     print(f"전화번호 : {phone}")
#     print(f"이름 : {name}")
#     print(f"회사 : kh정보교육원")
#
# # 함수는 선언 이후 호출 해야만 동작, 한번 만들어진 함수를 여러번 호출하여 반복되는 코드를 줄임
# name_card("james", "newyork", "010-1234-5678")
# name_card("kane", "london", "010-1234-0000")
# name_card("kasumi", "tokyo", "010-1111-2222")

# 순차 검색
# def search_list(a,x):
#     for i in range(len(a)):
#         if x == a[i] : return i
#     return -1
#
# v = [17, 92, 18, 33, 58, 7, 42]
# print(search_list(v,33))
# print(search_list(v,18))
# print(search_list(v, 100))

# 기본값 인자 : 함수 선언 시 매개변수에 대해서 기본값을 정의 할 수 있다.
# 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값 호출
# def profile(name, grade = 2, age = 18, school = "VictimHighSchool"):
#     print(f"Name : {name}, School : {school}, Grade : {grade}, Age : {age}")
#
# profile("james")
# profile("jessy")
# profile("kane",None,21)

# 가변 매개변수 : 변수의 개수가 정해지지 않은 경우에 사용
# *(Asterisk)를 붙여주면 함수의 매개변수를 몇개의를 입력하든 함수내에서 튜플로 인식
# def profile(name, age, *lang):
#     print(f"name : {name}, age : {age}", end=" ")
#     for e in lang:
#         print(e, end=" ")
#     print()
#
# profile("James", 18, "Python", "Java", "C", "C++", "REACT")
# profile("Kane", 30, "Python", "Java", "Swift")
# profile("Jessy", 25, "Java", "kotlin")

knife = 10  # 칼을 10자루 준비


def game(player):
    global knife
    knife -= player
    print(f"남아 있는 칼은 {knife} 자루")


player = int(input("경기에 참여 하는 학생이 몇명 입니까? : "))
game(player)
print(f"경기에 사용하고 남은 칼은 {knife} 입니다.")
