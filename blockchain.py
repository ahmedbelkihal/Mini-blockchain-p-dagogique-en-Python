## Le chaînage et la gestion de la chaîne

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