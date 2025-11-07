#!/usr/bin/python3
#With the aid of a function and a dictionary, write an interactive Python programme/script that will ask the user the following questions

def question_gen():
    questions = ["What's your name?", "How old are you?", "What is your favourite colour?", "Do you like Python?", "The world is flat: True or False?"]
    q_a = {}
    for q in questions:
        print(q)
        r = input()
        if q == "What's your name?":
            a = "good to meet you"
            q_a[q] = a
        elif q == "How old are you?":
            if int(r) > 21:
                a = "me too!"
                q_a[q] = a
            else:
                a = "that's a great age"
                q_a[q] = a
        elif q == "What is your favourite colour?":
            if r.upper() == "YELLOW":
                a = "best color"
                q_a[q] = a
            else:
                a = "cool"
                q_a[q] = a
        elif q == "Do you like Python?":
            if r.upper() == "YES":
                a = "great"
                q_a[q] = a
            else:
                a = "ok"
                q_a[q] = a
        elif q == "The world is flat: True or False?":
            if r.upper() == "FALSE":
                a = "that's correct"
                q_a[q] = a
            else:
                a = "you need to look this up"
                q_a[q] = a
        print(q_a.values())

#Here's a dict that stores a codon usage table for translation: 
#Write a Python programme/script that will take any DNA sequence and translate it into protein using the translation table.
#What happens if the DNA sequence contains undetermined bases (e.g. N)?
#Can you generate a translation in all three "forward" frames (transcription is on the top strand, starting at base 1, 2, and 3)?
#Can you generate a translation in all three "reverse" frames (transcription is on the bottom strand, starting at base end, end-1, and end-2)?
gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def dna_translator(dna):
    k = 3
    translation = []
    dna = dna.upper().strip(" ")
    for j in range(0, 3):
        seq_aa = ""
        for i in range(j, len(dna) - 2, 3):
            codon = dna[i:i+k]
            if codon in gencode:
                seq_aa += gencode[codon]
            else:
                seq_aa += "X"
        translation.append(seq_aa)
    return "".join(translation)

#reverse
def dna_translator_reverse(dna):
    comp = {"A":"T", "T":"A", "C":"G", "G":"C"}
    reverse_strand = ""
    for base in dna:
        reverse_strand += comp.get(base, "N")
    dna = reverse_strand[::-1].upper()
    k = 3
    translation = []
    for j in range(0, 3):
        seq_aa = ""
        for i in range(j, len(dna) - 2, 3):
            codon = dna[i:i+k]
            if codon in gencode:
                seq_aa += gencode[codon]
            else:
                seq_aa += "X"
        translation.append(seq_aa)
    return "".join(translation)

