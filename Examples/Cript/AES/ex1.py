# pip3 install cryptography

from cryptography.fernet import Fernet


def generate_key():
    """
    Создаем ключ и записываем в файл
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Загружаем ключ из директории
    """
    key = open("secret.key", "rb").read()
    return key


def encrypt_message(message):
    """
    Шифруем сообщение
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    return encrypted_message


def decrypt_message(msg):
    """
    Дешифруем собщение
    """

    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(msg)
    return decrypted_message


if __name__ == "__main__":
    data_for_cript = "My Secret Message!"
    cript_data = ""
    while True:
        a = input("\n1 - Шифрование: \n2 - Дешифрование:\n")
        if a == "1":
            generate_key()
            cript_data = encrypt_message(data_for_cript)
            print(">> Зашифровано: ", cript_data)
        elif a == "2":
            dec_msg = decrypt_message(cript_data)
            print("Расшифровано: ", dec_msg.decode())
        elif a == "3":
            break
