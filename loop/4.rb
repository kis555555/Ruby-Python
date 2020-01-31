puts("아이디를 입력하세요")
input_id = gets.chomp()
#real_DDang = "DDang"
#real_Non = "Non"
members = ['DDangNon','Non','bloger','test']

for member in members do
    if member == input_id 
        puts("Hello " + member)
        exit
    end
end
puts("Who are you?")    



#if real_DDang == in_str :
#    print("Hello, DDang")
#elif real_Non == in_str :
#    print("Hello, Non")
#else :
#    print("Who are you?")