import os
import sys

def translit(txt):
	text = txt.lower()
	dic = {
		u'а': u'a',
		u'б': u'b',
		u'в': u'v',
		u'г': u'g',
		u'д': u'd',
		u'е': u'e',
		u'ё': u'e',
		u'ж': u'zh',
		u'з': u'z',
		u'и': u'i',
		u'й': u'y',
		u'к': u'k',
		u'л': u'l',
		u'м': u'm',
		u'н': u'n',
		u'о': u'o',
		u'п': u'p',
		u'р': u'r',
		u'с': u's',
		u'т': u't',
		u'у': u'u',
		u'ф': u'f',
		u'х': u'h',
		u'ц': u'ts',
		u'ч': u'ch',
		u'ш': u'sh',
		u'щ': u'sch',
		u'ъ': u'',
		u'ы': u'y',
		u'ь': u'',
		u'э': u'e',
		u'ю': u'yu',
		u'я': u'ya',
		u' ': u'_',
			}

	dic_en = 'abcdefghijklmnopqrstuvwxyz'

	translate_txt = ""

	for i in text:
		if i in dic.keys():
			i = dic[i]
			translate_txt = translate_txt + i
		elif i in dic_en:
			translate_txt = translate_txt + i
		else:
			pass

	print (translate_txt)

translit("Привет Мир! PriVet MiR!")

os.system('pause' if os.name == 'nt' else """bash -c 'read -s -n 1 -p "Press any key to continue...\n"'""")