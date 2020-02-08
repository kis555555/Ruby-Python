class C 
    def initialize(v)
        @value = v
    end
    def show()
        p(@value)
    end
    def getValue()
        return @value
    end
    def setValue(v)
        @value = v
    end
end

c1 = C.new(10) #루비에서는 외부에서 인스턴스 변수 접근 불가능
p(c1.getValue())
c1.setValue(20)
c1.show()