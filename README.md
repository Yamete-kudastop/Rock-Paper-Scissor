# Rock Paper Scissor
 
Rock Paper Scissor
 
## Rock Paper Scissors (Pierre - Feuille - Ciseaux) ##

Premier projet Python 
Le but : recréer le classique Pierre - Feuille - Ciseaux contre l’ordinateur, en mode console.


Objectif du projet

Ce projet nous a permis de :

 -Apprendre le langague Python et sa logique 
 -Appris le fonction Random 



Structure du projet


Rock-Paper-Scissor/

 ──RPS
 ── main.py 
 ──.gitattributes              
  ── SRC/
    ── Player/Player.py   
    ── Computer/Computer.py   
    ── Choice/Choice.py  
    ── Fight/Fight.py     
    ── Score/Score.py     
    ── Round/Round.py  
    ── Win
    ── Lose   

 Exmplications de chaque categories 

 main.py :
 Ce fichier orchestre le jeu du début à la fin, en combinant choix du joueur, rounds, scores et messages de victoire/défaite, pour une expérience complète et interactive.
 
 Player.py :
 Elle sert à personnaliser l’expérience du joueur tout en gardant un nom par défaut s’il ne saisit rien.

 Computeur.py : 
 Cette fonction simule le coup de l’ordinateur à chaque manche, elle retourne rock, paper ou scissors de façon aléatoire.

 Choice.py : 
 Cette fonction garantit que le joueur entre un choix valide, et le renvoie une fois que c’est correct.

 Fight.py :
 Cette fonction renvoie toujours l’un des trois résultats possibles :
 win  le joueur gagne
 lose  l’ordinateur gagne
 tie  égalité

Score.py : 
Classe pour suivre les scores d’un jeu joueur vs ordinateur (victoires, défaites, égalités, rounds).
add_result(result) : met à jour le score
show_score(final=False) : affiche le score actuel ou final

Round.py : 
Fonction principale qui gère un tour complet du jeu. Elle récupère les choix du joueur et de l’ordinateur, détermine le gagnant et affiche le résultat à l’écran. Utile pour automatiser un round et connecter toutes les parties du jeu (choix, combat, score, messages de victoire/défaite).

Win.py :
Affiche un message de victoire lorsque le joueur gagne un round.

Lose.py :
Affiche un message de défaite lorsque le joueur perd un round.


Lancer le jeu

1 Ouvrir le terminal dans le dossier du projet.
2 Exécuter la commande :

py main.py


Règles du jeu

 Le joueur choisit entre rock, paper ou scissors
 L’ordinateur fait un choix aléatoire.
Le programme affiche le résultat :
  Tu gagnes, tu perds, ou égalité 
 Le score s’actualise à chaque manche.


 À propos

Auteur :Jon Siong Théo Veret
Étudiants en Bachelor Cybersécurité à Ynov Val d’Europe.
Projet 1 en Python : Rock Paper Scissors


