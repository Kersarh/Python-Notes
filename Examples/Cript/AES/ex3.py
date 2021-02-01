"""
Hежим EAX позволяет получателю обнаруживать любую несанкционированную модификацию.
В таком режиме на выходе не только зашифрованный текст,
а также MAC tag для проверки целостности. 
"""
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# pip install pycryptodome


def generate_key():
    """
    Создаем ключ и записываем в файл
    """
    return get_random_bytes(32)


def encrypt_message(msg, key):
    """
    Шифруем сообщение
    """
    data = msg.encode()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce
    return ciphertext, tag, nonce


def decrypt_message(msg, tag, nonce, key):
    """
    Дешифруем собщение
    """
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(msg, tag)
    return data.decode()


def encrypt_message_to_file(msg, key):
    """
    Шифруем сообщение
    """
    data = msg.encode()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    nonce = cipher.nonce

    # Сохраним данные в файл
    file_out = open("encrypted.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


def decrypt_message_to_file(key):
    """
    Дешифруем собщение
    """
    # Чтения из файла
    file_in = open("encrypted.bin", "rb")
    nonce, tag, msg = [file_in.read(x) for x in (16, 16, -1)]

    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(msg, tag)
    return data.decode()


if __name__ == '__main__':
    data = "my secret data!"  # Сообщение
    key = generate_key()  # Генерация ключа

    # Шифрование в программе
    cripto_text, tag, nonce = encrypt_message(data, key)
    dc = decrypt_message(cripto_text, tag, nonce, key)
    print("Сообщение: ", dc)

    # cripto_text - наше сообщение
    # tag - MAC (или тег)
    # nonce - произвольное число, которое используется только в криптографических связях.

    # Шифрование с сохранением в файл

    encrypt_message_to_file(data, key)
    dc_f = decrypt_message_to_file(key)
    print("Из файла: ", dc_f)
