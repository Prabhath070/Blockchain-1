from block import Block 

foo_block = Block.mineblock(Block.genesis() , 'foo')

print (foo_block.toString())


