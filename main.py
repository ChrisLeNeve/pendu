
from random import choice

zero = '''
------------
|          |
|
|
|
|
-----------


'''

one = '''
------------
|          |
|          O
|
|
|
-----------

'''
two = '''
------------
|          |
|          O
|          |
|
|
-----------

'''
three = '''
------------
|          |
|          O
|          |
|         /
|
-----------

'''
four = '''
------------
|          |
|          O
|          |
|         / \\
|
-----------

'''
five = '''
------------
|          |
|          O
|         -|
|         / \\
|
-----------

'''
fin = '''
------------
|          |
|          O
|         -|-
|         / \\
|
-----------

'''

etapes_pendaison = [zero, one, two, three, four, five]
mots = ['Enfield', 'Triumph', 'BMW', 'Peugeot', 'Citroen', 'Renault', 'Volvo', 'Fiat', 'Mazda', 'Toyota', 'Audi', 'Volkswagen', 'Ford', 'Tesla', 'Chrysler', 'Porsche']
mot = choice(mots)
mot_en_cours = '_ ' * len(mot)
lettres_devinees = []
fin_du_jeu = False

while not fin_du_jeu:
	print(etapes_pendaison[0])
	print('Le mot: ')
	print(mot_en_cours)
	print('Devine une lettre :')
	lettre = input('lettre : ').lower()
	lettres_devinees.append(lettre)
	if lettre not in mot.lower():
		etapes_pendaison.pop(0)	
		if len(etapes_pendaison) == 0:
			print(fin)
			print('tu as perdu')
			fin_du_jeu = True
	else:
		il_reste_au_moins_une_lettre_a_deviner = False
		mot_en_cours_temporaire = ''
		for i in mot:
			if i.lower() in lettres_devinees:
				mot_en_cours_temporaire = mot_en_cours_temporaire + i + ' '
			else:
				mot_en_cours_temporaire = mot_en_cours_temporaire + '_ '
				il_reste_au_moins_une_lettre_a_deviner = True
		mot_en_cours = mot_en_cours_temporaire
		if not il_reste_au_moins_une_lettre_a_deviner:
			print(mot.upper())
			print('bravo, tu as gagné !')
			fin_du_jeu = True






'''
choisir un mot
tant que le jeu n'est pas terminé:
	afficher l'étape actuelle dans le pendu
	écrire un tiret pour chaque lettre non devinée et toutes les lettres devinées jusqu'à présent
	faire deviner une lettre
	si la lettre existe dans le mot:
		s'il n'y a plus aucune lettre à deviner:
			game over
	si la lettre n'existe pas dans le mot:
		passer à l'étape suivante dans le pendu
		si on est à la dernière étape:
			game over

'''