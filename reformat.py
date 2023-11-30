

def combineArgs(lst:list,argument:int):
	temp = []
	for i in range(len(lst)):
		temp.append(lst[i][argument])
	return temp


def lst2str(superlist:list):
	rawArgs = superlist
	groupedArgs = []
	zippedArgs = []
	
	rnge = len(superlist[0])

	# grab all related arguments `i` from each sublist of rawArgs, add to a new sublist in groupedArgs
	for i in range(len(rawArgs[0])):
		groupedArgs.append(combineArgs(rawArgs,i))
	
	# convert all list items to strings
	for i in range(len(groupedArgs)):
		for j in range(len(groupedArgs[0])):
			groupedArgs[i][j] = str(groupedArgs[i][j])

	# combine each sublist of related arguments into one string separated by a comma
	for i in range(len(groupedArgs)):
		zippedArgs.append(','.join(groupedArgs[i]))

	return zippedArgs


def dic2lstlst(dic:bool):
	keys = list(dic.keys())
	values = list(dic.values())
	
	return list(map(list, zip(keys, values)))


def prettyDic(dic:dict, new:bool):
	lstlst = dic2lstlst(dic)
	out = []
	for i in range(len(lstlst)):
		temp = []
		temp.append(str(lstlst[i][0]))
		temp.append("  =  ")
		temp.append(str(lstlst[i][1]))

		out.append(''.join(temp))
	
	out = '\n'.join(out)

	if new == True:
		return ''.join(['\nNew settings: \n', out])
	else:
		return ''.join(['\nCurrent settings: \n', out])


def allStr(lst):
	if type(lst) != list:
		if type(lst) == dict:
			raise TypeError('Function reformat.allStr does not accept dictionaries, but was given one.')
		lst = [lst]

	for i in range(len(lst)):
		lst[i] = str(lst[i])

	return lst
		

def assemble(options:list, settings:list):
	for i in range(len(settings)):
		options[i*2+1] = settings[i]

	return options


def subprocessPipeGet(command:list, lineNumber:int, listItem:int):
	'''
	This function runs the given command via subprocess.Popen(command, stdout=subprocess.PIPE) and returns a specific value as specified by lineNumber and listItem.

	Parameters
	----------
	command : a list of strings to send to `subprocess.Popen()`. ex: ['echo', '"hi"']
	lineNumber : the integer of the line number to grab the item from (counting up from 1)
	listItem : the integer of the desired item in the line (counting up from 0); items are separated by a space.

	Returns
	-------
	str : all returns are formatted as strings
	'''

	import subprocess

	process = subprocess.Popen(command, stdout=subprocess.PIPE)

	for i in range(lineNumber):
		output = str(process.stdout.readline())


	# do some output processing
	# before = "b'/dev/tty1 /mnt/iventoy pxe.local 10.0.2.15'"
	output = output.split(' ') 			# ["b'/dev/tty1", '/mnt/iventoy', 'pxe.local', "10.0.2.15'"]
	item = output[listItem]				# "/mnt/iventoy"

	# if the selected item is first in the line
	if listItem == 0:							# "b'/dev/tty1"
		tempItem = []
		item = list(item)						# ['b', "'", '/', 'd', 'e', 'v', '/', 't', 't', 'y', '1']
		for i in range(len(item)):
			if i in [0,1]:
				continue
			tempItem = item.append(item[i])		# ['/', 'd', 'e', 'v', '/', 't', 't', 'y', '1']
		item = ''.join(tempItem)				# "/dev/tty1"

	# if the selected item is last in the line
	elif listItem == len(output) - 1:			# "3084'"
		tempItem = []
		item = list(item)					# ["3", "0", "8", "4", "'"]
		for i in range(len(item)):
			if i == len(item) - 1:
				continue
			tempItem = item.append(item[i])		# ["3", "0", "8", "4"]
		item = ''.join(tempItem)				# "3084"
	
	return str(item)