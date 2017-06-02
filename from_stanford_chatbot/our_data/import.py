import numpy as np 
import matplotlib.pyplot as plt



f = open("Training_Shuffled_Dataset.txt", 'r')
counter = 0
lenngth_sentence = []
counter = 0


for line in f:
 	#print(line+"\n")
 	counter += 1
 	line1 = line.strip().split("\t")
 	for line2 in line1:
 		words = line2.strip().split()
 		if len(words) <= 100:
 			lenngth_sentence.append(len(words))

 			

#f1 = open("whatever.txt", "w")

#for it in lenngth_sentence:
	#print(str(it)+"\n")

print(max(lenngth_sentence))

#for mm in lenngth_sentence:


length = np.array(lenngth_sentence)

plt.hist(length, bins='auto')  # plt.hist passes it's arguments to np.histogram
plt.title("Histogram with 'auto' bins")
plt.show()







f.close()
f1.close()