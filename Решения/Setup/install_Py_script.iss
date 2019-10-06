; Этот сценарий создан с помощью Мастера Inno Setup.
; ОБРАТИТЕСЬ К СПРАВОЧНОЙ ДОКУМЕНТАЦИИ, ЧТОБЫ ИСПОЛЬЗОВАТЬ ВСЕ ВОЗМОЖНОСТИ INNO SETUP!

[Setup]
; Примечание: Значение AppId является уникальным идентификатором для этого приложения.
; Не используйте одно и тоже значение AppId для разных приложений.
; (Для создания нового значения GUID, выберите в меню "Инструменты" пункт "Создать GUID".)
AppId={{F5482354-0EA6-43C7-8CAD-4E5E665C1C37}
AppName=My Program
AppVersion=1.5
;AppVerName=My Program 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.wylek.ru/
AppSupportURL=http://www.wylek.ru/
AppUpdatesURL=http://www.wylek.ru/
DefaultDirName=C:\Users\aleks\Desktop\Новая папка\My Program
DisableProgramGroupPage=yes
OutputDir=C:\Users\aleks\Desktop\Новая папка
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "russian"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "F:\Projects\Py_test\main.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "F:\Projects\Py_test\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Примечание: Не используйте' флаги "ignoreversion" для общих системных файлов.
; Подцепляем инсталлятор PYTHON
Source: "C:\Users\aleks\Desktop\ters\python-3.6.2-amd64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall;
; Подцепляем Bat для зависимостей
Source: "C:\Users\aleks\Desktop\ters\run.bat"; DestDir: "{tmp}"; Flags: deleteafterinstall;

[Icons]
Name: "{commonprograms}\My Program"; Filename: "{app}\main.py"
Name: "{commondesktop}\My Program"; Filename: "{app}\main.py"; Tasks: desktopicon

[Run]
Filename: "{app}\main.py"; Description: "{cm:LaunchProgram,My Program}"; Flags: shellexec postinstall skipifsilent
; Запустить установку Python
Filename: {tmp}\python-3.6.2-amd64.exe; StatusMsg: Python. Please wait...
; Запустить bat для зависимостей 
Filename: {tmp}\run.bat; StatusMsg: Python. Please wait...

