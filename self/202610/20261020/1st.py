import base64

cipher = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

raw_bytes = bytes.fromhex(cipher)

print(raw_bytes)

base64_bytes = base64.b64encode(raw_bytes)

print(base64_bytes)