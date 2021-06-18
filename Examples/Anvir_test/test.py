"""
Создает тестовый текстовый файл опредяляемый антивирусами как вирус!
"""
str1 = """X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-"""
str2 = "STANDARD-ANTIVIRUS-TEST-FILE!"
str3 = "$H+H*"

with open("test.txt", "w") as f:
    f.write(str1 + str2 + str3)
