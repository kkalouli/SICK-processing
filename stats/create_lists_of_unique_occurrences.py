# create_lists_of_unique_occurences.py
# creates files containing lists with all unique lemmas, forms, dep and the different POS tags.
# author : Katerina Kalouli, 8.6.2017
import re, os, codecs
from collections import defaultdict

# open the input and output files
inFile = open ('SICK.parsed_sensesTaggedJIGSAW_SUMOmapped.conllu', 'r')

outN = open ('stats/unique_nouns.txt', 'w')
outV = open ('stats/unique_verbs.txt', 'w')
outADJ = open ('stats/unique_adj.txt', 'w')
outADV = open ('stats/unique_adv.txt', 'w')
outLEM = open ('stats/unique_lemmas.txt', 'w')
outFO = open ('stats/unique_forms.txt', 'w')
outDEP = open ('stats/unique_deps.txt', 'w')

# create defaultdicts for each word category and each other category
nouns=defaultdict(int)
verbs=defaultdict(int)
adj=defaultdict(int)
adv=defaultdict(int)
lemmas = defaultdict(int)
forms = defaultdict(int)
deps = defaultdict(int)

# lists of POS tags
nouns_abr = ["NN", "NNP", "NNPS", "NNS" ]
verbs_abr = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "MD"]
adj_abr = ["JJ", "JJR", "JJS"]
adv_abr = ["RB", "RBR", "RBS"]


# read the conllu into lines
inF = inFile.readlines()

# go through each line
for line in inF:
	# skip comment line
	if line.startswith("#") or line.startswith("\n"):
		continue
	# get the form
	form = line.split("\t")[1]
	# get the pos tag
	pos = line.split("\t")[4]
	# get the lemma
	lemma = line.split("\t")[2]
	# get the dep
	dep = line.split("\t")[7]
	# adding the occurrences to the dicts
	# the . has a straight lemma so it is excluded from the lemmas
	if form != ".":
		lemmas[lemma] +=1
	forms[form] +=1
	deps[dep] +=1
	# depending on the pos tag, add the lemma to the corresponding dict and increment its occurences
	if pos in nouns_abr:
		nouns[lemma] += 1
	if pos in verbs_abr:
		verbs[lemma] += 1
	if pos in adj_abr:
		adj[lemma] += 1
	if pos in adv_abr:
		adv[lemma] += 1
		
	
# sort the dicts by decreasing values and write them into the output files	
for element in sorted(nouns, key=nouns.get, reverse=True):
	outN.write(element+"\t"+str(nouns.get(element))+"\n")
	
for element in sorted(verbs, key=verbs.get, reverse=True):
	outV.write(element+"\t"+str(verbs.get(element))+"\n")
	
for element in sorted(adj, key=adj.get, reverse=True):
	outADJ.write(element+"\t"+str(adj.get(element))+"\n")
	
for element in sorted(adv, key=adv.get, reverse=True):
	outADV.write(element+"\t"+str(adv.get(element))+"\n")
	
for element in sorted(lemmas, key=lemmas.get, reverse=True):
	outLEM.write(element+"\t"+str(lemmas.get(element))+"\n")
	
for element in sorted(forms, key=forms.get, reverse=True):
	outFO.write(element+"\t"+str(forms.get(element))+"\n")
	
for element in sorted(deps, key=deps.get, reverse=True):
	outDEP.write(element+"\t"+str(deps.get(element))+"\n")
	

	
	


		