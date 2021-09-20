
def run(file):

	count = 0
	dic = []

	print('open ' + file)

	f = open(file)

	while True:

		line = f.readline()

		if not line:
			break

		dic.append( line.strip() )
		count += 1

	print('close ' + file)

	return dic, count