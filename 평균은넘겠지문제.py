def get_avr():
    avr = [0, ]
    n = 0
    T = int(input())
    for i in range(T):
        alist = list(map(int, input().split(" ")))
        avr[n] = sum(alist) / len(alist)
        if len(alist) >= T: n += 1
    return avr


avr_list = [0, ]
C = int(input())
for i in range(C):
    avr_list = get_avr()
print(avr_list)
