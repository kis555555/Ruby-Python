class Cal(object) :
    def __init__(self,v1,v2) : #생성자 self는 생성한 인스턴스가 들어옴
        if isinstance(v1,int) :
            self.v1 = v1
        if isinstance(v2,int) :
            self.v2 = v2
    def setV1(self, v) :
        if isinstance(v,int) :
            self.v1 = v
    def getV1(self) :
        return self.v1
    def getValue(self) :
        return 
    def add(self) : # self 첫 번째에는 생성 인스턴스가 오고 이름은 마음대로 바꿔도 된다.
        return self.v1+self.v2
    def subtract(self) :
        return self.v1 - self.v2

c1 = Cal(10,10) #첫 번째 매개변수는 2번째, 두 번째 매개변수는 첫번째를 가리킴
print(c1.add())
print(c1.subtract())

c1.setV1('one')
c1.v2 = 30
print(c1.add())