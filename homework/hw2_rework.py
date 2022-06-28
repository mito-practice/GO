from Bio import SeqIO
from collections import Counter

hum_genome = SeqIO.parse('GRCh37_latest_genomic.fna', 'fasta')
def codon_counter(seq):
    counted_codons = {}
    for i in range(0, len(str(seq.seq)), 3):
        codon = str(seq.seq[i:i + 3]).upper()
        return codon
l = []
for seq in hum_genome:
    for nucl in seq:
        l.append(codon_counter(seq))
        seq = seq[1:]

print(Counter(l))