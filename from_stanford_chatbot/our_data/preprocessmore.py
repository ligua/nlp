import re

file = open("Training_Shuffled_Dataset.txt","r")

data = []



for line in file:
	sentenceline = line.strip().split("\t")
	moredata = []
	for eachsen in sentenceline:
	 	moredata.append(eachsen)
	data.append(moredata)



print("Process data done")
output_file = open("trainingfile","w")

pairs = []


for triple in data:
	for i in range(len(triple)-1):
		line1 = triple[i]
		line2 = triple[i+1]
		if line1 and line2:
			pairs.append([line1, line2])


print("create data pair done")


for pair in pairs:
	[line1, line2] = pair
	output_file.write(line1+"+++$$$+++"+line2+"\n")


