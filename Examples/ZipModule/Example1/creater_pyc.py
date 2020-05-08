#! python
import compileall

modDir = "lib" # папка с модулем
compileall.compile_dir(modDir)

# # Для одного файла
# import py_compile
# py_compile.compile('mod1.py')