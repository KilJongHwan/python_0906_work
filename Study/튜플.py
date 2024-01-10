# 튜플이란 ? 변경할 수 없는 시퀀스 자료형 (나머지는 리스트와 동일)
# 튜플의 정의 ()괄호를 사용하거나 생략 할 수 있음

# 튜플 만들기
person = "james", 20 , "New york"
# print(person)

# 튜플 요소 접근 하기
# print(person[0])
# print(person[1])

# 튜플의 언패킹
name, age, addr = person
print(name)
print(age)
print(addr)

# 튜플의 언패킹 기능을 이용한 함수 만들기
def get_person():
    name = "kane"
    age = 23
    addr = "London"
    return name, age, addr

result = get_person()   # 언패킹되서 전달되는 반환값을 패킹해서 받음
print(result)

a,b,c = get_person()
print(a,b,c)

tp = 1,1,2,2,2,3,3,3,3
print(tp.count(3))  # 매개변수로 전달한 변수가 몇번 나오는지 확인 하는 함수
print(tp.index(2))  # 매개변수로 전달한 변수의 시작 인댁스 반환
print(len(tp))
# 튜플에서 안되는 것 (immutable 특성이기 때문에 삭제 할 수 없음
# del tp[0]