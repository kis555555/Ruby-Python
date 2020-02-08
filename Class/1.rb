class Cal #루비는 무조건 대문자로 시작
    def initialize(v1,v2) #initialize는 생성자를 만드는 작업을 함 
        # @를 통해서 매개변수 값을 받아줘야함. @v1(인스턴스 변수)
        @v1 = v1 # @가 없는 v1는 지역변수임
        @v2 = v2
    end

    def add()
        return @v1+@v2
    end
    
    def subtract()
        return @v1-@v2
    end
end

c1 = Cal.new(10,10)
p(c1.add()) #p 또한 puts와 같은 출력 함수임
p(c1.subtract())

c2 = Cal.new(30,20)
p(c2.add())
p(c2.subtract())