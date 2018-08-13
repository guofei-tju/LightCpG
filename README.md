# LightCpG

Input：BED format file

The format of BED file as follow,

Chromosome number-----position-----reads-----methylation state

chr1	136409		4		0

chr1	136423		6		1

chr1	136425		6		0

chr1	136473		4		1

chr1	839397		4		0

chr1	839398		6		0

chr1	839400		4		0

chr1	839401		6		0

chr1	852002		7		0

No.1 Feature extraction:

Sequence feature：

(1) DNA sequence is extracted by using the sequence_extract.py, in which hg19 database is necessary.

(2) n-gram feature is extracted by using demo.txt according the extracted sequence.


Structural feature:

Structural feature is extracted by using demo.txt, in which structural feature files are necessary.

CGI file is downloaded from the UCSC genome browser[1].

Transcription factor binding sites (TFBS), histone modification marks, chromatin states, and DNase I hypersensitive sites (DHSs) feature files are downloaded from the ENCODE[2].

Integrated Haplotype Score (iHS) is downloaded from http://hgdp.uchicago.edu/Browser_tracks/iHS.

GERP++ Constraint Score is downloaded from the SidowLab GERP++ tracks on hg19[3].


Positional feature:

Positional_feature.m is used to extract positional feature, in which multiple single-cell sequencing files are necessary.

No.2 Feature combination:

We combinate sequence feature, structural feature, positional feature to construct feature set.

No.3 classifier:

In our paper, five classifiers are employed to construct prediction model, including LightGBM[4], XGboost[5], Deep learning, Random Forset and GBDT.


References:

[1] Kent WJ, Sugnet CW, Furey TS, Roskin KM, Pringle TH, Zahler AM, et al. The human genome browser at UCSC. Genome Research. 2002;12(6):996-1006.

[2] Consortium EP. The ENCODE (ENCyclopedia of DNA elements) project. Science. 2004;306(5696):636-40.

[3] Davydov EV, Goode DL, Sirota M, Cooper GM, Sidow A, Batzoglou S. Identifying a High Fraction of the Human Genome to be under Selective Constraint Using GERP++. Plos Computational Biology. 2010;6(12):e1001025.

[4] Ke G, Meng Q, Finley T,Wang T, Chen W, Ma W, et al. LightGBM: A Highly Efficient Gradient Boosting Decision Tree. Advances in Neural Information Processing Systems. 2017, 3146–3154.

[5] Chen T, He T, Benesty M, Khotilovich V, Tang Y. XGBoost: A Scalable Tree Boosting System. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining. 2016.
























