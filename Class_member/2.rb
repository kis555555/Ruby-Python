class Cs
    def Cs.class_method() #클래스 메소드를 사용 할려면 클래스 명을 써야함.
        p("Class method")
    end
    def instance_method() # 인스턴스의 소속으로 사용
        p("Instance method")
    end
end

i = Cs.new()
Cs.class_method()
i.instance_method()

# i.class_method() 에러가 뜬다. 
# Cs.instance_method() 에러가 뜬다.