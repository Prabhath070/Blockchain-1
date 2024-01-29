from datetime import datetime
from sha256 import Sha256
class Block:
    def __init__(self, time_stamp , last_hash , current_hash , data):
        self.time_stamp = time_stamp
        self.last_hash = last_hash
        self.current_hash = current_hash
        self.data = data
    
    def toString(self):
        return "Block with time stamp: " + str(self.time_stamp) + "with last hash: " + str(self.last_hash) + "with current hash: " + str(self.current_hash) + "with data: " + str(self.data)

    def genesis():
        return Block('Genesis Time', '---' , 'fffr-fffr' , [])

    def mineblock(last_block , data ):
        time_stamp  = datetime.now()
        last_hash = last_block.current_hash
        current_hash  = Block.hash_function(time_stamp , last_hash , data) #hashlib.sha256(data_to_hash.encode()).hexdigest()
        return Block(time_stamp , last_hash , current_hash , data)

    def hash_function(time_stamp , last_hash , data):
        return Sha256.encrypt_data(time_stamp , last_hash , data)


    




