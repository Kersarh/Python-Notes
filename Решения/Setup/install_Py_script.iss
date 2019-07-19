; ���� �������� ������ � ������� ������� Inno Setup.
; ���������� � ���������� ������������, ����� ������������ ��� ����������� INNO SETUP!

[Setup]
; ����������: �������� AppId �������� ���������� ��������������� ��� ����� ����������.
; �� ����������� ���� � ���� �������� AppId ��� ������ ����������.
; (��� �������� ������ �������� GUID, �������� � ���� "�����������" ����� "������� GUID".)
AppId={{F5482354-0EA6-43C7-8CAD-4E5E665C1C37}
AppName=My Program
AppVersion=1.5
;AppVerName=My Program 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.wylek.ru/
AppSupportURL=http://www.wylek.ru/
AppUpdatesURL=http://www.wylek.ru/
DefaultDirName=C:\Users\aleks\Desktop\����� �����\My Program
DisableProgramGroupPage=yes
OutputDir=C:\Users\aleks\Desktop\����� �����
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
; ����������: �� �����������' ����� "ignoreversion" ��� ����� ��������� ������.
; ���������� ��������� PYTHON
Source: "C:\Users\aleks\Desktop\ters\python-3.6.2-amd64.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall;
; ���������� Bat ��� ������������
Source: "C:\Users\aleks\Desktop\ters\run.bat"; DestDir: "{tmp}"; Flags: deleteafterinstall;

[Icons]
Name: "{commonprograms}\My Program"; Filename: "{app}\main.py"
Name: "{commondesktop}\My Program"; Filename: "{app}\main.py"; Tasks: desktopicon

[Run]
Filename: "{app}\main.py"; Description: "{cm:LaunchProgram,My Program}"; Flags: shellexec postinstall skipifsilent
; ��������� ��������� Python
Filename: {tmp}\python-3.6.2-amd64.exe; StatusMsg: Python. Please wait...
; ��������� bat ��� ������������ 
Filename: {tmp}\run.bat; StatusMsg: Python. Please wait...

