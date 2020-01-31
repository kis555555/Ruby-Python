def f1()
    return 'f1'
end

puts(f1())

# 괄호 생략 가능
def f2
    return 'f2'
end

puts(f2())

def f3
    return 'f3'
end

puts(f3) #함수 호출시 괄호 또한 생략 가능

def f4(a1)
    return a1
end
puts(f4('f4'))

def f5 a1 # 매개변수 괄호 또한 생략 가능
    return a1
end
puts(f5('f5'))
puts(f5'f5') # 넘겨줄 값 또한 괄호 생략 가능
puts f5 'f5' #puts 또한 함수 이므로 생략 가능

def f6
    return 'f6'
end
puts f6

def f7 # return 값 없이도 사용 가능함.
    'f7'
end
puts f7

def f8
    a = 1
    b = 2
    a + b
end
puts f8