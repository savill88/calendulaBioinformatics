import sys
from Bio import Entrez

#0:python script name, 1: database name, 2:search term, 3: name of the file, 4: file format 
#return type
commandLineArg=sys.argv 


Entrez.email="sshrest3@ramapo.edu"
search_handle=Entrez.esearch(db=commandLineArg[1], term=commandLineArg[2], useHistory="y")
search_results= Entrez.read(search_handle) #XML format
#print(search_results)
search_handle.close()

gi_list= search_results["IdList"]
count= int(search_results["Count"])
print(count)
session_cookie=search_results["WebEnv"]
query_key=search_results["QueryKey"]

#using the search results and the history feature in the Entrez to fetch sequences
batch_size= 20
handle_sequence=open(commandLineArg[3], "w")
for start in range(0, count, batch_size):
           end=min(count, start+batch_size)
           print("Going to download record %i to %i" % (start+1, end))
           fetch_handle= Entrez.efetch(db=commandLineArg[1], rettype=commandLineArg[4], retstart=start, retmax= batch_size, webenv=session_cookie, query_key=query_key)
           data=fetch_handle.read()# can't use Entrez.read(fetch_handle) because the file is not in XML 
           fetch_handle.close()
           handle_sequence.write(data)
handle_sequence.close()




     
