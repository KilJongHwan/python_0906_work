# 함수란 ? 특별한 목적을 수행하기 위해 독립적으로 설계된 프로그램

# 이름, 주소 , 전화번호를 매개변수로 전달받아서 출력하는 함수
def name_card(name, addr, phone):
    print(f"주소 : {addr}")
    print(f"전화번호 : {phone}")
    print(f"이름 : {name}")
    print(f"회사 : kh정보교육원")

# 함수는 선언 이후 호출 해야만 동작, 한번 만들어진 함수를 여러번 호출하여 반복되는 코드를 줄임
name_card("james", "newyork", "010-1234-5678")
name_card("kane", "london", "010-1234-0000")
name_card("kasumi", "tokyo", "010-1111-2222")
