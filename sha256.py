import hashlib
class Sha256:
    def __init__(self):
        print("Intializing the SHA256")
    
    def encrypt_data(time_stamp , last_hash , data):
        final_data = str(time_stamp) + str(last_hash) + str(data)
        return hashlib.sha256(final_data.encode()).hexdigest()
