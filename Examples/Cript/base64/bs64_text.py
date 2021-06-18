import base64

txt = "Test message!"
print("Начальная фраза:", txt, "\n")

# Кодирование
# .encode() Преобразование в byte
bs16enc = base64.b16encode(txt.encode())
bs32enc = base64.b32encode(txt.encode())
bs64enc = base64.b64encode(txt.encode())

print("utf-8 > bs16:", bs16enc)
print("utf-8 > bs32:", bs32enc)
print("utf-8 > bs64:", bs64enc)

# Декодирование
# .decode() преобразование из byte в utf-8
bs16decode = base64.b16decode(bs16enc).decode()
bs32decode = base64.b32decode(bs32enc).decode()
bs64decode = base64.b64decode(bs64enc).decode()

print("bs16 > utf-8:", bs16decode)
print("bs32 > utf-8:", bs32decode)
print("bs64 > utf-8:", bs64decode)
