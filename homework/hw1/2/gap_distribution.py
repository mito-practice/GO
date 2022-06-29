from Bio import SeqIO
import re
from collections import defaultdict
import matplotlib.pyplot as plt

muscle_res = SeqIO.parse('muscle_res_prot_blastx.fasta', 'fasta')

distribution = defaultdict(int)
# finds gaps (where "-" is one or more gaps) in each seq and creates defaultdict(int)
# (key is a gap's len, value is a number of occurrences)
for prot_seq in muscle_res:
    match = re.findall('-+', str(prot_seq.seq))
    for gap in match:
        distribution[len(gap)] += 1

# no need to sort, 'cuz matplotlib itself sorts the dict, right?
plt.bar(distribution.keys(), distribution.values(), width=0.8)
plt.title('Gap distribution')
plt.xlabel('Gap size')
plt.ylabel('Number of gaps')
plt.savefig('Gap distro.PDF', format='PDF')


