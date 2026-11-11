from pwn import xor


# temp1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# temp2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
# temp3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# temp4 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
temp1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
temp2 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
temp3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
temp4 = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

flag = xor(temp4, temp3, temp1)

print(flag)