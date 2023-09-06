# 파이썬의 다양한 출력 방법
name = "james"
age = 20
gender = "male"
jobs = "Software Developer"
addr = "NewYork city"

# C 언어 스타일 : 서식지정자를 사용하는 방식
print("="*5,"C Style", "="*5)
print("Name : %s" % (name))
print("Age : %d"% (age))
print("Gender : %s"% (gender))
print("Job : %s"% (jobs))
print("Address : %s"% (addr))
# Python 스타일 : 3.6 이전 방식
print("="*5,"Python Style", "="*5)
print("Name & Address : {} , {}".format(name, addr))
print("Age : {}".format(age))
print("Gender : {}".format(gender))
# Python 스타일 : 3.6 이후 방식, f와 {} 사용해서 출력 방식
print("="*5,"Python Current Style", "="*5)
print(f"Name : {name}")
print(f"Age : {age}, Gender : {gender}, Job : {jobs}")
# Java 스타일 : 문자열 연결 방법 (+)
print("="*5,"Java Style", "="*5)
print("Name : " + name)
print("Age : " + str(age))
print("Address : " + addr)


