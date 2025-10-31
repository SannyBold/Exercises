#!/usr/bin/python3

import os, shutil, subprocess

shutil.copy("/localdisk/data/BPSM/Lecture14/data.csv", "/localdisk/home/s2850039/Exercises/Lecture14/data.csv")

os.system("head data.csv")

list_complete = []
with open("data.csv") as datafile:
    datafile = datafile.read().split("\n")
    for val in datafile:
        list2 = val.split(",")
        list_complete.append(list2)

list_complete.pop()

targets = {'Drosophila melanogaster', 'Drosophila simulans'}

for val in list_complete:
    if val[0] in targets:
        print(val[2])

for val in list_complete:
    if len(val[1]) > 89 and len(val[1]) < 110:
        print(len(val[1]), val[2])

#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.

for val in list_complete:
    at_c = (val[1].count("a") + val[1].count("t"))/len(val[1])
    if at_c < 0.5:
        print(val[2])

#Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.

for val in list_complete:
    if val[2].startswith("k") and val[0] != "Drosophila melanogaster" or val[2].startswith("h") and val[0] != "Drosophila melanogaster":
        print(val[2])

#For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).

for val in list_complete:
    at_c = (val[1].count("a") + val[1].count("t"))/len(val[1])
    if at_c < 0.65:
        print(f"{val[2]} high at")
    elif at_c > 0.45 and at_c < 0.65:
        print(f"{val[2]} med at")
    else:
        print(f"{val[2]} low at")
#Write a programme/script that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than some number of times n (you chose what the number n is!). 

dna="ATGCATCATGAAGCTGTTGAACGTATG"
k=2
n=3

bases = []
for i in range(0, len(dna)-k+1, 1):
    bases.append(dna[i:i+k])

high_bases = set()

for a in bases:
    if bases.count(a) > n:
        high_frequency = bases.count(a)
        high_bases.add(a) 


print(highest_base, highest_frequency)

#Pairwise distances: how similar are two sequences? Here is a list of DNA sequences that are all equal in length, with varying degrees of similarity to each other: 

#iterate over sequence count and change index each time for the sequence to compare the others against
#in the loop before index + 1, iterate over rest of sequences and compare bases, exclude the same sequence

listdna = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT'] 

overlapping_per_pairs = []
count=0
indexpos=0
valcompare = ""
for seq_index in range(len(listdna)):
    seqcompare = listdna[seq_index]
    for seq in listdna:
        count = 0
        if seq != seqcompare:
            for base in range(0, len(seq), 1):
                if seq[base] == seqcompare[base]:
                    count += 1
            percent_sim = count*100/len(seq)
            overlapping_per_pairs.append(f"{seq}_{seqcompare}_{percent_sim}")




