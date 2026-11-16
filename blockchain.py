## Le chaînage et la gestion de la chaîne

Ce fichier gère la liste globale des blocs et assure la liaison logique entre eux.

Il importe la classe Block créée précédemment pour pouvoir manipuler les blocs.

La classe Blockchain initialise automatiquement la chaîne avec un premier bloc spécial appelé le "Bloc Genesis" (le point de départ de la blockchain).

La méthode add_block() permet d'ajouter de nouveaux blocs : elle récupère le dernier bloc de la chaîne, extrait son hash pour l'assigner au champ previous_hash du nouveau bloc, et l'ajoute à la liste (c'est ce mécanisme qui crée le chaînage cryptographique).


from block import Block


class Blockchain:

  def __init__(self):
    self.chain = [Block(0, "Bloc Genesis", "0")]

  def add_block(self, data):
    previous_block = self.chain[-1]
    new_block = Block(
        index=len(self.chain), data=data, previous_hash=previous_block.hash
    )
    self.chain.append(new_block)