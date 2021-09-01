def singleton(_class) :
	instances = {}
	def getInstance(*args, **kwargs):
		if _class not in instances:
			instances[_class] = _class(*args, **kwargs)
		return instances[_class]
	return getInstance

screenSize = 800

@singleton
class Constants:
	title = "2048"

	index = 4 # x means x * x grid

	bsize =  screenSize // index

	size = bsize * index

	choices = [1, 2, 4]
	probabilites = [0.6, 0.3, 0.1] # probabilities for various numbers to occur when a number is being spawned from choices