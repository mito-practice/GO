from Bio import SeqIO
from collections import defaultdict
from collections import Counter
import matplotlib.pyplot as plt

muscle_res = SeqIO.parse('3_seq_from_muscle.fasta', 'fasta')

seq_len = 2368  # len of one seq, obtained manually
seq_content = defaultdict(set)

for prot_seq in muscle_res:
    for position, aa in enumerate(prot_seq):
        seq_content[position].add(aa)   # look's like {0: {'-'}}, where 0 is the num of the pos and '-' is AA in the pos
                                        # it also might be like {0: {'A', 'T'}}, meaning, on that pos there were more
                                        # than one AA at the pos in different sequences

conservative_aa = []
for aa_set in seq_content.values():
    if len(aa_set) == 1 and aa_set != {'-'}:
        conservative_aa.append(aa_set.pop())  # pop to have str in the list, not sets

counted_aa = Counter(conservative_aa)

aa_name = []
occurrence = []

for k, v in counted_aa.items():
    aa_name.append(k)
    occurrence.append(v)

plt.bar(aa_name, occurrence, width=0.8)
plt.title('AA conservativeness')
plt.xlabel('AA')
plt.ylabel('Times being conservative')
plt.savefig('AA conservativeness.PDF', format='PDF')


