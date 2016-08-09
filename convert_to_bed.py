'''
This script read AJHG table and convert it into a bed file,
listing 20kbp region around the eQTL site.
'''


import sys
from itertools import islice  

def main(filename):
	fileout = open(filename + "_converted.bed","w")

	#print filename

	filein = open(filename,"r")

	for line in islice(filein, 1, None):  
		elements = line.strip().split("\t")
		if (int(elements[5])-10000) < 0:
			print "FUCK"
			break
		fileout.write("chr"+elements[4] +"\t" +  str(int(elements[5])-10000) +"\t"+ str(int(elements[5])+10000) + "\t"+ elements[0] +"\t0\t"+ elements[6] + "\n")


if __name__ == "__main__":
	main(sys.argv[1])