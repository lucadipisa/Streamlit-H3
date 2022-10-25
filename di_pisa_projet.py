# -*- coding: utf-8 -*-
"""Di_Pisa_Projet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vrm_tVeQFPNRNE4Q5EZGskWX1ktN1UrC
"""

#Import des librairies
import streamlit as st
import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt

#Import du csv
filename = r'/content/drive/MyDrive/Colab/fighters.csv'
import csv
open(filename)
data = pd.read_csv(r'/content/drive/MyDrive/Colab/fighters.csv');
data

"""**Jeu de données** : Matches de Boxe


---
**Problèmatique** : Est-ce qu'il y a des caractèristiques qui facilitent la victoire d'un fighter ?


"""

#Continue
data_wins = data.sample(n=200)
nb = sb.relplot(data=data_wins, x="wins", y="height")
st.pyplot(nb)

"""Pour ce diagramme à nuage de points nous pouvons regarder comment se comporte la colonne wins par rapport à la taille du fighter (height). Nous constatons ainsi que nous pouvons avoir un fighter de petite taille (1.65 par exemple) qui possède environ 140 matchs gagnés alors qu'un autre fighter de plus grande taille (1.97 par exemple) a gagné 25 matchs."""

#Continue
data_reach = data.sample(n=100)
nb2 = sb.relplot(data=data_reach, x="wins", y="reach")
st.pyplot(nb2)

"""Pour ce qui concerce ce diagramme, nous pouvons constater que le "reach" ou l'allonge d'un fighter n'influence pas sur les matchs gagnés."""

nb3 = sb.catplot(data=data, x="wins", y="stance")
st.pyplot(nb3)


"""Ici nous constatons que la garde "orthodox" est plus utilisé que la "southpaw" mais nous devons filtrer ces données afin d'identifier des éventuelles données aberrantes."""

nb4 = sb.boxplot(data=data, x="wins", y="stance")
fig1 = nb4.figure
st.pyplot(fig1)

"""On peut voir que nous avons des données aberrantes : cela est dû aux combattants qui ont fait plus de matchs ou les meilleurs."""

data_stance = data[ data['wins'] < 55 ]
nb5 = sb.boxplot(data=data_stance, x="wins", y = "stance")
fig2 = nb5.figure
st.pyplot(fig2)

"""Après avoir enlevé ces données aberrantes, nous pouvons constater que la moyenne de victoires de ceux qui utilisent une garde "southpaw" est supérieure à celle des fighters qui utilisent l' "orthodox"."""

nb6 = plt.figure(figsize=(10,6))
data_wins3 = data.sample(n=50)
sb.barplot(y='ko_rate', x='wins', data=data_wins3)
plt.ylabel('Pourcentage de KO')
plt.xlabel('Victoires')
plt.show()
fig3 = nb6.figure
st.pyplot(fig3)


"""Une autre caractéristique est le pourcentage de KO réalisés par un fighter. On peut voir que cela n'a aucun réel impact sur le nombre de victoires car tout peut dépendre aussi du nombre de matchs total : Si un combattant a 100% de KO mais qu'il a que 1 ou 2 matchs ce n'est pas pertinent.

Pour conclure, on peut dire que nous pouvons pas dire qu'une caractéristique X d'un fighter influence sur son nombre de victoires. 
Ceci est expliquable car un match se déroule entre deux fighters de plus ou moins la même taille et même poids.
La seule caractéristique, en moyenne, qui influence le nombre de victoire est la garde car nous avons plus de victoires pour ceux qui utilisent le southpaw par rapport à l'orthodox.
On peut aussi dire que la victoire d'un match est déterminé par la prouesse et la technique du fighter en question.
"""

