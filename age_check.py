import os
sp =  []
fileName = "sample02.txt"
newFile = open("myfile2.txt", 'w',encoding='utf8')
def check(args):
    lines = args.readlines()
    for line in lines:
        sp = line.split(",")
        sp[1] = sp[1].strip()

        if int(sp[1]) >= 19:
            sp.append("성인")
        else:
            sp.append("미성년자")
        sp[2] += "\n"
        newFile.writelines("{}/{}/{}".format(sp[0], sp[1],sp[2]))
        print(sp)

if os.path.exists(fileName): # 파일이 같은 경로내에 있을경우 실행
    # encoding하지않으면 에러가 발생해서 추가하였음
    file = open(fileName, "r", encoding='utf8')
    check(file)
    file.close()
else: # 경로내에 없을경우 sample02파일을 재생성하고 작업을 실행하게끔 설정
    f = open(fileName, "w", encoding='utf8')
    f.writelines("김철수,40\n홍길동,12")
    print("sample02 파일이 생성되었습니다")

newFile.close()