#!/usr/bin/python
'''
from Bio import Entrez 
Entrez.email="sshrest3@ramapo.edu"
handle= Entrez.esearch(db="nucleotide", term="ft[gene] AND Chrysanthemum lavandulifolium [Orgn]", useHistory="y")
record= Entrez.read(handle) 
handle.close()

giList=record["IdList"]
print giList
sessionCookie=record["WebEnv"]
queryKey=record["QueryKey"]
count=int(record["Count"])
print count

'''
'''
batch_size= 20
handle_sequence=open("ftGeneChrysanthemumSearch.fasta", "w")
for start in range(0, count, batch_size):
           end=min(count, start+batch_size)
           print("Going to download record %i to %i" % (start+1, end))
           fetch_handle= Entrez.efetch(db="nucleotide", rettype="fasta", retstart=start, retmax= batch_size, webenv=sessionCookie, query_key=queryKey)
           data=fetch_handle.read()# can't use Entrez.read(fetch_handle) because the file is not in XML 
           fetch_handle.close()
           handle_sequence.write(data)
handle_sequence.close()
'''
'''
#writing the blast results onto a file in xml format
from Bio.Blast import NCBIWWW

result_handle=NCBIWWW.qblast("blastn", "nt", giList[2])
save_file= open("my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()
result_handle.close()
'''

def giParser(titleString):
	titleString=titleString.strip()
	startIndex=titleString.find('|',0)
	endIndex=titleString.find('|',startIndex+1)

	return titleString[startIndex+1:endIndex]


giList=[]
from Bio.Blast import NCBIXML

result_handle=open("my_blast.xml")
blast_records = NCBIXML.parse(result_handle)

for blast_record in blast_records:
	for alignment in blast_record.alignments:
		stringTitle=str(alignment.title)
		print stringTitle
		giList.append(giParser(stringTitle))
		

f=open('giListBlastResult.txt','w')
for ids in giList:
	f.write(ids+'\n')
f.close()