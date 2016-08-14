#!/usr/bin/python 
#author: Safal Shrestha 
#returns an XML format file from a BLAST search using a GI number 
#parses the XML file to retrieve the GI numbers from the search 
#writes the GI number to a txt file

from Bio.Blast import NCBIWWW, NCBIXML

giNumber= int(raw_input("Please enter the GI number: "))
fileName=raw_input("Please enter the name of the xml file to which you would like to write to: ")


blastHandle=NCBIWWW.qblast("blastn", "nt", giNumber)
blastRecords= open(fileName, "w")
blastRecords.write(blastRecords.read())
blastRecords.close()
blastHandle.close()


def giParser(titleString):
	titleString=titleString.strip()
	startIndex=titleString.find('|',0)
	endIndex=titleString.find('|',startIndex+1)

	return titleString[startIndex+1:endIndex]



giList=[]

xmlFile=open(fileName)
blastRecords = NCBIXML.parse(xmlFile)

for blastRecord in blastRecords:
	for alignment in blast_record.alignments:
		stringTitle=str(alignment.title)
		giList.append(giParser(stringTitle))


giFromBlast=raw_input("Please enter the name of the text file where you would"+\
 "like to save the GI numbers of the Blast results")
f=open(giFromBlast,'w')
for ids in giList:
	f.write(ids+'\n')
f.close()