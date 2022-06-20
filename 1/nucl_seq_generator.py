import random
from Bio.Blast import NCBIWWW
#generate seq of random length
length = random.randint(100, 1000)
seq = ''.join(random.choices('ATGC', k=length))

result_handler = NCBIWWW.qblast("blastn", "nr", seq, format_type='Text')
print(seq)
print(result_handler)
with open('blasta_res.txt', 'w') as save_file:
    blast_res = result_handler.read()
    save_file.write(blast_res)
