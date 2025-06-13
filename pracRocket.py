ground = 0 

maxHeight = 100

rocketLoc = 0

print(maxHeight)

while rocketLoc <= maxHeight:
    print(f'location{rocketLoc}')
    rocketLoc = rocketLoc +1

print("Max height has been reached")

while rocketLoc > ground:
    print(f'location{rocketLoc}')
    rocketLoc = rocketLoc -1

print("Rocket has landed")
    