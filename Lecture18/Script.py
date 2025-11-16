#!/usr/bin/python3

import re

acc_list = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

#search for accessions
#contain the number 5
five_acc = []
de = []
deo = []
d_e = []
de_o = []
sxy = []
sxye = []
nums = []
u_nums = []
num_3 = []
num3m = []
edarp = []
for acc in acc_list:
    #contains a 5
    if re.search(r'5', acc):
        five_acc.append(acc)
    #contain the letter d or e
    if re.search(r'[de]', acc):
        de.append(acc)
    #contain the letters d and e in that order
    if re.search(r'de', acc):
        deo.append(acc)
    #contain the letters d and e in that order with a single letter between them
    if re.search(r'd.e', acc): #may need to specify letter
        d_e.append(acc)
    #contain both the letters d and e in any order
    if re.search(r'(d+).*(e+)', acc) or re.search(r'(e+).*(d+)', acc):
        de_o.append(acc)
    #start with x or y
    if re.search(r'^[xy]', acc):
        sxy.append(acc)
    #start with x or y and end with e
    if re.search(r'^[xy].*e$', acc):
        sxye.append(acc)
    #contains any 3 numbers in any order
    if re.search(r'\d.*\d.*\d', acc):
        nums.append(acc)
    #contains 3 different numbers in the accession
    digitset = set()
    for c in acc:
        if c.isdigit():
            digitset.add(c)
    if len(digitset) == 3:
        u_nums.append(acc)
    #contain three or more numbers in a row
    if re.search(r'\d{3,}', acc):
        num3m.append(acc)
    #end with d followed by either a, r or p
    if re.search(r'd[arp]$', acc):
        edarp.append(acc)

all_lists = [five_acc, de, deo, d_e, de_o, sxy, sxye, nums, u_nums, num3m, edarp]

index = 0

for lis in all_lists:
    index += 1
    print(f'{index}: {lis}\n')






