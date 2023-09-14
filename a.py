
def coffee():
    menu = {"아이스 아메리카노" : 3000, "아메리카노" : 3000, "아이스 라떼" : 4000, "라떼" : 3500, "아이스크림" : 8000}

    ice_menu = {}
    hot_menu = {}

    for i,j in menu.items():
        if i[0:3] == "아이스":
            ice_menu[i] = j
        else:
            hot_menu[i] = j

    print("아이스 매뉴 : {}".format(ice_menu))
    print("hkt 매뉴 : {}".format(hot_menu))

def EndConnect(text):

    text2 = input("끝말을 이어주세요 ")
    while(text[-1] == text2[0]):
        text = input("끝말을 이어주세요")
    print("끝말이 다릅니다")

def maxmin(*args):
    n=0
    m=10000000
    for i in args:
        if n < i:
            n = i
        if m > i:
            m = i
    print(n)
    print(m)

 maxmin(3,50, 60, 100 , 34)
