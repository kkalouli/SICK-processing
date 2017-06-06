# map_parses_to_pairs.py
# goes through the parsed unique sentences and matches each pair of SICK to its parse.
# author : Katerina Kalouli, 2.6.2017
import re, os, codecs


# open the input files
inConllu = open ('SICK.parsed_sensesTaggedJIGSAW_SUMOmapped.conllu', 'r')

inCsv = open ('/pairs/AnBBnA.csv', 'r') 


# read the parsed sentences (the conllu) into lines
conllu = inConllu.read()
# read the pairs from the csv file
inPairs = inCsv.readlines()


# go through the pairs
for pair in inPairs:
	if pair.startswith("pair_ID"):
		continue
	# get the pair id, sentence A and B and the entailment labels
	id = pair.split(",")[0]
	A = pair.split(",")[1]
	B = pair.split(",")[2]
	entailmentAB =  pair.split(",")[5] 
	entailmentBA =  pair.split(",")[6]
	# write all that into a newly created file, called as the pair id
	out = open ('/pairs/AnBBnA/'+id + ".txt", 'w')
	out.write("A = "+ A)
	out.write("\n")
	out.write("B = "+B)
	out.write("\n")
	out.write("Entailment A to B = "+ entailmentAB)
	out.write("\n")
	out.write("Entailment B to A = "+ entailmentBA)
	out.write("\n\n")
	# look for the specific parses within the conllu file
	regexA = "# "+re.escape(A)+ "(.*\n)+?(?=\n)"
	matchA = re.search(regexA, conllu)
	if matchA:
	# write them into the output file
		A_to_write = matchA.group()
		out.write("Conllu A:\n")
		out.write(A_to_write)
	regexB = "# "+re.escape(B)+ "(.*\n)+?(?=\n)"
	matchB = re.search(regexB, conllu)
	if matchB:
		B_to_write = matchB.group()
		out.write("\nConllu B:\n")
		out.write(B_to_write)
	
# close the files	
inConllu.close()
inCsv.close()
	