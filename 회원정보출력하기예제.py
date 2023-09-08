# 회원정보를 입력 받아서 출력 하는 예제 진행
# - 이름 입력
# - 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# - 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로 입력 받고 나머지는 재 입력 요청을 한다.
# - 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고 나머지는 재 입력 요청 한다.
# - 결과는 마지막에 한번에 출력 한다.
def input_age():
    while True:
        age = input("나이를 입력 하세요 : ")
        if age.isdigit():
            age = int(age)
            if 0 < age < 200: return age
        print("회원정보를 잘못 입력하셧습니다 다시 입력해주세요")


def input_sex():
    while True:
        sex = input("성별을 입력 하세요 : ")
        if sex == "m" or "M":
            return "male"
        elif sex == "f" or "F":
            return "female"
        else:
            print("회원정보를 잘못 입력하셧습니다 다시 입력해주세요")


def input_jobs():
    while True:
        job = input("직업을 입력 하세요 : ")
        if job.isdigit():
            job = int(job)
            if 0 < job < 5:
                return job
            else:
                print("회원정보를 잘못 입력하셧습니다 다시 입력해주세요")


def print_info(name,age,sex,job):
    job_str = "", "학생", "회사원", "주부", "무직"
    print("=" * 3, "회원 정보", "=" * 3)
    return  f" 이름 : {name} 나이 : {age} 성별 : {sex} 직업 : {job_str[job]}"


# 함수는 선언 이후 호출해야 동작
member_info = "member.txt"
fd = open(member_info, "wt",encoding="utf-8")
while True:
    name = input("이름을 입력하세요 : ")
    if name == "quit" : break
    age = input_age()
    sex = input_sex()
    job = input_jobs()
    rst = print_info(name,age,sex,job)
    fd.write(rst + "\n")
fd.close()
