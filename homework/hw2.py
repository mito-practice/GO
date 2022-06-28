from collections import Counter
from Bio import SeqIO
import itertools

f = SeqIO.parse('seqdump.txt', 'fasta')  # one seq from human genome

def codon_counter(seq, codon_len=3):
    seq_chunks = []
    for _ in seq:
        seq_chunks += [seq[i:i+codon_len] for i in range(0, len(seq), codon_len)]  # EXPENSIVE
        seq = seq[1:]
    counted_codons = Counter(seq_chunks)
    return dict(itertools.islice(counted_codons.items(), len(counted_codons) - 2))  # get rid of the last 2 nucl groups
                                                                                    # as they're di- and mononuncls


for seq in f:
    print(codon_counter(str(seq.seq).lower(), 3))
