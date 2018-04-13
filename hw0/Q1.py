from collections import OrderedDict

def statistic(filename):
	dict = OrderedDict()
	try:
		with open(filename, 'r') as f:
			list = f.read()
			words = list.split()
			for word in words:
				dict[word] = dict.get(word, 0) + 1
	except Exception as e:
		print('Unable to open ', filename, ':', e)
		raise
	
	try:
		with open('Q1.txt', 'w') as f:
			i = 0
			n = len(dict) - 1
			for word in dict:
				f.write(word + ' ' + str(i) + ' ' + str(dict[word]))
				if i < n:
					f.write('\n')
				i = i + 1
	except Exception as e:
		print('Unable to open Q1.txt', ':', e)
		raise

		
statistic('words.txt')	
	