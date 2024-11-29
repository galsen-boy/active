# TinyScanner: A Simple Port Scanner

## Overview

## Description

TinyScanner est un outil léger en ligne de commande conçu pour les administrateurs réseau, les professionnels de la sécurité et les passionnés de technologie afin d'effectuer des opérations de base de scan de ports. Il prend en charge l'analyse des ports TCP et UDP pour identifier les ports ouverts ou potentiellement filtrés sur un hôte cible. Cet outil est particulièrement utile pour les diagnostics réseau, les audits de sécurité et les fins éducatives.


### Qu'est-ce qu'un port ?
Un port sert de passerelle pour permettre aux programmes d'envoyer et de recevoir des données via un réseau, garantissant que les données parviennent au programme destiné sur un appareil.

### Qu'est-ce que le scan de ports ?
Le scan de ports consiste à vérifier les ports d'un ordinateur ou d'un réseau afin de déterminer lesquels sont ouverts ou fermés, révélant ainsi les services disponibles et les éventuelles vulnérabilités.

### Pourquoi le scan de ports est-il important en test d'intrusion (pentesting) ?
Le scan de ports est essentiel en test d'intrusion car il permet d'identifier les ports ouverts et les services sur un système cible. Ces informations permettent aux pentesters d'évaluer la sécurité du réseau, de repérer d'éventuels points d'entrée, et de simuler des attaques réelles, ce qui aide les organisations à renforcer leurs défenses.

## Avertissements et Défis
### Analyse des ports UDP

La détection des ports UDP ouverts présente des défis uniques en raison de la conception sans connexion de ce protocole. Contrairement au TCP, l'absence de réponse d'un port UDP ne signifie pas de manière définitive que le port est ouvert ou fermé. Ainsi, TinyScanner peut signaler les ports UDP comme "ouverts/filtrés" ou "ouverts/filtrés (pas de réponse)" en fonction de l'absence de réponse ou d'un message ICMP indiquant que le port est inaccessible. Cette méthode est choisie pour sa simplicité et sa praticité pour des analyses de base, bien qu'elle ne fournisse pas toujours des résultats concluants.
### Considérations légales et éthiques

L'analyse des ports peut être perçue comme intrusive par les opérateurs de réseau. Assurez-vous toujours d'avoir une autorisation explicite pour analyser le réseau ou l'hôte concerné. Les analyses non autorisées peuvent être illégales ou enfreindre les politiques locales.

### Comment fonctionne le programme ?
Le programme est un scanner de ports qui permet aux utilisateurs de spécifier un hôte cible et une plage de ports à analyser. Il établit des connexions à l'aide de sockets TCP ou UDP pour vérifier si les ports sont ouverts ou fermés, puis il rapporte l'état de chaque port.


### Prérequis

- Python 3.x installed on your system.
- Network access to the host you intend to scan.

### Running the Scanner
``hostname -I``
```
11.11.90.120 172.18.0.1 172.19.0.1 172.17.0.1
``` 

1. **Cloner ou télécharger le script TinyScanner** sur votre machine locale.

2. **Ouvrez un terminal ou une invite de commande** et accédez au répertoire contenant `tinyscanner.py`.

3. **Exécutez le script** avec les paramètres requis :
```
python3 tinyscanner.py <host> <port/port-range> [-u] [-t]
```

- `<host>`: The IP address or hostname of the target machine.
- `<port/port-range>`: Specify a single port (e.g., 80) or a range of ports (e.g., 20-80).
- `-u`: Perform a UDP scan (optional).
- `-t`: Perform a TCP scan (optional).

**Example**:
``python3 tinyscanner.py -t 127.0.0.1 -p 80-83``
```
Port 81/TCP is closed
Port 80/TCP is open | Service: http
Port 82/TCP is closed
Port 83/TCP is closed
```
``python3 tinyscanner.py -u 127.0.0.1 -p 80-83``
```
Port 80/UDP is open/filtered (no response)
Port 81/UDP is open/filtered (no response)
Port 83/UDP is open/filtered (no response)
Port 82/UDP is open/filtered (no response)
```
 ``python3 tinyscanner.py -h``
 ```
usage: tinyscanner.py [-h] [-p PORT [PORT ...]] [-u] [-t] host

Usage: tinyscanner [OPTIONS] [HOST] [PORT]

positional arguments:
  host                  The host to scan

optional arguments:
  -h, --help            show this help message and exit
  -p PORT [PORT ...], --port PORT [PORT ...]
                        Range of ports to scan
  -u, --udp             UDP scan
  -t, --tcp             TCP scan
  ```

Cette commande scanne les ports 80 à 90 sur l'hôte ``192.168.1.1`` pour les protocoles TCP et UDP.
## Comment ça fonctionne

TinyScanner utilise le module ``socket`` de Python pour tenter des connexions sur les ports spécifiés. Pour les scans TCP, il essaie d'établir une connexion en utilisant la méthode ``connect_ex``. Un port est considéré comme ouvert si la connexion est réussie. Pour les scans UDP, en raison de la nature sans connexion du protocole UDP, le scanner envoie une charge utile de base et attend une réponse. Si aucune réponse n'est reçue, le port est considéré comme ouvert/filtré. Le scanner utilise le multithreading pour effectuer des scans en parallèle, réduisant ainsi le temps total de scan.

## Avertissements et défis
### Scan UDP

La détection des ports UDP ouverts présente des défis uniques en raison de la conception sans connexion du protocole. Contrairement au TCP, l'absence de réponse d'un port UDP n'indique pas de manière définitive le statut du port. Ainsi, TinyScanner peut signaler les ports UDP comme ``ouverts/filtrés`` ou ``ouverts/filtrés (pas de réponse)`` en fonction de l'absence de réponse ou d'un message ICMP indiquant que le port est inaccessible. Cette méthode est choisie pour sa simplicité et son efficacité pour les scans basiques, bien qu'elle ne fournisse pas toujours des résultats concluants.
Considérations légales et éthiques

Le scan de ports peut être interprété comme intrusif par les opérateurs de réseaux. Assurez-vous toujours d'avoir une permission explicite pour scanner le réseau ou l'hôte en question. Les scans non autorisés peuvent être illégaux ou enfreindre les politiques locales.


## Tester localement avec du code serveur

Pour faciliter les tests de TinyScanner, nous fournissons un script serveur simple capable d'exécuter des serveurs TCP et UDP sur des ports spécifiés. Ce script peut simuler un environnement réel sur votre machine locale, offrant ainsi un cadre sûr et pratique pour les tests.

### Exécution du script serveur

1. Enregistrez le script serveur fourni sous le nom de `servers.py`.

2. Exécutez le script avec Python en spécifiant le port de départ et le nombre de serveurs :
``python3 servers.py <start_port> <num_servers>``

Cela démarrera des serveurs TCP et UDP alternés sur des ports consécutifs à partir de `<start_port>`.

### Exemple

Pour démarrer 10 serveurs en commençant par le port 80 (5 serveurs TCP et 5 serveurs UDP sur des ports alternés) :

``sudo python3 servers.py 80 10``
```
[sudo] Mot de passe de mouhamadou : 
Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
UDP server listening on port 81
TCP server listening on port 82
UDP server listening on port 85
TCP server listening on port 84
    self.run()
  File "/usr/lib/python3.8/threading.py", line 870, in run
UDP server listening on port 83
TCP server listening on port 86
UDP server listening on port 87
    self._target(*self._args, **self._kwargs)
TCP server listening on port 88
  File "servers.py", line 10, in start_tcp_server
    server_socket.bind(('0.0.0.0', port))
OSError: [Errno 98] Address already in use
UDP server listening on port 89
```

Cette configuration vous permet de tester la fonctionnalité de TinyScanner en scannant votre localhost ``(127.0.0.1)`` sur les ports que vous avez ouverts avec le script serveur.


### Conclusion

TinyScanner est un outil simple pour des tâches de scan de ports basiques. Bien qu'il présente des limitations, notamment dans la détection des ports UDP, il constitue une ressource éducative et un point de départ pour des diagnostics réseau plus complexes. Utilisez toujours TinyScanner de manière responsable et avec autorisation.
### Quelles sont les questions d'audit ??
[Cliquez ici pour voir les questions d'audit.](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/active/audit)

#### Authored by: [Mouhamadou Fadilou Diop](https://learn.zone01dakar.sn/git/mouhamadoufadiop/)
###### Completed during [zone01-dakar](https://learn.zone01dakar.sn/) full-stack development course.
#### Project Description: [here](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/active)
