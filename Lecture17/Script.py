#!/usr/bin/python3

#python -m venv playtime
#playtime/bin/pip install pandas
#source playtime/bin/activate
#import pandas
#deactivate


df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])

#how many fungal species have genomes bigger than 100Mb? What are their names?

'Fungi' in set(df['Group'])

df[df.apply(lambda x : x['Group'] in ['Fungi'] and x['Size (Mb)'] > 100, axis = 1)].unique().shape[0]

#how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?

df[df.apply(lambda x : x['Group'] in ['Plants', 'Animals', 'Fungi', 'Protists'] and x['Genes'] > 0, axis = 1)].unique().shape[0]

#which Heliconius species genomes have been sequenced?

df['Genus'] = df.apply(lambda x : x['#Organism/Name'].split(' ')[0], axis=1)

df[df.apply(lambda x : x['Genus'] == 'Heliconius' and x['Genes'] > 0, axis = 1)].shape[0]

Heliconus_genomes = df[df['Genus'] == 'Heliconius']

Heliconus_genomes['Genes'].notna().sum()

'Heliconius' in set(df['Genus'])

#which sequencing centre has sequenced the most plant genomes? the most insect genomes?

allplants = df[df['Group'] == 'Plants']

allplants['Center'].value_counts().head()

'Insects' in set(df['SubGroup'])

df.loc[df['SubGroup'] == 'Insects', 'Center'].value_counts().head(1)


#add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?

df['Proteins per gene'] = df['Proteins']/df['Genes']
df[df['Proteins per gene']*100 > 10]



