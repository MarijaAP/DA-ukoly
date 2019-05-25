"""Moje kamarádka učí soukromě němčinu. Potřebuje pro klienty připravit texty, 
které se časem naučí nazpaměň (jedná se o právní předpisy). Proto jim připravuje 
stále stejný text, ve kterém vynechá nejprve každé 
5. slovo, později každé 4. slovo atd., až se text naučí zpaměti. 
Výstupem bude nový soubor. Pracujte se souborem lorem.py.
Vytvořte pro ni program, jehož vstupem bude textový soubor a informace, 
kolikátý znak se má zaměnit.
"""

def doplnovacka(file, number):
	with open(file) as f:
		text = f.read()
	f.closed
	text = text.replace("\n", "# ")
	text = text.replace("  ", " ")
	#print(text)

	seznam = []
	seznam = text.split(" ")
	#print(seznam)

	for i in range(0, len(seznam), number):
		word = seznam[i]
		seznam[i] = "-" * len(word)

	s = " ".join(seznam)
	print(s)
	s = s.replace("#", "\n")
	print(s)
	return
	
print(doplnovacka("lorem.txt", 5))
