#Ce document contient les exercices des deux chapitres suivants d'OpenClassrooms

#Le type
character = "Quirrel"
print(character)

#Pour tester le type d'une variable, il faut utiliser la console
#Exemple : monBooleen = False
#type(monBooleen)
#La console va afficher : <class 'bool'>

# La fonction "type()" en Python est utilisée pour déterminer le type de données
# d'une variable. Elle renvoie le type de l'objet en tant que sortie, tel que 'int',
# 'str', 'bool', etc. Cela permet aux développeurs de vérifier rapidement et facilement
# le type de données avec lesquelles ils travaillent. (OpenClassrooms)

#Exercice de fin de chapitre précédent
nom = "Luna"
age = 19
taille = 1.54
est_etudiant = False
print(nom, age, taille, est_etudiant) # Je peux tout imprimer en même temps
# J'ai ensuite utilisé la console pour vérifier le type de chaques variables
# Fin du chapitre


#Début du chapitre : Enregistrez des groupes de données avec les listes

indie_games = ["Hollow Knight: SilkSong", "KinitoPET", "Undertale", "Little Misfortune"]
print(indie_games[2])

# Pour accéder au dernier élément de la liste, utilisez l’indice -1 (OpenClassrooms)

print(indie_games[-1])


#Accédez aux caractères d’une chaîne comme un élément d’une liste

# Par exemple, dans la chaîne langage = "PYTHON", langage[2] vous renverra "T".
# Tout simplement parce que l’indice 2 dans le mot "PYTHON" est le "T".
# Ou bien, avec l’indice de la position inverse, vous devez utiliser langage[-4]
# pour accéder à  "T" (OpenClassrooms)

lost_wave = "EKT"
lost_wave[1] # La console renvoie 'K'

lost_song = "Blind the wind"
lost_song[-4] # La console renvoie 'w'

#Modifiez les éléments d’une liste

indie_games = ["Hollow Knight: SilkSong", "KinitoPET", "Undertale", "Little Misfortune"]
indie_games[2] = "Fran Bow"
print(indie_games)

#Ajoutez, retirez et triez les listes

# Pour ajouter un jeu indé à la fin de la liste existante,
# vous pouvez utiliser la méthode append()

indie_games.append("Doki doki literature club")
print(indie_games)

# remove() retire uniquement la première instance du terme que vous saisissez.
# Pour connaître la longueur de la liste, utilisez la méthode len()

indie_games = ["Hollow Knight: SilkSong", "KinitoPET", "Undertale", "Little Misfortune", "Doki doki literature club"]
print(indie_games)
len(indie_games) # Tout ça dans une console python


#sort()
spanish_songs = ["Rumba do vesou", "Mehdi", "Arrinconamela"]
spanish_songs.sort()
print(spanish_songs)

#extend()
alphabet = ['a', 'b', 'c']
alphabet.extend('d')
print(alphabet)

#insert()
internet_horror = ['Mandela Catalogue', 'Mlp infection AU', 'Best friend september']
internet_horror.insert(3, 'Lacey games')
print(internet_horror)

#pop()
internet_horror = ['Mandela Catalogue', 'Mlp infection AU', 'Best friend september', 'Lacey games']
internet_horror.pop(2)
print(internet_horror)

#index()
internet_horror = ['Mandela Catalogue', 'Mlp infection AU', 'Best friend september', 'Lacey games']
x = internet_horror.index('Mlp infection AU')
print(x)

#count()
internet_horror = ['Mandela Catalogue', 'Mlp infection AU', 'Best friend september', 'Lacey games']
y = internet_horror.count('Best friend september')
print(y)

#reverse()
internet_horror = ['Mandela Catalogue', 'Mlp infection AU', 'Best friend september', 'Lacey games']
internet_horror.reverse()
print(internet_horror)


#Découvrez les tulpes

spanish_songs_tulpe = ("Rumba do vesou", "Mehdi", "Arrinconamela")
# Contrairement aux listes, les tulpes ne sont pas modifiables et sont entre parenthèses

#Trouvez un élément

# Pour ça, on utilise l'opérateur 'in'
spanish_songs = ["Rumba do vesou", "Mehdi", "Arrinconamela"]
"Rumba do vesou" in spanish_songs #La console affiche True

spanish_songs = ["Rumba do vesou", "Mehdi", "Arrinconamela"]
"Payo Michto" in spanish_songs #La console affiche False

#Exercice de fin de chapitre

fruits = ["pomme", "banane", "orange"] # 1. Création de la liste
fruits.insert(3, "kiwi") # 2. Ajout de "kiwi"
fruits.pop(2) # 3. Supression de "orange"
fruits[1] = "ananas" # 4. Modification du deuxième élément en "ananas"
len(fruits) # 5. Affichage de la longueur de la liste
fruits.sort() # 6. Tri de la liste
print(fruits) # 7. Impression de la liste : ['ananas', 'kiwi', 'pomme']

#Fin du chapitre