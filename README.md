# nanopore_sequencing
Reproducing a nanopore sequencing experiment by following the workflow mentioned in the reference paper.
The basecalled fast5 reads could be dowloaded from gigaDB. The basic stats/metrics could be obtained by using Poretools. Poretools could also convert fast5 reads to fasta or fastq format for alignment. And then the reads were aligned to reference genome (Escherichia coli str. K-12 substr. MG1655). The following is the pipeline.
<img width="714" alt="pipeline" src="https://cloud.githubusercontent.com/assets/15060044/24547734/dbdf0746-1643-11e7-8c4f-e5647f71d855.png"> 

The Galaxy Workflow, 11 steps ( 7 self wrapped tools  + 4 tools from tools_shed)
<img width="854" alt="galaxy_workflow" src="https://cloud.githubusercontent.com/assets/15060044/25758616/ddf8e306-3201-11e7-95eb-6f4f4fe6f0ae.png">

### Reference paper
[A reference bacterial genome dataset generated on the MinION™ portable single-molecule nanopore sequencer](https://academic.oup.com/gigascience/article-lookup/doi/10.1186/2047-217X-3-22)
##### [Reference genome: Escherichia coli str. K-12 substr. MG1655](https://www.ncbi.nlm.nih.gov/nuccore/U00096.2)
##### GigaDB [Data](http://gigadb.org/dataset/100102)
##### Bioinformatics pipeline in paper [Github](https://github.com/arq5x/nanopore-scripts)

### Tools used
1. Poretools [GitHub](https://github.com/arq5x/poretools) [Document](http://poretools.readthedocs.io/en/latest/)
2. LAST aligner [link](http://last.cbrc.jp/)

