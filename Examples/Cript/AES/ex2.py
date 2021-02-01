import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result = json.dumps({'iv': iv, 'ciphertext': ct})
    return result


def decrypt_message(json_input, key):
    """
    Дешифруем собщение
    """
    try:
        b64 = json.loads(json_input)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)

    except (ValueError, KeyError) as e:
        print("Decryption ERROR!\t>>>\t", e)


if __name__ == '__main__':
    data = "my secret data!"  # Сообщение
    key = generate_key()  # Генерируем ключ шифрования
    cr = encrypt_message(data, key)  # Шифруем сообщение
    print(cr)
    decr = decrypt_message(cr, key)  # Дешифруем сообщение
    print(decr)