hex_code = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_code = bytes.fromhex(hex_code)

print(bytes_code)

for k in range(256):
    decoded = bytes([b ^ k for b in bytes_code])
    # print(decoded.decode("utf-8"))
    try:
        print(decoded.decode("utf-8"))
    except:
        print("sorry")