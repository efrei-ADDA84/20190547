# 20190547

## TP1 et TP2 

Cf. branche TP2

## TP3 Théo MARTIN

### Démarche

J'ai créé une GitHub Action qui push sur Azure mon image. 

#### Particularités rencontrées 

J'ai du créer un secret github afin de rajouter la variable d'nevironnement API_KEY dans le github action  
J'ai également du préciser dans la github action le port 8081.


On retrouve donc mon image sur le lien : 

http://devops-20190547.francecentral.azurecontainer.io:8081/?lat=5.902785&lon=102.754175

## TP4 Théo MARTIN

Le TP4 se trouve dans le dossier correspondant sur le main.  

On a créé notre main.tf puis rajouté les outputs afin de générer une clé ssh.  

Sur Windows, le id_rsa n'était pas reconnu. J'ai du passer par un fichier texte private_key.txt pour rentrer la commande suivante :  
```  ssh -i private_key.txt devops@51.103.85.191 ```  

On est ensuite connecté à la VM.  
On peut ensuite utiliser ``` terraform destroy ```
