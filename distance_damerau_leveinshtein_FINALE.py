#---------------------- Script Distance de Levenshtein et Damerau Levenshtein V2------------#
import numpy as np

# Les mots à comparer
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
liste1 = liste_mot1
print(liste_mot1)

with open("texte_2.txt") as f:
    for line2 in f:
        for mot2 in line2:
             liste_mot2.append(mot2)  
print(liste_mot2)
liste2 = liste_mot2

# Longueur des mots
long_ch1 = len(liste_mot1)
long_ch2 = len(liste_mot2)


# Matrice d'édition M
## Initialisation à 0: (n+1 lignes * m+1 colonnes)
mat_lev = np.full(shape=(long_ch1+1,long_ch2+1),fill_value=0)
mat_dl = np.full(shape=(long_ch1+1,long_ch2+1),fill_value=0)

print("Initialisation de la matrice à zéro : \n")
print(mat_lev)

## Initialisation avec les indices
for i in range(1,long_ch1+1): 
        mat_lev[i,0] = mat_lev[i-1,0]+1
        mat_dl[i,0] = mat_dl[i-1,0]+1 
for j in range(1,long_ch2+1): 
        mat_lev[0,j] = mat_lev[0,j-1]+1
        mat_dl[0,j] = mat_dl[0,j-1]+1 

print("\n\n\nInitialisation de la matrice avec les indices : \n")
print(mat_lev)

# Matrice Cout
cout = np.full(shape=(long_ch1,long_ch2),fill_value=0)
for i in range(0,long_ch1):
    for j in range(0,long_ch2):
        if liste_mot1[i] != liste_mot2[j]:
            cout[i][j] = 1
        else:
            cout[i][j] = 0
print("\n\n\nMatrice Cout : \n") 
print(cout)  

## MATRICE D'EDITION
# Distance Lev = Min(supp,ins,sub)
# Distance Dam_Lev = Min(supp,ins,sub,trans)
         
for i in range(1,long_ch1+1):
    for j in range(1,long_ch2+1):
        mat_lev[i,j] = min(mat_lev[i-1,j] + 1 , mat_lev[i,j-1] + 1, mat_lev[i-1,j-1] + cout[i-1,j-1])
        mat_dl[i,j]  = min(mat_dl[i-1,j] + 1,   mat_dl[i,j-1]  + 1, mat_dl[i-1,j-1]  + cout[i-1,j-1] , mat_dl[i-2,j-2] + cout[i-1,j-1]) # +transposition
        
        
Distance_Lev   = mat_lev[long_ch1,long_ch2]
Distance_Dam_Lev = mat_dl[long_ch1,long_ch2]

print("Matrice Levenshtein :\n",mat_lev)
print("Matrice Damerau Levenstein :\n",mat_dl)

print("Distance de Levenshtein :",Distance_Lev)
print("Distance de Damereau Leveinshtein :",Distance_Dam_Lev)
