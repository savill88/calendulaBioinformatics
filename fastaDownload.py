#!/usr/bin/python 
#author: Safal Shrestha 
#general script that searches the entrez database and returns the list of GI numbers 

from Bio import Entrez 
Entrez.email="sshrest3@ramapo.edu"

nameDatabase= raw_input("Please enter the name of the database you would like to enter:")
searchTerm=raw_input("Please enter the search term: ")
boolHistory=raw_input("Would you like to use the history feature with the search ('y' for Yes and 'n' for No)")



handleSearch= Entrez.esearch(db=nameDatabase, term=searchTerm, useHistory=boolHistory)
records= Entrez.read(handleSearch) 
handleSearch.close()

giList=records["IdList"]
sessionCookie=records["WebEnv"]
queryKey=records["QueryKey"]
count=int(records["Count"])



fileNameOutputFasta=raw_input("Please enter the name of the file you would like to write the sequences to: ")
batchSize=int(raw_input("Please enter the size of the batch you would like to download the sequences: "))
handleWrite=open(fileNameOutputFasta,'w')


for start in range(0, count, batchSize):
           end=min(count, start+batchSize)
           print("Going to download record %i to %i" % (start+1, end))
           fetch_handle= Entrez.efetch(db=nameDatabase, rettype="fasta", retstart=start, retmax= batchSize, webenv=sessionCookie, query_key=queryKey)
           data=fetch_handle.read()# can't use Entrez.read(fetch_handle) because the file is not in XML 
           fetch_handle.close()
           handle_sequence.write(data)
handle_sequence.close() 
