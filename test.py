def giParser(titleString):
	titleString=titleString.strip()
	startIndex=titleString.find('|',0)
	endIndex=titleString.find('|',startIndex+1)

	return titleString[startIndex+1:endIndex]

titleString="gi|3243232525|etsdgsg"
giParser(titleString)


