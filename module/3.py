#import DDang # a를 리턴하는 함수
import Non # b를 리턴하는 함수
from DDang import a  as z # DDang 이라는 모듈로부터 a라는 함수만 임폴트함(as z 하면 z로 함수명을 변경)

#print(DDang.a())
print(Non.a())

print(z()) # from 을 통해 특정 함수만 불러 올 시 a()로 사용하여야함