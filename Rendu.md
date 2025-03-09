# TP3-Crypto



## Question 1
- Il faut chiffrer le fichier avec une clé aléatoire. 
- Chiffrer le chiffrement précédant avec un des deux mots de passe et stocker le résultat dans une clé.
- Chiffrer la clé aléatoire (celle qui a chiffré le fichier) avec l'autre mot de passe et stocker le résultat dans l'autre clé.
Ainsi, pour déchiffrer, il faudra posséder les deux clés et les deux mots de passe pour pouvoir reconstituer le fichier initial.


## Question 2
Pour simuler les deux clé usb deux dossiers clé1 et clé2 sont créé a l'initialisation. Pour facilité le test le fichier de mot de passe est présent dans le répertoire, mais peut être supprimer après l'initialisation.

## Question 3
Pour ajouter un responsable légal par admin nous allons nous baser sur l'exercice 1.
Au lieu de chiffrer une seule fois le fichier, nous allons le chiffrer pour chaque combinaison admin/representant. Les deux admin ont les cle 1 et 2, les représentant ont les clés 3 et 4 :
- chiffrer le fichier avec une clé aléatoire.*

- Chiffrer le contenu chiffré avec le mot de passe de l'admin 1, palcer le résultat dans la clé 1, chiffrer la clé aléatoire avec le mot de passe de l'admin 2 et placer le résultat dans la clé 2.

- Chiffrer le contenu chiffré avec le mot de passe de l'admin 1, placer le résultat dans la cle 1, chiffrer la clé aléatoire avec le mot de passe du représentant 2 et placer le résultat dans la clé 4.

- Chiffrer le contenu chiffré avec le mot de passe de l'admin 2, placer le résultat dans la clé 2, chiffrer la clé aléatoire avec le mot de passe du représentant 1 et placer le résultat dans la clé 3.

- Chiffrer le contenu chiffré avec le mot de passe du représentant 1, placer le résultat dans la clé 3, chiffrer la clé aléatoire avec le mot de passe du représentant 2 et placer le résultat dans la clé 4.


## Question 4
Après initialisation, supprimez deux clés pour simuler une connexion a deux. Tenter de connecter l'admin 1 et son propre représentant générera une erreur, pareille pour le 2 et sont représentant

## Question 5
Pour supprimer les droits d'un représentant dans notre modèle, il faut les 3 autres clé les trois autres mots de passe et supprimer des clés présente l'association de fichier avec la clé absente pour qu'il ne puisse plus jamais déchiffrer le fichier même en présence d'une autre clé.


## Correction du modèle 

Après l'implémentation, il est devenu évident que stocker le fichier dans une des clés poserait problème pour modifier le fichier après le démarrage en retirant les clés.
Pour améliorer le modèle nous allons rajouter une étape :
Nous allons chiffrer le fichier avec une cle aléatoire K.
Nous chiffrons k avec une clé aléatoire k2.
Nous chiffrons le résultat du chiffre de k avec le md1 puis le plaçons dans la clé 1.
Nous chiffrons la clé k2 avec me mdp2 et plaçons le résultat dans clé 2.

