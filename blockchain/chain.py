import hashlib

from blockchain.block import Block


class Chain:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.blocks = []
        self.pool = []
        self.hash = None
        self.__create_origin_block()

    def proof_of_work(self, block: Block):
        self.hash = hashlib.sha256()
        self.hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == self.hash.hexdigest() \
            and int(self.hash.hexdigest(), 16) < 2 ** (256 - self.difficulty) \
            and block.previous_hash == self.blocks[-1].hash

    def add_to_chain(self, block: Block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_data_to_pool(self, data: str):
        self.pool.append(data)

    def __create_origin_block(self):
        self.hash = hashlib.sha256()
        self.hash.update(''.encode('utf-8'))
        first_block = Block("First Block", self.hash)
        first_block.mine(self.difficulty)
        self.blocks.append(first_block)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(difficulty=self.difficulty)
            self.add_to_chain(block)
            pretty_print_block(block=block)

    def visualize_blockchain(self):
        for block in self.blocks:
            pretty_print_block(block=block)


def pretty_print_block(block: Block):
    print("\n\n=============================")
    print("Hash:\t\t", block.hash.hexdigest())
    print("Previous Hash:\t\t", block.previous_hash.hexdigest())
    print("Nonce:\t\t", block.nonce)
    print("Data:\t\t", block.data)
    print("\n\n=============================")
