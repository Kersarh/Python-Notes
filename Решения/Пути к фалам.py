# -*- coding: UTF-8 -*-

from pathlib import Path
root = Path('C:\\')
print("root = ", root)

path = root / 'folder' / 'folder2'
print(path.resolve())
# /home/weenkus/Workspace/Projects/DataWhatNow-Codes/how_your_python3_should_look_like/post_sub_folder/happy_user