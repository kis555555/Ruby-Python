5.times() {puts 'times'} #5번 반복
2.times() {puts'2times'} #2번 반복
3.upto(5) {puts'3 to 5 uptp'}#3에서 5까지 숫자가 올라감 즉 3번 반복함
3.upto(5) {|i| puts(i)} # |i| 에 3~5까지 반복하면서 값을 넣어준다.

a = 6
a.upto(9) {|item| puts(item)}