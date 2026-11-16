## La classe Block et le hachage SHA-256
ce fichier définit la structure de base d'un bloc individuel au sein de la blockchain.

il importe le module hashlib pour l'algorithme de hachage sécurisé et time pour horodater chaque bloc.

La classe Block initialise les attributs essentiels : l'index du bloc, son horodatage (timestamp), les données qu'il transporte (data), et le hash du bloc précédent (previous_hash).

La méthode calculate_hash() rassemble toutes ces informations sous forme de texte, les convertit en octets, et applique la fonction cryptographique SHA-256 pour générer une empreinte unique et infalsifiable.import hashlib
import time


class Block:

  def __init__(self, index, data, previous_hash=''):
    self.index = index
    self.timestamp = time.time()
    self.data = data
    self.previous_hash = previous_hash
    self.hash = self.calculate_hash()

  def calculate_hash(self):
    block_contents = (
        str(self.index)
        + str(self.timestamp)
        + str(self.data)
        + str(self.previous_hash)
    )
    return hashlib.sha256(block_contents.encode()).hexdigest()
