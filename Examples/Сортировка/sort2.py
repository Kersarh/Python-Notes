# Сортировка без учета регистра

f_0='ABbBCda'
f_2 = []
for sub_lst in f_0:
    f_2.append(sorted(''.join(sub_lst), key=str.lower))
print(f_2)