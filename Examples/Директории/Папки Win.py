import os

a = os.getenv("APPDATA")
print(a)
w = os.getenv("WINDIR")
print(w)

#------------------------------


from win32com.shell import shell, shellcon
path = shell.SHGetFolderPath(0, shellcon.CSIDL_DESKTOP, None, 0)
print(path)

# shellcon.CSIDL_PROFILE — папка пользователя (C:\Users\username);
# shellcon.CSIDL_DESKTOP — рабочий стол (C:\Users\username\Desktop);
# shellcon.CSIDL_MYMUSIC — музыка (C:\Users\username\Music);
# shellcon.CSIDL_MYPICTURES — изображения (C:\Users\username\Pictures);
# shellcon.CSIDL_MYVIDEO — видео (C:\Users\username\Videos).