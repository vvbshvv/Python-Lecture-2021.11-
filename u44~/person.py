class Person:    # 클래스
    def __init__(self, name, age, address='제주시 연동'):
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('안녕하세요. 저는 {self.name}입니다.')