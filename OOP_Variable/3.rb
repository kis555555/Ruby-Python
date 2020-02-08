class Cal
    def initialize(v1,v2)
        @v1 = v1
        @v2 = v2
    end
    def add() 
        return @v1+@v2
    end

    def subtract()
        return @v1-@v2
    end
    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        end
    end
    def getV1(v)
        return @v1
    end
end

c1 = Cal.new(10,10)
c1.setV1('oo')
p(c1.add())