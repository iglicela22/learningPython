# Loop starts from 99 and counts down to 1 (not including 0), stepping by -1
for x in range(99, 0, -1):
    
    # Print how many bottles are currently on the wall
    print(f'{x} bottles of beer on the wall')
    
    # Print how many bottles of beer are there
    print(f'{x} bottles of beer')
    
    # Print the action of taking one bottle down
    print('Take one down, pass it around')
    
    # Print the number of bottles left on the wall (x - 1)
    print(f'{x-1} bottles of beer on the wall')
