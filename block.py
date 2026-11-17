## La classe Block et le hachage SHA-256

import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concaténation des données du bloc pour le hachage
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Test du chaînage
genesis_block = Block(0, "Bloc Genèse", "0")
second_block = Block(1, "Deuxième bloc", genesis_block.hash)

print(f"Hash Genèse : {genesis_block.hash}")
print(f"Hash Bloc 1  : {second_block.hash}")
print(f"Previous Hash du Bloc 1 : {second_block.previous_hash}")