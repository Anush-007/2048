# VERY MESSY CODE


from random import randint, choice, choices

from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN
from .constants import choices, probabilites, index



class Grid:
	grid = [
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0],
		[0, 0, 0, 0]
	]



	def __init__(self):
		maxIndex = index - 1
		self.grid[randint(0, maxIndex)][randint(0, maxIndex)] = 1

		self.actions = {
			K_LEFT : self.left,
			K_RIGHT : self.right,
			K_UP : self.up,
			K_DOWN : self.down
		}


	def right(self):
		for index, row in enumerate(self.grid):
			lastIndex = len(row) - 1
			i = lastIndex - 1
			j = lastIndex
			# Doubling if pairs are found
			possibleIndices = []
			while i >= 0:
				if row[i] == row[j]:
					row[j] *= 2
					row[i] = 0
					i -= 2
					j = i + 1
				elif row[i] == 0:
					i -= 1
				else:
					j = i
					i -= 1
			row = [i for i in row if i != 0] # removing all zeros
			zeros = [0] * (index - len(row)) # adding zeros to make the list of proper size
			row = zeros + row
			self.grid[index] = row
			if row[0] == 0:
				possibleIndices.append(index)
		if len(possibleIndices) > 0:
			self.grid[choice(possibleIndices)][0] = choices(choices, probabilites)[0]

	def left(self):
		possibleIndices = [] # indices where we can spwan new number
		for index, row in enumerate(self.grid):
			i = 0
			j = 1
			# Doubling if pairs are found
			while j < len(row):
				if row[i] == row[j]:
					row[i] *= 2
					row[j] = 0
					j += 2
					i = j - 1
				elif row[j] == 0:
					j += 1
				else:
					i = j
					j += 1
			row = [i for i in row if i != 0] # removing all zeros
			zeros = [0] * (index - len(row)) # adding zeros to make the list of proper size
			row += zeros
			if row[-1] == 0:
				possibleIndices.append(index)
			self.grid[index] = row
		if len(possibleIndices) > 0:
			self.grid[choice(possibleIndices)][-1] = choices(choices, probabilites)[0]

	def down(self):
		for i in range(index):
			k = index - 1
			j = k - 1
			while (j >= 0):
				if self.grid[j][i] == self.grid[k][i]:
					self.grid[k][i] *= 2
					self.grid[j][i] = 0
					j -= 2
					k = j + 1
				elif self.grid[j][i] == 0:
					j -= 1
				else :
					k = j
					j -= 1
			col = [self.grid[t][i] for t in range(index) if self.grid[t][i] != 0]
			col = ([0] * (index - len(col))) + col
			for ind, item in enumerate(col):
				self.grid[ind][i] = item
		possibleInices = [i for i in range(index) if self.grid[0][i] == 0]
		if (len(possibleInices) > 0):
			self.grid[0][choice(possibleInices)] = choices(choices, probabilites)[0]

	def up(self):
		for i in range(index):
			j , k = 0, 1
			while k < index:
				if self.grid[j][i] == self.grid[k][i]:
					self.grid[j][i] *= 2
					self.grid[k][i] = 0
					k += 2
					j = k - 1
				elif self.grid[k][i] == 0:
					k += 1
				else :
					j = k
					k += 1
			col = [self.grid[t][i] for t in range(index) if self.grid[t][i] != 0]
			col = col + ([0] * (index - len(col)))
			for ind, item in enumerate(col):
				self.grid[ind][i] = item
		possibleInices = [i for i in range(index) if self.grid[-1][i] == 0]
		if (len(possibleInices) > 0):
			self.grid[-1][choice(possibleInices)] = choices(choices, probabilites)[0]

	def move(self, key):
		self.actions.get(key)()