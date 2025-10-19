
use s2850039;

create table if not exists blasthits
(query text, subject text, pcid float, alignlen int, 
         mm int, gaps int, qstart int, qend int, substart int, 
         subend int, eval float, score float, HSP_group int) ;
truncate table blasthits;
LOAD DATA local INFILE
      '~/Exercises/Lecture06/noheader_blastoutput2.out'
      INTO TABLE blasthits
      FIELDS TERMINATED BY '\t' ;
#show hsp with mm>20
select * from blasthits where mm > 20;
#show the HSPs shorter than 100 amino acids and with more than 20 mismatches
select * from blasthits where alignlen < 100 and mm > 20;
#list the first 20 HSPs that have fewer than 20 mismatches
select * from blasthits where mm < 20 limit 20;
# how many HSPs are shorter than 100 amino acids?
select count(*) from blasthits where alignlen < 100 ;
#list the top ten highest (best) HSPs.
select * from blasthits order by score desc limit 10 ;
#list the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
select substart from blasthits where subject like "%AEI%" ;
#how many subject sequences have more than one HSP?
select sub1, sub2 from (select subject as sub1, count(*) as sub2 from blasthits group by subject) as sub where sub2 > 1 ;
#what percentage of each HSP is made up of mismatches?
select sub1, mp from (select subject as sub1, mm * 100 / alignlen as mp from blasthits) as subs;
#allocate HSPs into different groups based on their scores

update blasthits SET HSP_group = 1 where score < 100;
update blasthits SET HSP_group = 2 where score >= 300;
update blasthits SET HSP_group = 3 where score >= 400;


