# Genes

For lab today, we'll be writing a piece of software that allows us to analyze the genomic information from a number of sample organisms. I have already created these samples and stored them in Codio, so all you will need to know about these is that the variable `genomes` will be automatically populated with the genomes from the files. The code to do that is below if you need it again:

```python
def count_vulnerable_genomes(fname):
  genomes = []
  with open(fname, 'r') as f:
    for line in f.readlines():
      genomes.append(line[:-1])
  # your code below here...
```

Imagine that a number of these genomes represent organisms vulnerable to some terrible affliction that can be easily treated. We only need to know a number of treatments to order to treat the organisms.

Every organism has a *genome* that is made up of four character *codons*. An example genome is `TGCG TCTT GTAC TTGA CCTG` and has 5 codons within it.

Each afflicted organism has a *marker sequence*. If the sequence `ATTT` appears in their genome, then we need to further analyze the genome to determine if the organism is afflicted.

For each genome with a marker sequence, construct a *summary chromosome* by combining the first character from each chromosome. We know if an organism is afflicted if there are more Guanine and Cytosine in the summary chromosome than Adenine and Thymine (more G and C than A and T).

## Tasks

1. Find all of the genomes that have the marker sequence in them.
2. Create a summary chromosome for the genome.
3. Count the number of afflicted organisms.
4. Return this count.

## Grader

|||topic
## Open Your Code

[Open the code file](open_file student_code/genes.py panel=2)

|||

{Check It!|assessment}(test-1176591700)

## Example

The following is an example using the input from `genes_test.txt`

From an initial input of:
```bash
TGGC GGAA AAAC GATA AACC GAGG AAAC TACA CAAT AACA CCAA CGAC AACT GTGA AGTA AGAT GTCA ATCG TTCT GTAC ACAA GAAA ATTT TAGG CAAC 
GCGA TCCT CTAA CACG CATG AAAA CACT ACAT CTAG CTGC TCAC GTAC CCTG CGGC GAGA TTTT AACG TGAT CTGT GTCC CATC TGCT TGGG GATC AGAC 
TAGT TAGT CGAA CAAC TTTG ATAC ATCG AGGC GATG TCCA GCCT TGGC ACTG TGAC GGGT GTGT ACTA CACA GTTT AGAA GCCT CCAA ATTC GGTG TGAT 
GCGA TACT ACTC ATGC GATG ATTG CCAA TAAT GCTA AAGG AGCA AGTT GCCA ATGT ACAC GAGG AAAT TAGG ACCA TAAA TGGG AGGG TGCT ATTC TATG 
CGTT GGCG CTTC ACCA TTTG CAAT CTGG CTAC TGAT ACTC CGAT CGTT AATT GTAT CCCA GAGT CTCT TAAT AATT GGTA GAGT ATTT ATTT TCAT GTTA 
ATAG TTGA GTTT TCTC ACAT GAAG GGTC GCAA TAAC CCTG CCTC CTTC GAGG CTAA CGTC TACA TTTG TAGT ATTC AGGG CCCG CCCC TTCT TTTG ATTT 
TGCG TCTT GTAC TTGA CCTG GTAG TGAT GCAG GCGA TTAC CGTA CGGA TGAC ATTA TGGA AAGT TAGG GATT ATCT AAAC CTGA TTGG ACCA TGAC ATTT 
TCCG ATGA CAGA CCTC ATGC CGCA GTAA TTAG GGGT TTTA ATTG GCGA GCAA GCGC GCGG TCTT ACCA AAGA GGTT ACCC CAGG TTGG TTTA CTAG AACG 
TTGG AATG ATTG CCAC CGCT TTAC ATTA GGTA GCTA GCGA AGCA AAGC GCGC GCGC GTGC TGCA AGTT TTTA CGAA CTCG GGTG TTCA GCTC GGGG AATG 
TGGA ACTC TCTA GATA GTAC ACGC TGGA ATAA GATC CGGC ATAC TGGA AATA GAGA GGCT GCTA ACCT CTGG CCAT ACTT ATCC ACTA CGAT TTTT ATGT
```


Four genomes are identified as containing the marker sequence.
```python
[
  'TGGC GGAA AAAC GATA AACC GAGG AAAC TACA CAAT AACA CCAA CGAC AACT GTGA AGTA AGAT GTCA ATCG TTCT GTAC ACAA GAAA ATTT TAGG CAAC ', 
  'CGTT GGCG CTTC ACCA TTTG CAAT CTGG CTAC TGAT ACTC CGAT CGTT AATT GTAT CCCA GAGT CTCT TAAT AATT GGTA GAGT ATTT ATTT TCAT GTTA ', 
  'ATAG TTGA GTTT TCTC ACAT GAAG GGTC GCAA TAAC CCTG CCTC CTTC GAGG CTAA CGTC TACA TTTG TAGT ATTC AGGG CCCG CCCC TTCT TTTG ATTT ', 
  'TGCG TCTT GTAC TTGA CCTG GTAG TGAT GCAG GCGA TTAC CGTA CGGA TGAC ATTA TGGA AAGT TAGG GATT ATCT AAAC CTGA TTGG ACCA TGAC ATTT '
]
```

These four genomes then construct summary chromosomes of:
```python
[
  'TGAGAGATCACCAGAAGATGAGATC', 
  'CGCATCCCTACCAGCGCTAGGAATG', 
  'ATGTAGGGTCCCGCCTTTAACCTTA', 
  'TTGTCGTGGTCCTATATGAACTATA'
]
```

Of these four summary chromosomes, only one exhibits the property of having more 'G' and 'C' genes than 'A' and 'T'.

The returned value should be `1`.