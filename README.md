# nanopore_sequencing
Repeoducing a nanopore sequencing experiment by following the workflow mentioned in the reference paper.
The basecalled fast5 reads could be dowloaded from gigaDB. The basic stats/metrics could be obtained by using Poretools. Poretools could also convert fast5 reads to fasta or fastq format for alignment. And then the reads were aligned to reference genome (Escherichia coli str. K-12 substr. MG1655). The following is the pipeline.
<img width="714" alt="pipeline" src="https://cloud.githubusercontent.com/assets/15060044/24547734/dbdf0746-1643-11e7-8c4f-e5647f71d855.png"> 

### Reference paper
A reference bacterial genome dataset generated on the MinION™ portable single-molecule nanopore sequencer
##### Links
<https://academic.oup.com/gigascience/article-lookup/doi/10.1186/2047-217X-3-22>
#### Data 
<http://gigadb.org/dataset/100102>
###reference genome: Escherichia coli str. K-12 substr. MG1655
<https://www.ncbi.nlm.nih.gov/nuccore/U00096.2>

### Tools used
1. Poretools
<https://github.com/arq5x/poretools>,<http://poretools.readthedocs.io/en/latest/>
2. LAST aligner
<http://last.cbrc.jp/>
3. Test data (999 reads from three flowcells of 46K reads) 
<https://s3.amazonaws.com/ngs2016/ectocooler_subset.zip>
