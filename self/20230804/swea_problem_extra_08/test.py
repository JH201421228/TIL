test_list_1st = [0,0,1,1,1,0,1,1,1]
test_list = [str(i) for i in test_list_1st]
test_list.insert(0,'0')
test_list.append('0')
test_str = ''.join(test_list)
print(test_str)
cnt = 0
start = 1
while True:
    index = test_str.find('01110', start)
    if index != -1:
        cnt += 1
        start += index + 1

    else:
        break

print(cnt)