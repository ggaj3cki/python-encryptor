#!/usr/bin/python3

import sys

# zewnetrzna biblioteka wymagajaca instalacji 
# pip3 install cryptography lub apt install python3-cryptography
# import odpowiedniej funkcji z aliasem fer
from cryptography.fernet import Fernet as fer

# pobranie sciezki do pliku do zaszyfrowania
pathToFile = sys.argv[2]

# pobranie sciezki klucza
pathToKey = sys.argv[3]

#pobranie opcji do uruchomienia
try:
	opcja = int(sys.argv[1])
except:
	print('Wybierz 1 (szyfrowanie) albo 2 (deszyfrowanie)')

def szyfrowanie (sciezkaPliku, sciezkaKlucza):
	#generowanie i zapis klucza do zmiennej
	klucz = fer.generate_key()
	
	# zapis klucza do pliku
	with open(sciezkaKlucza, 'wb') as plik:
		plik.write(klucz)

	# uzycie klucza
	klucz = fer(klucz)

	# otwarcie pliku
	with open(sciezkaPliku, 'rb') as plik:
		original = plik.read()

	#szyfrowanie pliku
	zaszyfrowany = klucz.encrypt(original)

	# zapis zaszyfrowanego pliku
	with open(sciezkaPliku, 'wb') as plik:
		plik.write(zaszyfrowany)

def deszyfrowanie(filepath, keypath):
	# otwarcie klucza i zmiana kodowania z bytestring na utf-8
	with open(keypath, 'rb') as plikKlucza:
		klucz = plikKlucza.read()
	klucz = klucz.decode('utf-8')

	# uzycie klucza
	klucz = fer(klucz)

	# otwarcie zaszyfrowanego pliku
	with open(filepath, 'rb') as zplik:
		zaszyfrowany = zplik.read()

	# odszyfrowanie pliku
	odszyfrowany = klucz.decrypt(zaszyfrowany)

	# zapis odszyfrowanego pliku
	with open(filepath, 'wb') as oplik:
		oplik.write(odszyfrowany)

# srpawdzanie wybranych funkcji i uruchomienie odpowiedniej funkcji
if opcja == 1:
	szyfrowanie(pathToFile, pathToKey)

if opcja == 2:
	deszyfrowanie(pathToFile, pathToKey)
