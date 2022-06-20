from collections import Counter
import matplotlib.pyplot as plt


with open('conservative_aa.txt') as file:
    mega_seq = file.read()

counted_aa = Counter(mega_seq)

aa_name = []
occurrence = []

for k, v in counted_aa.items():
    aa_name.append(k)
    occurrence.append(v)

plt.bar(aa_name, occurrence, width=0.8)
plt.title('AA conservativeness')
plt.xlabel('AA')
plt.ylabel('Times being conservative')
plt.savefig("AA conservativeness.PDF", format='PDF')
