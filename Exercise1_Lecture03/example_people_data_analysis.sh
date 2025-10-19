awk 'BEGIN {FS = "\t"} NR>1, NF == 7 && {print $0}' example_people_data.tsv | wc -l # number of people in data
awk 'BEGIN {FS = "\t"} NR>1 && NF == 7 && $6 <= 1995 {print $0}' example_people_data.tsv | wc -l # people aged around 30 or above
awk 'BEGIN {FS = "\t"} NF == 7 && $1 == "Jan"' example_people_data.tsv | wc -l # number of people named Jan
awk 'BEGIN {FS = "\t"} NR>1 && NF == 7 {print $7}' example_people_data.tsv | sort | uniq -c | sort -nr | head -1 
awk 'BEGIN {FS = "\t"} NR>1 && NF == 7 && $7 == "Mozambique" && $6 <= 1974' example_people_data.tsv | wc -l # most common country of birth and people aged 50+ from country
grep "\.edu" example_people_data.tsv | sort -t $'\t' -k7,7 -k1,1r| cut -f1,7 # details in reverse alphabetical order of names in each country with .edu emails



