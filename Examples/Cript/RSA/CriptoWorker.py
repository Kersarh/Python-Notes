import os
import pickle

from Crypto import Random
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

# pip install pycryptodome
# Python 3.9
# pycryptodome==3.10.1


class CriptoWorker:
    """
    Класс шифрования RSA. Надстройка над pycryptodome
    """

    def __init__(self) -> None:
        pass

    def createKey(self, savefolder: str = "keys", secret: str = None) -> dict:
        """Генерация пары RSA ключей

        Args:
            savefolder (str, optional): [Директория сохранения ключей]. Defaults to "keys".
            secret (str, optional): [Пароль приватного ключа]. Defaults to "secret".

        Returns:
            Dict: [Словарь из "private" и "public"]
        """

        # Проверяем есть ли папка куда сохраняем ключи если нет создаем
        if not os.path.exists(savefolder):
            os.makedirs(savefolder)

        # Генерируем пару ключей
        key = RSA.generate(2048)

        # Приватный ключ
        if secret:  # с паролем
            private_key = key.export_key(
                passphrase=secret, pkcs=8, protection="scryptAndAES128-CBC"
            )
        else:  # без пароля
            private_key = key.export_key("PEM")

        # Сохраняем приватный ключ
        private_file = f"{savefolder}\\private.pem"
        with open(private_file, "wb") as f:
            f.write(private_key)

        # Публичный ключ
        # Генерируем
        public_key = key.publickey().export_key("PEM")
        # записываем в файл
        public_file = f"{savefolder}\\public.pem"
        with open(public_file, "wb") as f:
            f.write(public_key)
        # Возвращаем список ключей
        result = {"private": private_key, "public": public_key}
        return result

    def createSignature(
        self,
        raw_message: bytes,
        aliseprivate: bytes,
        bobpublic: bytes,
        privatePwd: str = None,
    ) -> bytes:
        """Создает сигнатуру сообщения.

        Алиса подписывает сообщение своей цифровой подписью и шифрует ее открытым ключом Боба (асимметричным алгоритмом RSA).

        Args:
            raw_message (bytes): [Шифруемое сообщение]
            aliseprivate (bytes): [Приватный ключ отправителя]
            bobpublic (bytes): [Публичный ключ адресата]
            privatePwd (str, optional): [Пароль приватного ключа]. Defaults to None.

        Returns:
            bytes: [description]
        """
        plaintext = raw_message
        # Подписываем цифровой подписью Алисы
        privatekey = RSA.importKey(aliseprivate, passphrase=privatePwd)
        myhash = SHA.new(plaintext)
        signature = PKCS1_v1_5.new(privatekey)
        signature = signature.sign(myhash)
        # Шифруем сигнатуру ключом Боба
        publickey = RSA.importKey(bobpublic)
        cipherrsa = PKCS1_OAEP.new(publickey)
        sig = cipherrsa.encrypt(signature[:128])
        sig = sig + cipherrsa.encrypt(signature[128:])
        return bytes(sig)

    def checkSignature(
        self,
        message: dict,
        decript_message: bytes,
        bobprivate: bytes,
        alisepublic: bytes,
        privatePwd=None,
    ) -> bool:
        """Проверка сигнатуры.

        Боб расшифровывает и проверяет подпись Алисы.

        Args:
            message (dict): [Получаем сигнатуру из зашифрованного файла]
            decript_message (bytes): [Расшифрованное сообщение]
            bobprivate (bytes): [Приватный ключ получателя]
            alisepublic (bytes): [Публичный ключ отправителя]
            privatePwd (str, optional): [Пароль приватного ключа]. Defaults to None.

        Returns:
            bool: [True или False]
        """

        # Расшифровываем сигнатуру
        signature = message["Signature"]
        privatekey = RSA.importKey(bobprivate, passphrase=privatePwd)
        cipherrsa = PKCS1_OAEP.new(privatekey)
        sig = cipherrsa.decrypt(signature[:256])
        sig = sig + cipherrsa.decrypt(signature[256:])
        # Верификация
        plaintext = decript_message

        publickey = RSA.importKey(alisepublic)
        myhash = SHA.new(plaintext)
        signature = PKCS1_v1_5.new(publickey)
        test = signature.verify(myhash, sig)
        return test

    def createMsg(
        self, raw_message: bytes, aliseprivate: bytes, bobpublic: bytes, privatePwd=None
    ) -> dict:
        """Создание зашифрованного сообщения.

        Алиса генерирует случайный сеансовый ключ и шифрует этим ключом сообщение (с помощью симметричного алгоритма AES).
        Сеансовый ключ шифруется открытым ключом Боба (асимметричным алгоритмом RSA).

        Args:
            raw_message (bytes): [Сообщение для шифровки]
            aliseprivate (bytes): [Приватный ключ отправителя]
            bobpublic (bytes): [Публичный ключ получателя]
            privatePwd (str, optional): [Пароль приватного ключа]. Defaults to None.

        Returns:
            dict: [Словарь из "Data" - Сообщение, "Signature" - Сигнатуры, "Sessionkey" - Сессионного ключа]
        """

        plaintext = raw_message  # Данные которые будем шифровать
        # Получаем публичный ключ адресата
        publickey = RSA.importKey(bobpublic)
        cipherrsa = PKCS1_OAEP.new(publickey)

        # Создаем 256 bit сессионный ключ и шифру
        sessionkey = Random.new().read(32)  # 256 bit
        # Вектор
        iv = Random.new().read(16)  # 128 bit
        # Шифруем текст
        obj = AES.new(sessionkey, AES.MODE_CFB, iv)
        ciphertext = iv + obj.encrypt(plaintext)
        ciphertext = cipherrsa.encrypt(ciphertext)
        cript_message = bytes(ciphertext)  # Зашифрованное сообщение

        # Шифруем сессионный ключ
        sessionkey = cipherrsa.encrypt(sessionkey)
        sessionkey = bytes(sessionkey)  # Сессионный ключ

        # Создаем сигнатуру
        aliseprivate_key = RSA.importKey(aliseprivate, passphrase=privatePwd)
        signature = self.createSignature(
            raw_message, aliseprivate, bobpublic, privatePwd=privatePwd
        )

        result = {
            "Data": cript_message,
            "Signature": signature,
            "Sessionkey": sessionkey,
        }
        return result

    def decryptData(
        self, message: dict, bobprivate: bytes, alisepublic: bytes, privatePwd=None
    ) -> list:
        """Дешифрование данных.

        Боб расшифровывает сеансовый ключ своим приватным ключом.
        При помощи полученного, таким образом, сеансового ключа
        Боб расшифровывает зашифрованное сообщение Алисы
        и проверяет сигнатуру

        Args:
            message (dict): [Зашифрованный файл]
            bobprivate (bytes): [Приватный ключ получателя]
            alisepublic (bytes): [Публичный ключ отправителя]
            privatePwd (str, optional): [Пароль приватного ключа]. Defaults to None.

        Returns:
            list: [Список из расшифрованного сообщения и отметки верификации]
        """

        privatekey = RSA.importKey(bobprivate, passphrase=privatePwd)
        cipherrsa = PKCS1_OAEP.new(privatekey)
        # Расшифровка сеансового ключа
        sessionkey = message["Sessionkey"]
        sessionkey = cipherrsa.decrypt(sessionkey)

        # Расшифровка сообщения
        ciphertext = message["Data"]
        ciphertext = cipherrsa.decrypt(ciphertext)
        iv = ciphertext[:16]
        obj = AES.new(sessionkey, AES.MODE_CFB, iv)
        plaintext = obj.decrypt(ciphertext)
        plaintext = plaintext[16:]
        # Провека сигнатуры
        verification = self.checkSignature(
            message, plaintext, bobprivate, alisepublic, privatePwd=privatePwd
        )
        return [plaintext, verification]

    def saveMsgToFile(self, message: dict, file: str) -> None:
        with open(file, "wb") as f:
            pickle.dump(message, f)

    def readFileToMsg(self, file: str) -> None:
        with open(file, "rb") as f:
            data_new = pickle.load(f)
        return data_new


if __name__ == "__main__":
    message = "Тесовое сообщение".encode()
    cript = CriptoWorker()
    alise = cript.createKey("alise", secret="my_password")
    bob = cript.createKey("bob", secret="my_password")
    cripto_mes = cript.createMsg(
        message, alise["private"], bob["public"], privatePwd="my_password"
    )

    cript.saveMsgToFile(cripto_mes, "file.txt")
    a = cript.readFileToMsg("file.txt")
    print(cripto_mes == a)
    d = cript.decryptData(a, bob["private"], alise["public"], privatePwd="my_password")
    print(f"Сообщение: {d[0].decode()} \nВерификация: {d[1]}")
