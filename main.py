## Le script de test en local

Ce fichier sert à tester et valider le bon fonctionnement de ton code avant de l'envoyer sur GitHub.

Il importe la classe Blockchain pour initialiser une nouvelle chaîne de test.

Il utilise la méthode add_block() pour insérer plusieurs blocs contenant des données fictives.

Il parcourt toute la blockchain à l'aide d'une boucle pour afficher dans la console les détails de chaque bloc (son numéro, son hash unique et le hash du bloc précédent) afin de vérifier visuellement que le chaînage fonctionne correctement.



from blockchain import Blockchain

# Test du chaînage
ma_blockchain = Blockchain()
ma_blockchain.add_block("Données du bloc 1")
ma_blockchain.add_block("Données du bloc 2")

for bloc in ma_blockchain.chain:
  print(f"Bloc {bloc.index} | Hash: {bloc.hash} | Précédent: {bloc.previous_hash}")