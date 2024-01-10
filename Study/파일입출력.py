# 파일 쓰기 : 파일을 읽거나 쓰기 위해서는 반드시 open() 해야함
# 파일 객체 = open(파일명, 파일모드,인코딩)
# 파일명 : 파일경로_파일명 (파일경로를 입력하지 않으면 현재 위치에 저장)
# 파일모드 : r(read),w(write),a(append), 파일이 없으면 생성하고 추가, 있으면 파일의 마지막에 추가
# score_file = open("score.txt",'w',encoding="utf-8")
# print("Math : 50",file=score_file)
# print("English : 90",file=score_file)
# score_file.write("Korean : 98" + "\n")
# score_file.write("Science : 45" + "\n")
# score_file.close()

# 파일 읽기
# read() : 파일내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() : 해당 파일의 내용을 한 라인씩 읽어 들여 문자열로 반환, 더이상 읽을 내용이 없으면 None 반환
# readlines() : 해당 파일의 모든 라인을 순서대로 읽어 각각의 라인을 하나의 요소로 저장하는 리스트를 반환
# score_file = open("score.txt",'r',encoding="utf-8")
# print(score_file.read())
# score_file.close()
# while True :
#     line = score_file.readline() # 한줄씩 읽음
#     if not line: break  # 더이상 읽을 라인이 없으면 None으로 확인되고 None은 거짓
#     print(line, end="") # 한줄씩 읽어서 출력하기 때문에 줄바꿈 문자가 포함되어 있음
# score_file.close()

# lines = score_file.readlines()  # 해당 파일 모든 라인 순서대로 읽어서 리스트 생성
# for e in lines:
#    print(e, end="")
# score_file.close()

# with 키워드 사용 하기 : open() 이후에 자동으로 close를 호출해주는 기능
# with open("score.txt",'r',encoding="utf-8") as score_file:
#     print(score_file.read())
#
# print("End Program")

import pickle
# # 객체를 직렬화하여 파일에 저장하기
# data = {"name" : "james", "age" : 23, "addr": "NewYork"}
# with open("data.pickle","wb") as file:
#     pickle.dump(data, file)

# 파일에서 객체를 역직렬화하여 복원하기
with open("data.pickle","rb") as file:
    restored_data =pickle.load(file)

print(restored_data)