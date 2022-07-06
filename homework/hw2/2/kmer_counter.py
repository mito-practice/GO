from Bio import SeqIO
from collections import defaultdict
import csv
import os

fasta = SeqIO.parse('GRCh37_latest_genomic.fna', 'fasta')


k = 5 # 3
kmer_freq = defaultdict(int)
for seq in fasta:
    kmer_freq['Chromosome'] = seq.id
    seq = str(seq.seq)
    for i in range(0, len(seq), 1):
        cur_kmer = seq[i : i + k]
        kmer_freq[cur_kmer] += 1
    with open('res', 'a+') as fout:
        writer = csv.DictWriter(fout, fieldnames=kmer_freq.keys())
        if os.stat("res").st_size == 0:
            writer.writeheader()
        writer.writerow(kmer_freq)




