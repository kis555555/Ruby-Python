input_id = input("아이디를 입력해주세요 : ")

def login(_id) :
    members = ['DDangNon','Non','test']
    for member in members :
        if member == _id :
            return True
    return False

if login(input_id) :
    print('Hello ' + input_id)
else :
    print('who are you')