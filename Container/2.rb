al = ['A','B','C','D']
puts(al.length) # 배열의 길이

al.push('E') # 끝에 값 추가
print(al)
puts("")

al.delete('E') # 원소 이름을 통해서 삭제
print(al)
puts("")

al.delete_at(0) # 원소의 번호로 삭제
print(al)