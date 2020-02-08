class Cal(object) :
    _history = [] # 여태 계산한 식들을 저장할 배열
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
        result = self.v1 + self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1,self.v2,result))
        return result
    def subtract(self) :
        result = self.v2 - self.v2
        Cal._history.append("sub : %d-%d=%d" % (self.v1,self.v2,result))
        return result
    @classmethod
    def history(cls) :
        for item in Cal._history :
            print(item)
    def info(self) :
        return "Cal => v1 : %d, v2 : %d" %(self.v1,self.v2)

class CalMultiply(Cal) : #CalMultiply는 생성자가 없기 때문에 부모에게 생성자가 있는지 체크함
    def multiply(self) :
        result = self.v1 * self.v2
        Cal._history.append("mul : %d*%d=%d" %(self.v1,self.v2,result))
        return result
    def info(self) :
        return "Calmultiply => %s" % super().info() #super().info() 는 문자열로 출력되므로 %s를 해줌
class CalDivide(CalMultiply) :
    def divide(self) :
        result = self.v1 / self.v2
        Cal._history.append("divide : %d/%d=%d" %(self.v1,self.v2,result))
        return result
    def info(self) :
        return "Caldivide => %s" % super().info()

c0 = Cal(30,60)
print(c0.info())
c1 = CalMultiply(10,10)
print(c1.info()) # c1은 info()가 없으므로 부모가 가진 info를 호출
c2 = CalDivide(20,40)
print(c2.info())

Cal.history()