# split_SICK_to_pairs.py
# splits the SICK corpus into the different entailment relations found within the corpus
# all pairs of each relation are put into a .csv file, keeping the original ordering of SICK
# the short_stats.txt file is also produced: it holds some basic stats about the occurrences of each relation
# the file SICK_unique_sentences.csv contains all unique sentences of SICk: each sentence is given
# with the pair_id of the pair from which it originates
# author : Katerina Kalouli, 28.05.2017
import re, os, codecs


# open the input and output files
inFile = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/SICK.txt', 'r')

out1 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AcBBcA.csv', 'w')
out2 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AcBBnA.csv', 'w')
out3 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AcBBeA.csv', 'w')

out4 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AeBBeA.csv', 'w')
out5 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AeBBnA.csv', 'w')
out6 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AeBBcA.csv', 'w')

out7 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AnBBcA.csv', 'w')
out8 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AnBBeA.csv', 'w')
out9 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/AnBBnA.csv', 'w')

out10 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/short_stats.txt', 'w')
out11 = open ('/Users/kkalouli/Documents/Stanford/comp_sem/SICK/pairs/SICK_unique_sentences.csv', 'w')


# read the corpus into lines
inF = inFile.readlines()
# the list holding the unique sentences
sentences = []
# counters for the occurrences of each relation
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

# iterating through the corpus
for line in inF:
	# skip first title line
	if line.startswith('pair_ID'):
		out1.write(line)
		out2.write(line)
		out3.write(line)
		out4.write(line)
		out5.write(line)
		out6.write(line)
		out7.write(line)
		out8.write(line)
		out9.write(line)
		continue
	# split each line into its columns
	list = line.split("\t")
	# get the different info
	id = list[0]
	A_to_B = list[5]
	B_to_A = list[6]
	A = list[1]
	B = list[2]
	# add each unique sentence into the sentences list
	if A not in sentences:
		sentences.append(A)
	if B not in sentences:
		sentences.append(B)
	# do the splitting of the pairs into the corresponding files
	if A_to_B == "A_contradicts_B":
		if B_to_A == "B_contradicts_A":
			out1.write(line)
			count1 += 1
		elif B_to_A == "B_neutral_A":
			out2.write(line)
			count2 += 1
		elif B_to_A == "B_entails_A":
			out3.write(line)
			count3 += 1
	elif A_to_B == "A_entails_B":
		if B_to_A == "B_entails_A":
			out4.write(line)
			count4 += 1
		elif B_to_A == "B_neutral_A":
			out5.write(line)
			count5 += 1
		elif B_to_A == "B_contradicts_A":
			out6.write(line)
			count6 += 1
	elif A_to_B == "A_neutral_B":
		if B_to_A == "B_contradicts_A":
			out7.write(line)
			count7 += 1
		elif B_to_A == "B_entails_A":
			out8.write(line)
			count8 += 1
		elif B_to_A == "B_neutral_A":
			out9.write(line)
			count9 += 1
			
# write the unique sentences into the output file
for sent in sentences:
	out11.write(sent+"\n")
	
# fill in the stats file		
out10.write("There were " + str(count1) + " pairs of AcBBcA.\n")
out10.write("There were " + str(count2) + " pairs of AcBBnA.\n")
out10.write("There were " + str(count3) + " pairs of AcBBeA.\n")
out10.write( "There were " + str(count4) + " pairs of AeBBeA.\n")
out10.write( "There were " + str(count5) + " pairs of AeBBnA.\n")
out10.write( "There were " + str(count6) + " pairs of AeBBcA.\n")
out10.write( "There were " + str(count7) + " pairs of AnBBcA.\n")
out10.write( "There were " + str(count8) + " pairs of AnBBeA.\n")
out10.write( "There were " + str(count9) + " pairs of AnBBnA.\n")
out10.write( "There were " + str(len(sentences)) + " unique sentences.\n")

inFile.close()
out1.close()
out2.close()
out3.close()
out4.close()
out5.close()
out6.close()
out7.close()
out8.close()
out9.close()
out10.close()


