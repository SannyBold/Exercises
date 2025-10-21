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
dna_seq.find("GAATTC")
dna_seq_ri_len = len(str(dna_seq[21:len(dna_seq)]))
cut_site = dna_seq.find("G", 21)
print(cut_site)

#splicing
genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = genomic_dna[:64]
exon2 = genomic_dna[91:len(genomic_dna)]
exons = exon1 + exon2
intron = genomic_dna[64:92]
print(exons)
percentagecoding=len(exons)*100/len(genomic_dna)
print(percentagecoding)

seq = exon1.upper() + intron.lower() + exon2.upper()
print(seq)





