#!/usr/bin/python3

#Write a Python function that takes two arguments (a protein sequence and an amino acid residue code) and returns the percentage of the protein that the amino acid makes up. 

def aa_percent_calc(prot, aa):
    protein_seq = prot
    aa_code = aa
    count = 0
    for i in range(len(protein_seq)):
        if protein_seq[i] == aa_code:
            count += 1
    percent_aa = count*100/len(protein_seq)
    print(f" {aa_code} % in {protein_seq} is {percent_aa}")
    return percent_aa

#Modify the function from the previous exercise above so that it accepts a list of amino acid residues rather than a single one, and count these within the protein sequence. 
# If no list is given, the function should return the percentage of hydrophobic amino acid residues (i.e. amino acids A, I, L, M, F, W, Y, V). 

def aa_percentages_calculator(prot, aa_list=["A", "I", "L", "M"," F", "W", "Y", "V"]):
    protein_seq = prot
    aa_codes = list(aa_list)
    percentages = []
    for aa in aa_codes:
        count=0
        for i in range(len(protein_seq)):
            if protein_seq[i] == aa:
                count += 1
        percent_aa = count*100/len(protein_seq)
        percentages.append((aa, percent_aa))
        print(f" {aa} % in {protein_seq} is {percent_aa}")
    return percentages

#Write a Python function that will take a DNA sequence along with an optional threshold and return True or False to indicate whether the DNA sequence contains a high proportion of undetermined bases (i.e not A, T, G or C). Write some assertions to test whether the function works. 

def non_dna_detection(dna, threshold=20):
    seq = dna.upper()
    thresh = threshold
    non_base = 0
    for i in range(len(seq)):
        if seq[i] not in {"A", "T", "C", "G"}:
            non_base += 1
    non_base_per = non_base*100/len(dna)
    print(f"non dna percentage is {non_base_per}")
    if non_base_per < thresh:
        return False
    else:
        return True

#Write a Python function that, given any DNA sequence, will print all the k-mers (e.g. 4-mers) that occur more than n times. 

def k_mer(dna, n=3):
    seq = dna.upper()
    window = 4
    num = n
    kmers = []
    n_rep = set()
    for i in range(len(seq)):
        kmers.append(seq[i:i+window])
    for seq in kmers:
        if kmers.count(seq) > num:
            n_rep.add(seq)
    print(n_rep)
    return n_rep

#The user should be asked to supply, on the command line, the following:
#1. the sequence of interest
#2. the kmer length for analysis
#3. the threshold frequency of kmers found (i.e. the "more than this number" value)

def k_mer_int(dna, k, n=3):
    while True:
        print("enter a DNA sequence:")
        dna = str(input()).upper()
        if len(dna) > 1000:
            print("sequence too long (over 1000)")
        else:
            break
    while True:
        print("enter the kmer size:")
        k = int(input())
        if k > len(dna):
            print("window too long, longer than sequence")
        else:
            break
    print("enter the threshold frequency: default = 3")
    n = int(input())
    kmers = []
    n_rep = set()
    for i in range(len(dna)):
        kmers.append(dna[i:i+k])
    for seq in kmers:
        if kmers.count(seq) > n:
            n_rep.add(seq)
    print(n_rep)
    return n_rep

