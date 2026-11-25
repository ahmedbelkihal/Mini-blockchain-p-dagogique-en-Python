
import hashlib


def calculate_mining_hash(block, nonce):
    """
    Calculate the block hash including the nonce.
    The original block.py remains unchanged.
    """

    block_contents = (
        str(block.index)
        + str(block.timestamp)
        + str(block.data)
        + str(block.previous_hash)
        + str(nonce)
    )

    return hashlib.sha256(
        block_contents.encode()
    ).hexdigest()


def mine_block(block, difficulty=2):
    """
    Mine a block using Proof of Work.
    """

    if not isinstance(difficulty, int) or difficulty < 1:
        raise ValueError("Difficulty must be a positive integer")

    nonce = 0
    target = "0" * difficulty

    mining_hash = calculate_mining_hash(block, nonce)

    while not mining_hash.startswith(target):
        nonce += 1
        mining_hash = calculate_mining_hash(block, nonce)

    return nonce, mining_hash


def validate_proof(block, nonce, mining_hash, difficulty=2):
    """
    Validate the Proof of Work.
    """

    if not isinstance(difficulty, int) or difficulty < 1:
        return False

    calculated_hash = calculate_mining_hash(block, nonce)

    return (
        calculated_hash == mining_hash
        and mining_hash.startswith("0" * difficulty)
    )