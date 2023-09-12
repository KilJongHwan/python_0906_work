# 생성자는 클래스가 객체로 만들어 질 때 자동으로 호출되며, 객체의 초기값을 지정할 수 있다.
# 생성자 키워드 : __init__
# self : 자신의 객체를 가리키는 변수
class TV :
    def __init__(self, name, is_on, chanel, volume):
        self.name = name
        self.is_on = is_on
        self.chanel = chanel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_chanel(self, cnl):
        self.chanel = cnl
    def set_volume(self, vol):
        self.volume = vol
    def get_on(self):
        return self.is_on
    def get_chanel(self):
        return self.chanel
    def get_volume(self):
        return self.volume
    def view_tv(self):
        power = "OFF", "ON"
        print(f"Name : {self.name}")
        print(f"Power : {self.is_on}")
        print(f"Chanel : {self.chanel}")
        print(f"Volume : {self.volume}")

lg_tv = TV("LG", False, 10,10)
samsung_tv = TV("SAMSUNG", False, 20, 20)
lg_tv.view_tv()
samsung_tv.view_tv()