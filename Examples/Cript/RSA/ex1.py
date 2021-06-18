# pip install rsa
import rsa


def generate_key():
    """
    Создаем ключ и записываем в файл
    """
    pubkey, privkey = rsa.newkeys(512)
    return pubkey, privkey


def encrypt_message(message, pubkey):
    """
    Шифруем сообщение
    """
    return rsa.encrypt(message, pubkey)


def decrypt_message(message, privkey):
    """
    Дешифруем собщение
    """
    return rsa.decrypt(message, privkey).decode()


if __name__ == "__main__":
    message = b"my text"
    pubkey, privkey = generate_key()
    enc_msg = encrypt_message(message, pubkey)
    print("Зашифрованное сообщение: ", enc_msg)
    dec_msg = decrypt_message(enc_msg, privkey)
    print("Расшифрованное сообщение: ", dec_msg)
