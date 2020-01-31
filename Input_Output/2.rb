puts("아이디를 입력해주세요")
input = gets.chomp()
input_DDang = "22"
real_Non = "abc"


if input == input_DDang
    puts("Hello!, DDang")
elsif(real_Non == input)
    puts("Hello! Non")
else
    puts("Who are you")
end