from Bio import SeqIO
import os
import re

if os.path.exists('translated_dna_seq_trimmed.fasta'):
        os.remove('translated_dna_seq_trimmed.fasta')
# some sequences' lengths aren't multiple of 3, so I trimmed them
def trim(seq):
        if len(seq) % 3 == 0:
                return seq
        if len(seq) % 3 != 0:
                trimmed_seq = seq[1:]
                return trim(trimmed_seq)


for dna_seq in SeqIO.parse("seqdump.txt", "fasta"):
        trimmed_dna = trim(dna_seq.seq)
        prot = str(trimmed_dna.translate())
        prot = re.sub(r'[*]?', '', prot)
        with open('translated_dna_seq_trimmed.fasta', 'a') as out:
                out.write(f'>{dna_seq.id}\n{prot}\n' )