class Cs
    @@count = 0
    def initialize()
        #@count 인스턴스에 속한 변수
        @@count = @@count + 1 #클래스에 속한 변수
    end
    def Cs.getCount() #밑에서 클래스로 호출하고 있으므로 Cs. 을 통해서 클래스로 만들어줌
        return @@count
    end
end

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()

p(Cs.getCount())