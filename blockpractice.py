import hashlib as hasher

class Block:
    def __init__ (self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
 # here above we have created a block and initialised the information
 #that a blockcontains
 #generally the block information consists ofindex which is block number
 #time stamp that is block created time and date , data , previous hash
 #and current hash which is going to code down below
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index)+
                    str(self.timestamp)+
                    str(self.data)+
                    str(self.previous_hash))
        return sha.hexdigest()
