# 산술연산자 : 사칙 연산자(+,-,*,/) // (몫), ** (제곱 연산자), % (나머지 연산자)
i = 10  # 값을 대입할 때 형이 결정됨, 파이썬은 데이터 형이 없기에
j = 3
print(f"{i} + {j} = {i + j}")
print(f"{i} - {j} = {i - j}")
print(f"{i} * {j} = {i * j}")
print(f"{i} ** {j} = {i ** j}")
print(f"{i} / {j} = {i / j:.2}")
print(f"{i} // {j} = {i // j}")
print(f"{i} % {j} = {i % j}")

test = "Python"
print(test + " Hello")
print(test + str(100))
print(test * 3) # test 문자열 2번 반복
i += 1  # 파이썬은 증감 연산자가 없다
print(f"증감연산자 시험 : {i}")

# 간단 예제 : 파이썬은 변수를 상수로 만드는 방법은 없으며, 관례상 변수 이름을 모두 대문자로 표시하면 상수로 간주
TAX_RATE = (0.10)
#TAX_RATE[0] = 0.12
# income = int(input("당신의 수입을 입력 하세요 : "))
# print(f"당신이 내야 할 세금은 {income * TAX_RATE:.2f} 입니다")

# 관계 연산자 : AND(&&) => and, OR(||) => or, NOT(!) => not
x = 10
y = 20
z = 30
rst1 = x > 0 and x > y # False
rst2 = x > 0 or x > y # True
rst3 = not(x > 0 or x > y)

print(rst1,rst2,rst3,sep="\t")

# 다항(3항)연산자
num = int(input("정수 입력 : "))
rst = (num % 2 == 0) and "짝수" or "홀수" # e => (e % 2 == 0) and "짝수" or "홀수"
print(f"{num} 은 {rst}")

# 2진수 입력 받기 (0b)
number = 0b101010101
# 8진수 입력 받기
number = 0o1234567
# 16진수 입력 받기 (0123456789abcdef)
number = 0xffffff
