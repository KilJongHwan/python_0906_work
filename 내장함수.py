# 내장함수 : 파이썬이 기본적으로 제공, import가 필요 없음

# 큰값, 작은값 찾기
print(max(1,2,3,4,5,6,7,8,9,1235,246,346,75,347,345,374,34734,7347))
print(min(1,2,3,4,5,6,7,8,9,1235,246,346,75,347,345,374,34734,7347))

# 총합 구하기
print(sum([1,2,3,4,5,6,7,8,9,1235,246,346,75,347,345,374,34734,7347])) # 리스트에 대한 총힙
print(sum((1,2,3,4,5,6,7,8,9,1235,246,346,75,347,345,374,34734,7347))) # 튜플에 대한 총힙
# num = list(map(int, input("정수 값 입력 : ").split()))
# print(f"입력 받은 수의 총 합 : {sum(num)}")
# print(f"입력 받은 수의 총 합 : {sum(num)/len(num)}")

# 몫과 나머지 구하기
print(f"몫과 나머지 : {divmod(10, 4)}") # 튜플의 동작 원리, 두 개의 반환값으로 반환

# 여러개의 값을 한번에 입력받아 리스트로 만들기
# 최대값, 최소값 ,합계, 평균
# 합계에 몫과 나머지 : 5

# n = list(map(int, input().split()))
# print(f"최대값 : {max(n)}\n최소값 : {min(n)}\n합계{sum(n)}\n평균 : {sum(n) / len(n)}")
# print(f"몫과 나머지 : {divmod(sum(n), 5)}")

# 정렬
my_list = [62,34,75547,123,23,543,64,57,8695,34,5,7,345]
# 내림차순
print(sorted(my_list, reverse=True))
# 오름차순
print(sorted(my_list))