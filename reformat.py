

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
