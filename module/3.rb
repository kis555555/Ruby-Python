require_relative('DDang') # python 에서는 import 루비에서는 require
#relative는 현재 디렉토리에서 DDang라는 파일을 불러옴
require_relative('Non')

puts(DDang.a())
puts(Non.b())