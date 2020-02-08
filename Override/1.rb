class C1
    def m()
        return 'paernt'
    end
end

class C2 < C1
    def m()
        return super()+' child'
        #super()은 자식에서의 동일한 이름을 가진 함수를 부모클래스에서 찾음
    end
end

o = C2.new()
p(o.m())