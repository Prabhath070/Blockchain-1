# Genesis block is the first block in the block chain . 

#Blocks and SHA256 

-> Secure Hash Algorith (256 bit size of the hash) : 32 charachters

Properties:
-> Even if one charachter changes in the original data , the algorith will produce a different output , but given the same data is encrypted again and again ,we get the same output.

-> Its a one way Hash 
-> Useful for block validation 

hashlib.sha256(final_data.encode()).hexdigest() its how its done 