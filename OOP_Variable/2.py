class C(object) :
    def __init__(self, v) :
        self.value = v
    def show(self) :
        print(self.value)
    def setValue(self, v) :
        self.value = v
    def getValue(self) :
        return self.value

c1 = C(10)
print(c1.getValue()) #함수 밖에서 인스턴스 변수 접근이 가능
c1.setValue(20)
print(c1.getValue())
c1.show()