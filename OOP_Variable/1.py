class C :
    def __init__(self, v) :
        self.value = v
    def show(self) :
        print(self.value)

c1 = C(10)
print(c1.value) #함수 밖에서 인스턴스 변수 접근이 가능
c1.value = 20
print(c1.value)
c1.show()