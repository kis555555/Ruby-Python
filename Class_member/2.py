class Cs :
    @staticmethod
    def static_method() :
        print("static method")
    @classmethod
    def class_method(cls) : # self처럼 cls 를 써줘야함.
        print("class method")
    def instance_method(self) : # 인스턴스는 self로 첫 번째 인자를 줘야함
        print("instance method")

i = Cs()
#클래스 멤버 메소드
Cs.static_method() 
Cs.class_method()

i.instance_method()