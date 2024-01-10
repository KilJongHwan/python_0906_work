# 크기가 정해지지 않은 요소들에 대한 값을 저정하기 위한 자료형
# 아무 자료형이나 들어갈 수 있다.
# 중첩 사용이 가능하다 [[],[],[]],[[[]]]
# 뮤터블 객체(읽고,쓰기가 가능)
number = [1,2,3,4,5,6]
fruit = ["apple", "banana", "orange"]
mixed = [1,True,"seoul", 12.34]
dup = [[1,2,3,4,5], ["apple", "kiwi"]]

# # 변수와 리스트를 비교 해보기
# kor, eng, mat = map(int, input("성적 입력 : ").split())
# print(sum([kor,eng,mat]))
#
# # 리스트는 성적의 개슈에 상관없이 입력 받을 수 있음
# score = list(map(int, input("성적 입력 : ").split()))
# print(sum(score) / len(score))

str_name = ["seoul", "gangnam", "suwon","inchun"]
# 인덱싱
# print(str_name)     # 리스트 전체 출력
# print(str_name[1])  # 1번쨰 요소 출력
# print(str_name[1][2])  # 1번쨰 요소의 2번쨰 문자 출력
# #슬라이싱
# slice = str_name[1:3]  # 1번에서 3번 미만까지 잘라내기
# print(slice)
# print(len(slice[0]))

primes = [2,3,5,7]
print(primes[0])
print(primes[-1])
print(primes[-2:])

# 리스트 연산자 : 연결(+), 반복(*), len()
# list_a = [1,2,3]
# list_b = [4,5,6]
# print(list_a + list_b)
# print(list_a * 3)
# print(len(list_a + list_b))

# 리스트 요소 추가하기 : append() - 리스트의 맨 마지막에 추가, insert(index, 값) - 해당 인덱스에 값을 삽입
# list_a = [1,2,3]
# list_a.append(4)
# list_a.append(5)
# list_a.insert(1, 10)
# print(list_a)

# 리스트 제거하기 : pop(), remove()m clear(),del 리스트명[인덱스]
# pop() : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제, 인덱스가 있으면 해당 위치에 값을 삭제
# remove(값) : 해당하는 값을 제거, 만약 동일한 값이 여러개인 경우 낮은 인덱스값 제거
# clear() : 모든값을 삭제, 리스트를 지우지 않고 빈 리스트로 남긴다.
# list_all = [0,1,2,3,4,5,6,7,8,9, "a","b","c","d","korea"]
# print(list_all)
# print(list_all.pop(11)) # 해당하는 값을 삭제하면서 보여줌
# print(list_all.pop()) # 인덱스가 없으면 맨 마지막 요소 제거
# list_all.remove(2)  # 해당값을 제거하는데 보여주지 않는다(반환갑)
# print(list_all)
# del list_all[3] # 해당 인덱스의 값을 제거

# list_all.clear()
# print(list_all)

# 중복 제거
# my_list = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,1,2,3,4]
# new_list = []
# for e in my_list:
#     if e not in new_list: new_list.append(e)
# print(new_list)

# map(반환함수, 입력자료형), filter(반환함수, 입력자료형) 동작 확인
# num = list(filter(lambda e:int(e) % 2 == 0, input("값 : ").split()))
# print(num)

# 리스트의 원소 스캔하기
x = ["John", "George", "Paul", "Ringo"]
for e in x: # 향상된 for 문과 비슷한 영태
    print(e)
for i in range(len(x)): # 범위 기반 for 문 (초기값, 최종값, 증감값)
    print(x[i])

# map : 전달받은 값을 함수내부애서 가공해서 반환 (입력 개수와 반환 개수가 동일)
# filtew : 전달 받은 값을 함수 내부에서 조건이 일치하는 값 반환

import random
alist = list(map(int , input("무작위 숫자 입력 : ").split()))
odd = list(filter(lambda  e:e % 2 != 0, alist))
even = list(filter(lambda  e:e % 2 == 0, alist))

# for e in les :
#     if e % 2 == 0 : even.append(e)
#     else: odd.append(e)

print(even)
print(odd)