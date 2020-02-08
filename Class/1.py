class Cal(object) :
    def __init__(self,v1,v2) : #생성자 self는 생성한 인스턴스가 들어옴
        self.v1 = v1
        self.v2 = v2
    def add(self) : # self 첫 번째에는 생성 인스턴스가 오고 이름은 마음대로 바꿔도 된다.
        return self.v1+self.v2
    def subtract(self) :
        return self.v1 - self.v2

c1 = Cal(10,10) #첫 번째 매개변수는 2번째, 두 번째 매개변수는 첫번째를 가리킴
print(c1.add())
print(c1.subtract())

c2 = Cal(30,20)
print(c2.add())
print(c2.subtract())