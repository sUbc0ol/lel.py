
        
import base64

payload  = '\x2b\x0d\x06\x3c\x2d\x39\x1e\x3d'
payload += '\x2f\x77\x1a\x3c\x07\x0f\x05\x38'
payload += '\x15\x05\x34\x37\x17\x31\x0c\x39'
payload += '\x28'  '\x17\x15\x38\x08'  '\x14'
payload += '\x0d\x27\x0e\x1f\x79\x3c\x35\x7c'
payload += '\x36\x20\x27\x1c\x2f\x35\x07\x1f'
payload += '\x37\x2d\x2b'      '\x1a\x05\x2b'
payload += '\x01\x29'  '\x34\x78'  '\x01\x2d'
payload += '\x2b'  '\x31\x29\x00\x2f'  '\x25'
payload += '\x1d\x04\x2b\x7c\x1a\x23\x2a\x78'
payload += '\x0a\x25\x0b\x2f\x29\x0b\x0e\x7f'
payload += '\x1b\x25\x2f\x05'

key = "HELLOWORLDHELLOWORLDu" * 4
assert len(payload) == len(key)

code = ''
for p, k in zip(payload, key):
    code += chr(ord(p) ^ ord(k))

print("base64 encoded", code)
code = base64.b64decode(code)

print("after decoding", code)
eval(code)


# code: b'print(str("hello".upper().lower()),str("\\x77\\x6f\\x72\\x6c\\x64"))'

# simplified:        'w' 'o' 'r' 'l' 'd'
print("hello", str("\x77\x6f\x72\x6c\x64"))        
