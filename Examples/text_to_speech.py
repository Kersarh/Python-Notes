import requests
import pyglet
from pygame import mixer
import os

text_to_speech = "Тест tes2t"  # текст, который будет воспроизведён

# Запрос на яндекс
request = requests.get(
    "https://tts.voicetech.yandex.net/tts",
    params={
        "text": text_to_speech,
        "speaker": "alyss",
        "emotion": "evil",
        "format": "mp3",
    },
)

# Сохраняем ответ в файл
with open("foo.mp3", "wb") as file:
    file.write(request.content)
file.close()

# Проиграть файл и удалить его
mixer.init()
mixer.music.load("foo.mp3")
mixer.music.play()
# get_busy вернет False когда музыка прекратит проигрываться.
while mixer.music.get_busy():
    pass
mixer.stop()
mixer.quit()
os.remove("foo.mp3")

os.system(
    "pause"
    if os.name == "nt"
    else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'"""
)
