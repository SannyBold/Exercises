#!/usr/bin/python3

myhome = os.environ['HOME']

import shutil
import os
import subprocess

#copy files into work directory
shutil.copytree("/localdisk/data/BPSM/Lecture13", myhome + "Exercises/Lecture13")

os.chdir(myhome + "/Exercises/Lecture13")

#open input sequence file, read and split into a list separated by newlines 
with open("input.txt") as input1:
    inputseq1 = input1.read()

inputseqs = inputseq1.split()

#index out adaptors in list
finalseq = ""
noadaptorseqs = []
for seq in inputseqs:
    finalseq = seq[14:]
    noadaptorseqs.append(finalseq)
noadaptorseqs

#write adaptorless sequences to file
with open("input_no_adaptor.txt", "w") as output:
     for seq in noadaptorseqs:
         output.write(seq + "\n")

with open("input_no_adaptor.txt") as inputcount:
    inputcount = inputcount.read().split()
    for seq in inputcount:
        print(len(seq))

#extract index positions (start, stop)
with open("exons.txt") as indexgen:
    indexgen =  indexgen.read().split()

indexsplit = []
for i in indexgen:
    indexsplit += i.split(",")

#set start and stop lists with corresponding indexes

starti = indexsplit[::2]

stopi = indexsplit[1::2]

#amend sart positions to meet python indexing start positions
starti2 = []
for i in starti:
    starti2.append(int(i) - 1)


with open("genomic_dna2.txt") as dna2:
    dna2 = dna2.read()

#loop through length of start positions and substitute index for each positional start and stop values
exonseq = []
for i in range(len(starti2)):
    s = int(starti2[i])
    e = int(stopi[i])
    exonseq.append(dna2[s:e])


with open("genomic_dna2_exons.txt", "w") as output2:
    for seq in exonseq:
        output2.write(seq + "\n")

#sliding windows

string = "abcdefghijk"

offset=1

for i in range(len(string) - 6 +1, offset):
    window = string[i : i + 7]
    print(i, window)




with open("H2Bcoding.fasta") as H2Bseq:
    H2Bseq = H2Bseq.read().split("\n")
    H2Bseq = "".join(H2Bseq[1:])

#gc content calculation
offset = 3
for i in range(0, len(H2Bseq) - 30 + 1, offset):
    gc=0
    window = H2Bseq[i : i + 30]
    for base in window:
        if base in {"G", "C"}:
            gc += 1
    gc_content = gc*100/30
    print(window, gc_content)
    with open(f"window_{i}.out1", "w") as output:
        output.write(">H2B windows\n" + window)
    if i == 0: 
        with open("H2B_windows_tot.out1", "w") as output2:
            output2.write(">H2B windows\n" + window + "\n")
    else:
        with open("H2B_windows_tot.out1", "a") as output2:
            output2.write(window + "\n")



#print windows including partial
for i in range(0, len(H2Bseq) + 1, offset):
    window = H2Bseq[i : i + 30]
    print(window)

#take sequences from collection of files and sort based on size

os.chdir(myhome + "/Exercises/Lecture13")

for ilower in range(100, 1000, 100):
    iupper = ilower + 99
    dirname = str(ilower)+ "-" + str(iupper)
    os.mkdir(dirname)

for filename in listdir(myhome + '/Exercises/Lecture13'):
    if filename.endswith('.dna'):
        with open(filename) as file:
            file = file.read().split("\n")
            for seq in file:
                num = len(seq)
                for ilower in list(range(100, 1000, 100)):
                    iupper = ilower + 99
                    dirname = str(ilower)+ "-" + str(iupper)
                    if num >= ilower and num <= iupper:
                        output_path = dirname + "/" + "seq.dna"
                        with open(output_path, "a") as output:
                            output.write(seq + "\n")
                        




#bases = []
#for i in range(1, 10):
    #os.mkdir(f"{i*100}base")
    #bases.append(i*100)
    #
#
#with os.scandir(myhome + "/Exercises/Lecture13") as es:
    #for file in es:
        #if file.name.endswith(".dna"):
            #with open(file.path) as dna:
                #dna = dna.read().split()
                #for seq in dna:
                    #num = len(seq)
                    #for b in bases:
                        #if num < b:
                            #name = f"{num}base.txt"
                            #with open(os.path.join(out, name), "a") as out:
                                #out.write(seq + "\n")
#
#










    


