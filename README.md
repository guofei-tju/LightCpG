# LightCpG

## The Framework of LightCpG

<div align=center><img width="600" height="400" src="https://github.com/guofei-tju/LightCpG/blob/master/Framework.jpg"/></div>

# Input：BED format file

> The format of BED file as follow

> Chromosome_number  position  reads  methylation_state

> chr1	 136409		4		0

> chr1	136423		6		1

> chr1	136425		6		0

> chr1	136473		4		1

> chr1	839397		4		0

> chr1	839398		6		0


# No.1 Feature extraction

## Sequence feature

> In this paper, according to the position of the CpG sites in the raw data files, we first extracted the sequence from the reference hg19, 
> including the extracted DNA sequence of 101 bp with 50 bp before and 50 bp after the CpG site. 
> Then, we employ the method of n-gram to extract sequence feature from sequence.

> ### DNA sequence is extracted by using the [**sequence_extract.py**](https://github.com/guofei-tju/LightCpG/tree/master/feature/sequence%20feature), in which hg19 database is necessary.

>> In the code, the following questions need to be attention.

>>> The 'f' is the folder where hg19 database is stored.

>>> The 'sub_f' is the folder where input file is stored

> ### n-gram feature is extracted by using [**demo.txt**](https://github.com/guofei-tju/LightCpG/tree/master/feature/sequence%20feature) according the extracted sequence.

>> In the code, the following question need to be attention.

>>> 'sequence.fasta' is the the sequence file.


## Structural feature

> In this paper, structural feature includes CGI status (CGI, CGI shore, CGI shelf), cis-regulatory elements (TFBS, DNase, chromatin states, histone modification),  
> and DNA properties (iHS, constrain score). These features reprsent the attribute of CpG site in genome. 

> ### Structural feature is extracted by using [**demo.txt**](https://github.com/guofei-tju/LightCpG/tree/master/feature/structural%20feature), in which structural feature files are necessary.

>> CGI file is downloaded from the UCSC genome browser[1].

>> Transcription factor binding sites (TFBS), histone modification marks, chromatin states, and DNase I hypersensitive sites (DHSs) feature files are downloaded from the [ENCODE](https://www.encodeproject.org/)[2].

>> Integrated Haplotype Score (iHS) is downloaded from http://hgdp.uchicago.edu/Browser_tracks/iHS.

>> GERP++ Constraint Score is downloaded from the SidowLab GERP++ tracks on hg19[3].

>> In the code, the following questions need to be attention.

>>> The 'sample_file_name' is the input file.

>>> The 'Dir_f_feature' is the folder where multiple feature files are stored.

## Positional feature

> We posit that some of the same CpG sites with unknown methylation states can be detected in multiple cells, and that the states of these sites can vary between different cells. 
> We use positional feature to reprsent the information of methylation distribution in multiple cell.

> [**positional_feature.m**](https://github.com/guofei-tju/LightCpG/tree/master/feature/positional%20feature) is used to extract positional feature, in which multiple single-cell sequencing files are necessary.

# No.2 Feature combination

> We combinate sequence feature, structural feature, positional feature to construct feature set.

# No.3 classifier

> In our paper, five classifiers are employed to construct prediction model, including [**LightGBM[4]**](https://github.com/guofei-tju/LightCpG/tree/master/classifier), [**XGboost[5]**](https://github.com/guofei-tju/LightCpG/tree/master/classifier), [**Deep learning**](https://github.com/guofei-tju/LightCpG/tree/master/classifier), [**Random Forset**](https://github.com/guofei-tju/LightCpG/tree/master/classifier) and [**GBDT**](https://github.com/guofei-tju/LightCpG/tree/master/classifier).


# References

> [1] Kent WJ, Sugnet CW, Furey TS, Roskin KM, Pringle TH, Zahler AM, et al. The human genome browser at UCSC. Genome Research. 2002;12(6):996-1006.

> [2] Consortium EP. The ENCODE (ENCyclopedia of DNA elements) project. Science. 2004;306(5696):636-40.

> [3] Davydov EV, Goode DL, Sirota M, Cooper GM, Sidow A, Batzoglou S. Identifying a High Fraction of the Human Genome to be under Selective Constraint Using GERP++. Plos Computational Biology. 2010;6(12):e1001025.

> [4] Ke G, Meng Q, Finley T,Wang T, Chen W, Ma W, et al. LightGBM: A Highly Efficient Gradient Boosting Decision Tree. Advances in Neural Information Processing Systems. 2017, 3146–3154.

> [5] Chen T, He T, Benesty M, Khotilovich V, Tang Y. XGBoost: A Scalable Tree Boosting System. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2016.
