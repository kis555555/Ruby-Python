puts("아이디를 입력해주세요")
input_id = gets.chomp()
puts("비밀번호를 입력해주세요")
input_pw = gets.chomp()

id_DDang = "DDang"
pw_DDang = "1234"


if input_id == id_DDang and input_pw == pw_DDang
    puts("Hello! " + id_DDang)
else
    puts("로그인 실패")
end