require('date') #데이터라는 클래스를 로드함.

d1 = Date.new(2000,1,1) # 2000년 1월 1일
d2 = Date.new(2010,1,1)

p(d1.year())
p(d2.year())

p(Date.today()) # 현재 날짜를 출력 해줌.