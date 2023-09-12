# seat = [0] * 10
# money = 0
# while True:
#     sel = int(input("[1]예매하기 [2]종료하기 : "))
#     if sel == 1:
#         c = int(input("좌석 선택(1~10) : "))
#         if 10 >= c > 0:
#             if  seat[c-1] == 0:
#                 seat[c-1] = 1
#                 money += 12000
#                 print(seat)
#             else :
#                 print("좌석이 이미 존재합니다")
#     else : break
# print(f"좌석 : {seat}, 총 판매액 : {money}")

TICKET_PRICE = 12000
seat = [0] * 10

# 좌석 상태를 표시하는 메뉴 함수
def print_seat():
    for e in seat : # 향상된 for 문으로 좌석의 개수 만큼 순회
        if e == 0 : print("[ ]", end=" ")   # 판매안된 좌석
        else: print("[V]", end=" ")   # 판매된 좌석
    print()
# 총매출액 구하기
def amount():
    cnt = 0
    for e in seat:
        if e == 1 : cnt += 1    # 팔린 좌석의 총 개수 구하기
    return cnt * TICKET_PRICE
def select_seat():
    print_seat()    # 현재 예약 가능한 좌석 보여 주기
    num = int(input("좌석 번호를 선택하세요 : ")) - 1     # 선택된 죄석번호는 1부터 시작하고 인덱스는 0 부터 시작하기 떄문에 -1
    if seat[num] == 0 :
        seat[num] = 1
        print_seat()
    else: print("이미 예약된 좌석 입니다.")

while True :
    sel = int(input("[1]예매하기 [2]종료하기 : "))
    if sel == 1 : select_seat()
    else :
        print(f"총 매출액 : {amount()}원")
        break