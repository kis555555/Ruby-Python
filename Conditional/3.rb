input = 11
input_id = 22

real_pwd = "abc"
nick = "DDangNon"

if input == input_id
    puts("Hello!, " + nick)
else 
    if(real_pwd == input)
        puts("Hello!")
    else
        puts("Who are you")
    end
end