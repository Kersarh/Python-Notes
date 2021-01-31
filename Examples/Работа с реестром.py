import winreg as wreg

reg_dir = r"Software\\Microsoft\\Windows\\CurrentVersion\\Run"
key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, reg_dir, 0, wreg.KEY_SET_VALUE)
wreg.SetValueEx(key, "NAME", 1, wreg.REG_SZ, "VALUE")
# wreg.SetValueEx(key, "Name", 1, wreg.REG_DWORD, 1)

wreg.CloseKey(key)
