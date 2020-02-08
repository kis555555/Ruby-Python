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

class CalMultiply(Cal) : #CalMultiply는 생성자가 없기 때문에 부모에게 생성자가 있는지 체크함
    def multiply(self) :
        return self.v1 * self.v2
class CalDivide(CalMultiply) :
    def divide(self) :
        return self.v1 / self.v2

c1 = CalMultiply(10,10)
print(c1.add())
print(c1.multiply())

c2 = CalDivide(10,10)
print(c2.multiply())
print(c2.divide())