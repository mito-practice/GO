import random
from Bio.Blast import NCBIWWW
#generate seq of random length
length = random.randint(100, 1000)
seq = ''.join(random.choices('ATGC', k=length))

result_handler = NCBIWWW.qblast("blastn", "nr", seq)
print(result_handler)
with open('results.xml', 'w') as save_file:
    blast_res = result_handler.read()
    save_file.write(blast_res)