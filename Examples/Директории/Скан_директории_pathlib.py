"""
Сканирует директории и субдиректории и выводит фсе файлы и их размер в кб
"""
from pathlib import Path

root_path = Path("D:")

for path in Path.rglob(root_path, "*"):
    if path.is_file():
        print(f"{path} {path.stat().st_size / 1024:.3f} Кб")
