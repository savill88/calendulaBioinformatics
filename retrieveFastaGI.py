#author: Safal Shrestha 
#projectName: calendulaOfficinalisBioinformatics
#this python file takes commandline argument with the filename containing a text file 
#with GI numbers 
#works with command line arguments as well as with prompts


import sys
from Bio import Entrez

Entrez.email="sshrest3@ramapo.edu"


giList=[]
if len(sys.argv)>1:
	commandLineArgs=sys.argv
	fileInput=open(commandLineArgs[1], 'rb+') 
else:
	fileNameInput= raw_input("Please enter the name of the file with GI numbers in .txt format: ")
	fileInput=open(fileNameInput, 'rb+')

for line in fileInput:
	giNum=line.strip()
	giList.append(str(giNum))

fileInput.close()


if len(sys.argv)>2:
	fileOutput=open(sys.argv[2], "w")
	
else:
	print "The file name for output does not exists."	
	fileNameOutput=raw_input("Please enter the name of the file name you "+\
		"would like to write to in .fasta format:  ")
	fileOutput=open(fileNameOutput, "w")
efetchHandle=Entrez.efetch(db="nuccore", rettype= "fasta", id= giList)
records= efetchHandle.read() #might return an error 
efetchHandle.close()
fileOutput.write(records)
fileOutput.close()




