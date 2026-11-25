
from block import Block
from pow import mine_block, validate_proof

# Create a test block
block = Block(1, "First transaction", "0")

# Mine the block with difficulty 2
nonce, mining_hash = mine_block(block, difficulty=2)

print("BLOCK MINED SUCCESSFULLY!")
print("--------------------------")
print("Block index:", block.index)
print("Nonce:", nonce)
print("Mining hash:", mining_hash)
print("Difficulty: 2")

# Validate the proof
is_valid = validate_proof(
    block, nonce, mining_hash, difficulty=2
)

print("Proof valid:", is_valid)
