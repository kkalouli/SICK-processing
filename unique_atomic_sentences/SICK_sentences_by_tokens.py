# SICK_sentences_by_tokens.py
# produces a csv file with two columns. The first column is the sentence and the second one
# is the number of tokens of that sentence
# author : Katerina Kalouli, 31.05.2017
import re, os, codecs


# open the input and output files
inFile = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/SICK_unique_sentences.csv', 'r')

out = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/SICK_sentences_by_tokens.csv', 'w')




# read the corpus into lines
inF = inFile.readlines()

# write the title row
out.write("sentence\ttokens\n")

# go through the file
for sentence in inF:
	# split the line into its tokens
	tokens = sentence.split(" ")
	# count them
	size = len(tokens)
	# write them in the output
	out.write(sentence.replace("\n", "")+"\t"+str(size)+"\n")


# close the files
inFile.close()
out.close()
	