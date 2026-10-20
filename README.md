# webheaders

Donne une URL, le script fait une requête GET et regarde si les en-têtes de
sécurité HTTP importants sont présents (HSTS, CSP, X-Frame-Options...). Il
signale aussi le header Server quand il révèle la techno du serveur.

C'est le genre de vérif rapide qu'on fait au début d'un audit web, et ça aide
à comprendre à quoi sert chaque header.

## Install

```
pip install -r requirements.txt
```

## Utilisation

```
python headers.py example.com
python headers.py https://github.com
```

Tester sur des vrais sites est ok ici : on fait une simple requête GET, rien
d'intrusif, comme un navigateur. On peut aussi tester une DVWA locale.

## Ensuite

- vérifier la valeur des headers, pas juste leur présence (ex: HSTS avec un max-age trop court)
- suivre les redirections et montrer la chaîne http -> https
- scanner une liste d'URL depuis un fichier
