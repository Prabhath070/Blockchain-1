class defining :

class Block:
    def __init__(self, time_stamp , last_hash , current_hash , data):
        self.time_stamp = time_stamp
        self.last_hash = last_hash
        self.current_hash = current_hash
        self.data = data


#def __init(self ,...) # self is required 


Static method:
#without self passing into the parameters of the class method ,it becomes a static method

def static_method():


#except for instance variables , we have to use () to call any static or non static methods

