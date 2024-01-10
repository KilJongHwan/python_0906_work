file_name = "스타벅스일일매출.txt"
f = open(file_name,'r',encoding="utf-8")
head = f.readline() # 파일의 첫 번째 줄을 읽음
head_list = head.split() # 메뉴명을 공백 기준으로 잘라서 리스트로 변환

espresso = []
americano = []
latte = []
cappuccino = []

for line in f: # f눈 파일 객체이며 파일의 읽는 위치를 가리키는 식별자, 두번째 라인 부터 반복 처리
    data_list = line.split() # 각각의 라인을 공백 기준으로 자름
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    latte.append(int(data_list[3]))
    cappuccino.append(int(data_list[4]))

f.close()

print(f"{head_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso) / len(espresso)}")
print(f"{head_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano) / len(americano)}")
print(f"{head_list[3]} 전체 판매량 : {sum(latte)}, 일 평균 판매량 : {sum(latte) / len(latte)}")
print(f"{head_list[4]} 전체 판매량 : {sum(cappuccino)}, 일 평균 판매량 : {sum(cappuccino) / len(cappuccino)}")