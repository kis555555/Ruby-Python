name1 = String.new('DDang')
name2 = String.new('Non')
puts(name1.reverse())
puts(name2.reverse())
puts(name1.upcase())
puts(name1.size())

names = Array.new() # 배열 클래스에 대한 인스턴스가 만들어짐
names.push('DDang')
names.push('Non')
names.push('test')
puts(names)
puts(names.join('-')) #join은 naems 배열들을 () 안에 있는 놈으로 이어줌