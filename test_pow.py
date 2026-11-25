
from blockchain import Blockchain
from pow import mine_block, validate_proof

my_blockchain = Blockchain()

my_blockchain.add_block("First transaction")

block = my_blockchain.chain[-1]

nonce, mining_hash = mine_block(block, difficulty=2)

print("BLOCK MINED SUCCESSFULLY!")
print("Nonce:", nonce)
print("Mining hash:", mining_hash)
print("Proof valid:", validate_proof(block, nonce, mining_hash, difficulty=2))
