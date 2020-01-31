arr  = [1,3,56,7,13,52]
arr.delete_if() do |item|
    item > 7 #item값이 7 보다 크면 delete_if함수는 그 값을 삭제함
end

puts(arr)