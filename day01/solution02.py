# %% load and inspect input
with open('day01/input.txt', 'r') as f:
    inpt_str = f.read()
print(inpt_str)

# %% split blocks
str_blocks = inpt_str.strip().split('\n\n')
print(str_blocks)

# %% split numbers in blocks
str_blocks_split = [block.split('\n') for block in str_blocks]
print(str_blocks_split)

# %% cast numbers to integers and sum
sum_blocks = [sum(map(int, block)) for block in str_blocks_split]
print(sum_blocks)

# %% sort
sum_blocks.sort()
print(sum_blocks)

# %% print result
print(sum(sum_blocks[-3:]))
