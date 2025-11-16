#!/usr/bin/python3


#What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.
#What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
#What are the sequences of the fragments themselves?
import os, re

with open("long_dna.txt") as dna:
    dna = dna.read().strip()

bpsmI='A[ATCG]TAAT'
bpsmII='GC[AG][AT]TG'
last_cut=0
lastfrag=0
fragments=[]
cuts=[]
for seq in re.finditer(bpsmI, dna):
                lastfrag+=1
                cut_pos = seq.start()+3
                cuts.append(cut_pos)
                fragment_size = cut_pos-last_cut
                print(f'bpsmI digest sizes: {fragment_size}\n')
                last_cut=cut_pos
                if lastfrag == len(list(re.finditer(bpsmI, dna))):
                    fragment_size = len(dna)-last_cut
                    print(f'bpsmI digest sizes: {fragment_size}\n')

cut_pos2=0
for seq in re.finditer(bpsmII, dna):
    print(seq)
    cut_pos2 = seq.start()+4
    cuts.append(cut_pos2)

cuts.sort()

index=0
frags = []
last_cut2=0
for cut in cuts:
    index+=1
    frags.append(dna[last_cut2:cut])
    last_cut2=cut
    if index == len(cuts):
        frags.append(dna[last_cut:])

for frag in frags:
    print(f'length: {len(frag)}\nfragment: {frag}')










