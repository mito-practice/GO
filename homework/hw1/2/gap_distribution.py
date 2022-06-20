from Bio import SeqIO
import re
from collections import defaultdict
import matplotlib.pyplot as plt

distribution = defaultdict(list)
# finds gaps (where "-" is one or more gaps) in each seq and creates defaultdict
# (key is a gap's len, value is a list of gaps of similar length)
# thus, len of the value-list = number of gaps of given length
for prot_seq in SeqIO.parse('muscle_res_prot_blastx.fasta', 'fasta'):
    match = re.findall('-+', str(prot_seq.seq))
    for gap in match:
        distribution[len(gap)].append(gap)
    sorted_gaps = sorted(distribution.items())
gap_length = []
gap_number = []
for len_num_pair in sorted_gaps:    # len_num_pair is a tuple, i.e. (2, ['--'. '--'])
    gap_length.append(len_num_pair[0])
    gap_number.append(len(len_num_pair[1]))

# removed occurrences of gaps longer than 200 'cuz they're rare
plt.bar(gap_length[:139], gap_number[:139], width=0.8)
plt.title('Gap distribution')
plt.xlabel('Gap size')
plt.ylabel('Number of gaps')
plt.savefig("Gap distro.PDF", format='PDF')


