class C 
    def initialize(v)
        @value = v
    end
    def show()
        p(@value)
    end
end

c1 = C.new(10) #루비에서는 외부에서 인스턴스 변수 접근 불가능
c1.show()