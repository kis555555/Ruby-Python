class C1 :
    def m(self) :
        return 'parent'

class C2(C1) : #C1 상속
    def m(self) : #부모 함수를 자식 클래스에서 재정의(오버라이드함)
        return super().m() + ' child'
        #super는 부모를 가리킴 즉 super().m()은 부모가 가진 m함수 parent를 의미함
    pass #비어있는 클래스를 사용하기 위함

o = C2()
print(o.m()) 