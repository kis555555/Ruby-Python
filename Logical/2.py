input_id = input("아이디를 입력해주세요.\n")
id_DDangNon = "DDangNon"
input_pw = input("비밀번호를 입력해주세요.\n")
pw_DDangNon = "1234"

if id_DDangNon == input_id and input_pw == pw_DDangNon : 
    print("Hello! " + id_DDangNon)
else :
    print("로그인 실패")