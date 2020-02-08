class C
    #attr_reader :value
    #attr_writer :value
    attr_accessor :value #reader, write 모두 허용
    def initialize(v)
        @value = v
    end
    def show()
        p(@value)
    end
end

c1 = C.new(10) #루비에서는 외부에서 인스턴스 변수 접근 불가능
p(c1.value)
c1.value = 20
p(c1.value)
#c1.setValue(20)
#c1.show()