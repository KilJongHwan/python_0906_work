# 회원 가입을 위한 아이디와 패스워드 입력 받기
user = input("아이디 입력 : ")
if len(user) >= 8 :  # 입력받은 아이디 길이가 10과 같거나 크다면
    pw = input("비밀번호 입력 : ")
    # if pw.__len__() < 8 or pw.__len__() > 16:
    if len(pw) < 8 or len(pw) > 16:
        print("비밀번호는 8자에서 16자 사이여야 합니다.")
    elif pw.find(user) >= 0:
        print("비밀번호에 아이디를 포함시킬수 없습니다.")
    else:
        print(f"아이디 : {user}")
        print(f"패스워드 : {pw}")
else:
    print("아이디는 반드시 8자리 이상이여야합니다.")