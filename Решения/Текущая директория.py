import os
from pathlib import Path

print(Path.cwd())
os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")