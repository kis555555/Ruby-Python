class C(object) :
    def __init__(self, v) :
        self.__value = v #__value로하면 인스턴스 밖에서는 접근 불가
    def show(self) :
        print(self.__value)

c1 = C(10)

#print(c1.__value) #직접 접근은 불가능
c1.show() # 메소드를 통한 접근은 가능
