#!/usr/bin/python3

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#count As
Acount = dna_seq.count("A")
#count Ts
Tcount = dna_seq.count("T")
(Acount+Tcount)/len(dna_seq)

#complement of dna sequence
complement_seqr1=dna_seq.replace("A", "t")
complement_seqr2=complement_seq1.replace("T", "a")
complement_seqr3=complement_seqr2.replace("G", "c")
complement_seq=complement_seqr3.replace("C", "g")
print(complement_seq)

#find Ecori site
dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
len_cut_1 = dna_seq.find("GAATTC") + 1
len_cut_2 = len(str(dna_seq[len_cut_1:]))
print(cut_site)

#splicing
genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = genomic_dna[:63]
exon2 = genomic_dna[90:]
exons = exon1 + exon2
intron = genomic_dna[62:91]
print(exons)
percentagecoding=len(exons)*100/len(genomic_dna)
print(percentagecoding)

seq = exon1.upper() + intron.lower() + exon2.upper()
print(seq)





