#!/usr/bin/python3

shutil.copy("/localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt", "/localdisk/home/s2850039/Exercises/Lecture12")

os.system("""esearch -db nucleotide -query "AJ223353[ACCN]" | efetch -format fasta > H2B.fasta""")

os.system("""esearch -db nucleotide -query "AJ223353[ACCN]" | efetch -format genbank > H2B.genbank""")

os.system("""grep -v "^>" H2B.fasta > seq_H2B.txt""")


#separate coding and nc for H2B fasta CDS = 29...409

with open("seq_H2B.txt") as H2B_seq:
    H2B_whole = H2B_seq.read()
    H2B_whole = H2B_whole.replace("\n", "")

coding_H2B = H2B_whole[28:409]
nc_H2B =  H2B_whole[0:29] + H2B_whole[408:]

#write c and nc seqs to files after opening and close afterward
cH2B_outfile = open("AJ223353.1_Homo_sapiens_mRNA_for_histone_H2B_coding.fasta", "w")
cH2B_outfile.write(">AJ223353.1 Homo sapiens mRNA for histone H2B coding clone pJG4-5-15 29 ... 408 len=379\n" + coding_H2B)
cH2B_outfile.close()

ncH2B_outfile = open("AJ223353.1_Homo_sapiens_mRNA_for_histone_H2B_non_coding.fasta", "w")
ncH2B_outfile.write(">AJ223353.1 Homo sapiens mRNA for histone H2B non coding clone pJG4-5-15 1...29 & 409...808 len=428\n" + nc_H2B)
ncH2B_outfile.close()

#check for non DNA letters
non_base = 0
letters = []
for i in H2B_whole:
    if i not in {"A", "T", "C", "G"}:
        non_base += 1
        if i not in letters:
            letters.append(i)
print(non_base)

#plain genomic seq

os.system("""grep -v "^>" plain_genomic_seq.txt > pgs.txt""")

with open("pgs.txt") as g_seq:
    g_seq = g_seq.read()
    g_seq = g_seq.replace("\n", "")
    g_seq = g_seq.upper()

coding_g = g_seq[:63] + g_seq[90:]
nc_g =  g_seq[63:90]

#check for non DNA letters and clean sequence
non_base_g = 0
letters_g = []
c_g_fixed = ""
for i in coding_g:
    if i not in {"A", "T", "C", "G"}:
        non_base_g += 1
        if i not in letters_g:
            letters_g.append(i)
    else:
        c_g_fixed += i
print(non_base_g, letters_g)

non_base_g = 0
letters_g = []
nc_g_fixed = ""
for i in nc_g:
    if i not in {"A", "T", "C", "G"}:
        non_base_g += 1
        if i not in letters_g:
            letters_g.append(i)
    else:
        nc_g_fixed += i
print(non_base_g, letters_g)

#write to files

g_outfile_coding = open("plain_genomic_seq_coding.fasta", "w")
g_outfile_coding.write(">plain genomic sequence coding 1...63 & 91...126 len=98\n" + c_g_fixed)
g_outfile_coding.close()

g_outfile_non_coding = open("plain_genomic_seq_non_coding.fasta", "w")
g_outfile_non_coding.write(">plain genomic sequence non coding 64...90 len=28\n" + nc_g_fixed)
g_outfile_non_coding.close()
