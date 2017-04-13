#-------------------- Distance de Jaro V4-------------------#
import numpy as np           # Module math : matrice

texte1 = open("texte_1.txt")
texte2 = open("texte_2.txt")

liste_mot1 = []
liste_mot2 = []
line1 = ""
line2 = ""

## Utilisation du jeu de données
with open("texte_1.txt") as f:
    for line1 in f:
        for mot1 in line1:
             liste_mot1.append(mot1)
print(liste_mot1)

with open("texte_2.txt") as f:
    for line2 in f:
        for mot2 in line2:
             liste_mot2.append(mot2)  
liste2 = liste_mot2

# Longueur de x et y
long_mot1 = len(liste_mot1)
long_mot2 = len(liste_mot2)

## Test si les deux chaînes sont égales 
if liste_mot1 == liste_mot2:
    cpt =1
else:
    cpt = 0

# Initialisation du matches
m = 0

# Initialisation de la matrice de correspondance à 0
mat = np.full(shape=(long_mot1,long_mot2),fill_value=0)


# Distance d'éloignement Maximal entre les deux mots
DistMax = max(long_mot1,long_mot2)/2 - 1
print("Distance d'éloignement maximale entre les mots <= : ",DistMax)


# Fonction Matches----------------------------------
# Remplissage de la matrice
## Chercher les "1" pour calculer le matches
def matches(liste_mot1,liste_mot2,m):
    for i in range(0,long_mot1):
        for j in range(0,long_mot2):        
            if liste_mot1[i] == liste_mot2[j] and i-j <= DistMax: # + test DistMax
                mat[i][j] = 1   # corrspondance
                m = m+1
                break           # ne prendre que la première similarité!
            else:
              mat[i][j] = 0
              
    return m

matches = matches(liste_mot1,liste_mot2,m)
print("Matches = ",matches)
#----------------------------------------------------

listee = []
pos = []
# Rechercher les transpositions
## Supprimer les caractères n'ayant aucune correspondance
### i.e. les lignes et colonnes remplies de 0

# Accès ligne par ligne
print("Supression des mots non correspondants:\n")
def SuppNonCorrespLignes(mot1,mot2):
    for i in range(0,long_mot1):
        som = sum(mat[i])
        
        if sum(mat[i]) == 0.0:
            listee.append(liste_mot1[i])
            pos.append(i)
            i = i+1

    # inverser les indices :) 
    for p in range(len(pos)-1, -1, -1):
        a = pos[p]
        
        for i in range (long_mot1, -1, -1):
            if a == i:
                del(liste_mot1[i])

    return liste_mot1
                
liste_mot1 = SuppNonCorrespLignes(mot1,mot2)
print("Mot 1 devient = ",liste_mot1)

listee2 = []
pos2=  []
# Accès colonne par colonne
def SuppNonCorrespColonnes(liste_mot1,liste_mot2):
    for j in range(0,long_mot2):
        if sum(mat[:,j]) == 0.0:

            listee2.append(liste_mot2[j])
            pos2.append(j)
            j = j+1
    
    # inverser les indices :)  sinon erreur out of range
    for p in range(len(pos2)-1, -1, -1):
        a = pos2[p]
        
        for j in range (long_mot2, -1, -1):
            if a == j:
                del(liste_mot2[j])
                
    return liste_mot2

liste_mot2 = SuppNonCorrespColonnes(liste_mot1,liste_mot2)
print("Mot 2 devient = ",liste_mot2)
# ---------------------------------------------------


# Fonction Transposition ----------------------------
### trans = nbre de car différents ayant un correspondant
max_long = max(len(liste_mot1),len(liste_mot2))

car_sim = 0
def transposition(liste_mot1,liste_mot2,car_sim):
    for i in range (0,len(liste_mot1)):
        for j in range (0,len(liste_mot2)):
            if i == j:  
                if liste_mot1[i] == liste_mot2[j]:
                        car_sim = car_sim + 1   # nbre caractères similaires correspondants
                        break
   
    trans = (max_long - car_sim  ) /2 # trans = (nbre total car - nbre car. similaires) = nbre car différents puis divisé sur 2
    return trans

trans = transposition(liste_mot1,liste_mot2,car_sim)
print("Transposition = ",trans)

#--------------------------------------------------------


# Distance de Jaro
if cpt == 1:
    djaro = 1.0
else:
    djaro = 1/3 * (matches/long_mot1 + matches/long_mot2 + (matches-trans)/matches)

print("Distance de Jaro = ",djaro)


#----------------------------------------------------------

# Distance de Jaro-Winkler

## Le plus grand préfixe
# Il suffit de comparer les mots
prefixe = 0
for i in range(0,min(len(line1),len(line2))): 
        if line1[i] == line2[i] and prefixe <4:    # line correspond à la chaîne initiale
            prefixe = prefixe +1

#print("Prefixe : ",prefixe)

## Le coefficient
p = 0.1

if djaro == 1.0:
    djaroWinkler = 1.0
else:
    djaroWinkler = djaro + (prefixe * p * (1-djaro))
    print("Distance de Jaro Winkler : ",djaroWinkler)

