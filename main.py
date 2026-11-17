## Le script de test en local

from blockchain import Blockchain

# Test du chaînage
ma_blockchain = Blockchain()
ma_blockchain.add_block("Données du bloc 1")
ma_blockchain.add_block("Données du bloc 2")

for bloc in ma_blockchain.chain:
  print(f"Bloc {bloc.index} | Hash: {bloc.hash} | Précédent: {bloc.previous_hash}")