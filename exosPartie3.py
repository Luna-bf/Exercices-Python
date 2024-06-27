# Début du chapitre : Enregistrez des données complexes avec des dictionnaires

# Les dictionnaires sont indiqués par des accolades {} au début et à la fin.
# Chaque paire clé-valeur comprend un deux-points : placé entre la clé et la valeur,
# et une virgule , à la fin. Chaque dictionnaire doit être composé de clés uniques.

monDictionnaire = {"Rouge" : "#FF0000"}
monDictionnaire = {"La clé" : "La valeur"}

#Créez un dictionnaire et accédez à une valeur dans un dictionnaire

nouvelle_entreprise = {
    "responsable_de_l'entreprise" : "Luna BURATTI-FAYOLLE",
    "nom_de_l'entreprise" : "ça va de soie",
    "date_de_début" : "18/06/2024"
} #La console affiche bien ces données quand je le lui demande : nouvelle_entreprise[...]

#On peut aussi créer un dictionnaire avec la fonction dict()

x = dict(nom = "Luna", age = 19, majeure = True)
print(x) #La console affiche bien : {'nom': 'Luna', 'age': 19, 'majeure': True}

#Réalisez des opérations courantes avec les dictionnaires

calcul_dictionnaire = {
    "operation" : 13 + 8,
    "soustraction" : 21 - 5,
    "multiplication" : 16 * 2,
    "division" : 32 / 2,
    "division_flottante" : 32 / 3
}

#Ajoutez une paire clé-valeur

# Pour ajouter une paire clé-valeur à un dictionnaire, ajoutez juste une nouvelle clé 
# dans le dictionnaire existant. Si la clé existe déjà, vous l’écraserez en définissant
# une valeur.

info_maine_coon = {
    "poids" : "3 à 6 kg",
    "origine" : "états-unis"
}
print(info_maine_coon)

info_maine_coon["nom_scientifique"] = "Felis catus"
print(info_maine_coon) #Cela ajoute la donnée "nom_scientifique"

info_maine_coon["poids"] = "8,2 à 10 kg (mâle adulte)"
print(info_maine_coon) #Cela change la donnée "poids" de départ


#Supprimez une paire clé-valeur

info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}

#Pour faire ça on utilise le mot-clé 'del' ou la méthode 'pop'

del info_maine_coon["nom_scientifique"]
print(info_maine_coon)

# Certains mots font partie du langage Python, 
# et ne peuvent pas être utilisés comme noms de variables. Par exemple : del, if et else.
# Ces mots sont connus comme étant des mots réservés ou des mots-clés. 


#keys()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
info_maine_coon.keys()
print(info_maine_coon)


#values()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
info_maine_coon.values()
print(info_maine_coon)


#items()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
info_maine_coon.items()
print(info_maine_coon)


#get()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
x = info_maine_coon.get("origine")
print(x)


#pop()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
info_maine_coon.pop("poids")
print(info_maine_coon)


#clear()
info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
info_maine_coon.clear()
print(info_maine_coon)


#Vérifiez l’existence d’une clé spécifique

# Vous pouvez utiliser le mot-clé 'in' pour vérifier si une clé spécifique existe
# dans un dictionnaire. Pour faire cela, spécifiez la clé que vous voulez rechercher,
# écrivez le mot-clé 'in' et le nom de la variable du dictionnaire que vous examinez.
# Le résultat renvoie un booléen qui indique si la clé est dans ce dictionnaire.

info_maine_coon = {
    "poids" : "8,2 à 10 kg",
    "origine" : "états-unis",
    "nom_scientifique" : "Felis catus"
}
"origine" in info_maine_coon #Affiche True
"taille" in info_maine_coon #Affiche False

#Exercice de fin de chapitre

# 1. Création du dictionnaire fruits
fruits = { 
    "pomme" : "rouge",
    "banane" : "jaune",
    "orange" : "orange"
}

# 2. Ajout de la clé "kiwi"
fruits["kiwi"] = "vert"

# 3. Accès à la valeur correspondant à la clé "banane"
couleur_banane = fruits["banane"]

# 4. Modification de la valeur associée à la clé "pomme"
fruits["pomme"] = "vert"

# 5. Suppression de la clé "orange"
del fruits["orange"]
print(fruits)

# 6. Affichage des clés restantes dans le dictionnaire
print(fruits.keys())

#Fin du chapitre