screenSize = 800

title = "2048"

index = 4 # x means x * x grid

bsize =  screenSize // index

size = bsize * index

choices = [1, 2, 4]
probabilites = [0.6, 0.3, 0.1] # probabilities for various numbers to occur when a number is being spawned from choices